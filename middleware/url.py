from fastapi  import APIRouter,Request

app04=APIRouter()



@app04.get("/user")
async def get_user():
    pass