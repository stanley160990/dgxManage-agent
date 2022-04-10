import sys
import os
import json
import string
import hashlib
import random
import uuid


from click import command

from python_on_whales import Volume, docker

from libs.Config import Config
from libs.Connections import Docker
from libs.Random import Rand_socket
from libs.REST import REST

run_type = sys.argv[1]
hari = sys.argv[2]

# psql_con, psql_cur = Psql(Config().database_host, Config().database_port, Config().database_database, Config().database_user, Config().database_password).connect()
docker_con = Docker(Config().master_docker_sock).connect()

if run_type == "build":
    url_build_data = Config().master_url + "/approval/" + hari + "/" + Config().agent_id_mensin
    build_data = REST("GET", url_build_data, {}, {}).send()
    
    for data in build_data.json()['data']:
        tag = uuid.uuid4()
        images_name = str(data['id']) + ":" + str(tag)

        docker_con.images.build(path=data['working_dir'], dockerfile=data["docker_file"], tag=images_name) 

        # token = token.replace("#token:", "")
        headers = {'Content-Type': 'application/json'}
        payload = {'img_name':data['id'], 'tag': str(tag), 'id':data["id"]}
        
        url_update_data = Config().master_url + "/build"
        response = REST('POST', url_update_data, headers, json.dumps(payload)).send()

        print (response.json())
elif run_type == "run":

    url_run_data = Config().master_url + "/build/" + hari + "/" + Config().agent_id_mensin
    run_data = REST("GET", url_run_data, {}, {}).send()

    for data in run_data.json()['data']:
        url_mig_data = Config().master_url + "/mig/" + data['id_schedule']
        mig_data = REST("GET", url_mig_data, {}, {}).send()
        
        image_name = data['img_name'] + ":" + str(data['tag'])

        container_id = uuid.uuid4()

        gpu = '"device='+ mig_data.json()['mig_device'] +'"'
        container_name = str(container_id)
        free_socket = Rand_socket("free").random()
        port_publish = [("0.0.0.0:" + str(free_socket), 8888, "tcp")]

        if hari == "1":
            # 56 user
            print("senin")
            doc_cpu = 3
            doc_ram = '12g'
        elif hari == "2":
            # 56 user
            print("selasa")
            doc_cpu = 3
            doc_ram = '12g'
        elif hari == "3":
            # 24 user
            doc_cpu = 8
            doc_ram = '35g'
            print("rabu")
        elif hari == "4":
            # 16 user
            doc_cpu = 12
            doc_ram = '55g'
            print("kamis")
        elif hari == "5":
            # 8 user
            doc_cpu = 25
            doc_ram = '100g'
            print("jumat")
        elif hari == "10":
            #16 user Penelitian
            doc_cpu = 12
            doc_ram = "50g"
        elif hari == "11":
            #16 user Penelitian
            doc_cpu = 16
            doc_ram = "60g"
        
        folder_location = Config().master_userdir_path 
        user_container_volume = folder_location + "/" + container_name
        if os.path.isdir(folder_location) is False:
            os.mkdir(folder_location)
            os.mkdir(user_container_volume)
        else:
            os.mkdir(user_container_volume)
        
        # Generate Random String
        letters = string.ascii_lowercase
        random_letter =  ( ''.join(random.choice(letters) for i in range(10)) )

        # Generate Token
        hash_token = hashlib.sha1(random_letter.encode('utf-8')).hexdigest()
        token = str(hash_token)

        countainer_volume = [(user_container_volume, "/workspace/data", "rw"), (Config().master_datarepo_path, "/workspace/repo","ro")] 

        docker.container.run(image_name, detach=True, name=container_name, gpus=gpu, publish=port_publish, cpus=doc_cpu, memory=doc_ram, volumes=countainer_volume, envs={'JUPYTER_TOKEN': token})

        headers = {'Content-Type': 'application/json'}
        payload = {'id_container':container_name, 'id':data['id'], 'port': free_socket, 'token': token}
        
        url_update_data = Config().master_url + "/run"
        response = REST('POST', url_update_data, headers, json.dumps(payload)).send()

        print(response.json())
    
elif run_type == "":
    print("stop")