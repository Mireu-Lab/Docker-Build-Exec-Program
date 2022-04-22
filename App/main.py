from fastapi import FastAPI, UploadFile, File
from docker_build import nodejs, python, golang, cpp
import uvicorn
import shutil
import os

app = FastAPI()

@app.get("/")
def main():
    return {"Docs" : "http://exec.mireu.xyz/"}

@app.post("/check")
def check_docker_exec(file : UploadFile = File(...)):
    file_location = f"Data/user_file/{file.filename}"
    lang = file.content_type

    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)


    if lang == "text/x-python" or lang == "application/x-python":
        return_data = python.build(file.filename)
    elif lang == "application/x-javascript" or lang == "application/x-javascript":
        return_data = nodejs.build(file.filename)
    elif lang == "text/x-go" or lang == "application/x-go":
        return_data = golang.build(file.filename)
    elif lang == "text/x-c++src" or lang == "application/x-c++src":
        return_data = cpp.build(file.filename)
    else:
        return_data = {"test build language" : lang, "message" : "unsupported service file"}


    if os.path.isfile(file_location):
        os.remove(file_location)

    return return_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)