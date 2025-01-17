import datetime

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import socket
import datetime

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
        "hostname": socket.gethostname(),
        "body": dict(await request.json()),
        "url": str(request.url),
        "ts": str(datetime.datetime.now()),
        "ip": socket.gethostbyname(socket.gethostname()),

    }
    return JSONResponse(content=response)
