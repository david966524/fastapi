import json
import queue
import threading
import time
from enum import Enum

import test_
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import asyncio
import aiohttp
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel, HttpUrl
from app01 import url as url01
from app02 import url as url02
from app03 import url as url03
from middleware import url as url04


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str]
    images: list[Image] | None = None


app = FastAPI()
app.include_router(url01.app01, prefix="/app01", tags=["app01 查询参数 ，json对象（请求体数据）"])
app.include_router(url02.app02, prefix="/app02", tags=["app02 form表单数据， 上传文件"])
app.include_router(url03.app03, prefix="/app03", tags=["app03 request response"])
app.include_router(url04.app04, prefix="/app04", tags=["app04 中间件"])

#跨域处理
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"],

)

# m1 中间件先执行 然后m2 ，response 先return给m2 m2再return m1
@app.middleware("http")
async def m2(request: Request, call_next):
    print("m2 request")
    if request.headers.get("auth") != "123456":
        return Response(content="no login", status_code=401)
    response = await call_next(request)
    print("m2 response")
    return response


@app.middleware("http")
async def m1(request: Request, call_next):
    print("m1 request")
    response = await call_next(request)
    print("m1 response")
    return response


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8080)
