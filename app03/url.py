from fastapi import APIRouter
from fastapi import Request
from app03 import myModel
app03=APIRouter()

# request 对象
@app03.get("/request")
async def get_request(request:Request):
    requestUrl = request.url.url  #url
    clientIp = request.client.host # 客户端ip
    agent =request.headers.get("user-agent") # user-agent
    cookies=request.cookies # cookies
    return {"requestUrl":requestUrl,"clientIp":clientIp,"agent":agent}


# response_model
@app03.post("/reginster",response_model=myModel.UserOut) #使用 userOut 对象 返回
async def create_user(user:myModel.UserIn):
    print(f'create user {user}')
    return user

'''
隐藏掉了 password
Response body
Download
{
  "username": "david",
  "email": "user@example.com",
  "fullname": "wang"
}
'''

# response_model_exclude_unset    返回对象中 排除未赋值的属性
@app03.get("/items/{id}",response_model=myModel.Items,response_model_exclude_unset=True)
async def get_items(id:str):
    itmes={
        "foo":{"name":"Foo","price":0.2},
        "bar":{"name":"Foo","price":0.2,"tags":[1,2,3,4]},
        "baz":{"name":"Foo","price":0.2,"description":"sdddd"}
    }
    return  itmes[id]