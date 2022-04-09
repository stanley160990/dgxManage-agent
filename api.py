from ast import arg
from typing import AsyncContextManager
from fastapi import Request, FastAPI, Depends, File, Form, UploadFile, status
from fastapi.param_functions import Query
from libs.Config import Config
from pydantic import BaseModel

import uvicorn
import os
import random
import string
import hashlib
import hashlib

class Create_dockerfile(BaseModel):
    id_hari : str
    username: str
    DockerImages: str

class Create_minio(BaseModel):
    username: str
    password: str



app = FastAPI()

@app.post('/Dockerfile')
async def dockerFile_data(create_dockerfile: Create_dockerfile):
    
    working_folder = Config().master_location + "/Dockerfiles/" + create_dockerfile.id_hari + "/" + create_dockerfile.username
    
    # Generate Random String
    letters = string.ascii_lowercase
    random_letter =  ( ''.join(random.choice(letters) for i in range(10)) )

    # Generate Token
    hash_token = hashlib.sha1(random_letter.encode('utf-8')).hexdigest()
    token = str(hash_token)
    
    Docker_files = working_folder + "/Dockerfile-" + token
    
    f = ''
    if os.path.isdir(working_folder) is False:
        os.mkdir(working_folder)
        f = open(Docker_files, "w")
    else:
        if os.path.isfile(Docker_files) is False:
            f = open(Docker_files, "w")
        else:
            os.remove(Docker_files)
            f = open(Docker_files, "w")
    f.write("#token:"+ token + "\n")
    f.write("FROM " + create_dockerfile.DockerImages + "\n")
    f.write("RUN mkdir /repo\n")
    f.write("RUN pip install jupyterlab\n")
    f.write('CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]')
    f.close()

    return_data = {'error': False, 'working_folder': working_folder, 'docker_file': "Dockerfile-" + token}

    return return_data

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8181, log_level="debug")
