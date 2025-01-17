#!/usr/bin/bash

apt-get update -y # && apt-get upgrade -y
apt-get install git python3-venv python3 gunicorn -y

cd $HOME
mkdir -p code

cd $HOME/code/
git clone https://github.com/meanother/hapi.git

cd $HOME/code/hapi
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r req.txt


SERVICE_NAME="hapi"
SERVICE_DESCRIPTION="Outline Service"
SERVICE_PATH="/root/code/hapi"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"

# Create the service file
cat > $SERVICE_FILE <<EOF
[Unit]

Description=$SERVICE_DESCRIPTION
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=$SERVICE_PATH
Environment="PATH=$SERVICE_PATH/env/bin"
ExecStart=$SERVICE_PATH/env/bin/gunicorn -w 1 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:4500 main:app

[Install]
WantedBy=multi-user.target
EOF

echo "Service file created at: $SERVICE_FILE"
systemctl daemon-reload


systemctl start $SERVICE_NAME
systemctl enable $SERVICE_NAME
systemctl status $SERVICE_NAME
