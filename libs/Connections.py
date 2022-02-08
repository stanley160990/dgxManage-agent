import docker
    
class Docker(object):
    def __init__(self, args1):
        self.args1 = args1
    
    def connect(self):
        sock_file = self.args1

        client = docker.DockerClient(base_url=sock_file)
        

        return client