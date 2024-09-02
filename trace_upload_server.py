from fastapi import FastAPI, File, UploadFile
import os
from shutil import copyfileobj
from fastapi.middleware.cors import CORSMiddleware
import socket

app = FastAPI()

# Disable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

hostname = socket.gethostname()
test_num = 0


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    save_path = hostname  # specify your subdirectory here
    global test_num

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    with open(os.path.join(save_path, f"test{str(test_num)}.txt"), "wb") as buffer:
        copyfileobj(file.file, buffer)

    test_num += 1

    return {"filename": file.filename}
