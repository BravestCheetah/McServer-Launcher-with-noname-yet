from mcserver.backend.server.server_data import data
import requests as req
import re
import pathlib

class server():
    def __init__(self, path, metadata: list = ["My Awesome Server!", "This MOTD is awesome!"], serverdata: list = ["vanilla", "1.21.6"]) -> None:
        
        self.meta = metadata
        self.servermeta = serverdata

        self.path = path

        self.path_name = metadata[0]
        self.path_name = self.path_name.strip().lower()
        self.path_name = re.sub(r'[<>:"/\\|?*\s]+', "_", self.path_name).strip("_")

        self.server_data = data()

    def download_jar(self):

        download_url = self.server_data.get_jar_download(self.servermeta[0], self.servermeta[1])
        data = req.get(download_url).content

        target = pathlib.Path.joinpath(self.path, self.path_name, "server.jar")

        pathlib.Path.mkdir(pathlib.Path.joinpath(self.path, self.path_name))
        with open(target, "wb") as f:
            f.write(data)
        
        

    def install_server(self):
        pass

    def start_server(self):
        pass

    def kill_server(self):
        pass

    def restart_server(self):
        pass

