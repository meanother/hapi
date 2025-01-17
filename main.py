from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import socket
import datetime

from core.utils import logger

SERVER_TYPE = "MIRROR"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/info", status_code=201)
async def test(request: Request):

    response = {
        "h": socket.gethostname(),
        # "body": dict(await request.json()),
        "from_url": str(request.url),
        "server_type": SERVER_TYPE,
        # "ts": str(datetime.datetime.now()),
        # "ip": socket.gethostbyname(socket.gethostname()),
    }
    logger.info(f"Response: {response}")
    return JSONResponse(content=response)
