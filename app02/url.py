from fastapi import APIRouter
from fastapi import Form
from typing import List

from fastapi import File, UploadFile

app02 = APIRouter()


@app02.get("/login")
async def login():
    return {"msg": "login"}


# form表单数据
@app02.post("/reginster")
async def regin(username: str = Form(...), max_length=16, min_length=8, regex='[a-zA-Z0-9]',
                password: str = Form(...)):
    return {"username": username, "pw": password}


# file: bytes = File()  适合小文件上传
@app02.post("/files/")
async def create_file(file: bytes = File()):
    with open("test.txt", "w") as r:
        r.write(str(file))
    print(file)

    return {"file_size": len(file)}


@app02.post('/mulitFiles')
async def mulitFiles(files: List[bytes] = File()):
    for file in files:
        print(file)

    return {"files": len(files)}


# file: Upload 适合大文件上传
@app02.post("/uploadFile")
async def upload_file(file: UploadFile):
    filename = file.filename
    with open(file.filename,"w") as f:
        for line in file.file:
            f.write(str(line))

    return {"filename": filename}
