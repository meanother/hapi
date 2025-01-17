# Run

```bash
sudo bash -c "$(curl -sL https://raw.githubusercontent.com/meanother/hapi/main/init.sh)"
```

check proxy server:
```bash
curl -X POST -d '{"k": "v"}' http://proxy_server:8082/api/info 
```
