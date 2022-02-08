import yaml


class Config(object):
    def __init__(self):
        with open('etc/config.yml') as yamlfile:
            cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)

        self.master_location = cfg["master"]["location"]
        self.master_docker_sock = cfg["master"]["docker_sock"]
        self.master_url = cfg["master"]["master_url"]
        self.master_datarepo_path = cfg["master"]["datarepo_path"]
        self.agent_id_mensin = cfg["agent"]["id_mesin"]
