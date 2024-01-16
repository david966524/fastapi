from fastapi import APIRouter
from . import myModel
from typing import Union,Optional
app01 = APIRouter()

@app01.get("/user")
def get_user_info():
    return {"msg":"user_info"}

#查询参数
#http://127.0.0.1:8080/app01/user/12?username=123&password=ddd
@app01.get("/user/{id}")
def getUserByid(id:int,username:str,password:Union[str,None]=None,email:Optional[str]=None):
    #Optional 是 Union 的一种简写，当数据有可能是str，也有可能是None 是，可以写Optional[str]=None
    #email:Union[str,None]=None,email:Optional[str]=None
    return {"msg":id,"username":username}

#json 对象
@app01.post("/user")
async def add_user(item: myModel.Item):
    print(item)
    return item
