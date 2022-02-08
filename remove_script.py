import sys
import json

from libs.Config import Config
from libs.Connections import Psql, Docker
from libs.REST import REST

hari = sys.argv[2]
docker_con = Docker(Config().master_docker_sock).connect()

url_run_data = Config().master_url + "/run/" + hari + "/" + Config().agent_id_mensin
run_data = REST("GET", url_run_data, {}, {}).send()


for data in run_data.json()['data']:
    docker_con.containers.stop(data['id_container'])
    if data['durasi'] == data['durasi_aktual']:
        docker_con.containers.remove(data['id_container'])
        image_name = data['username'] + ":" + str(data['tag'])
        docker_con.images.remove(image_name)
    
    headers = {'Content-Type': 'application/json'}
    payload = {'id':data['id'], 'id_schedule':data['id_schedule']}
    
    url_update_data = Config().master_url + "/stop"
    response = REST('POST', url_update_data, headers, json.dumps(payload)).send()

    print(response.json())

