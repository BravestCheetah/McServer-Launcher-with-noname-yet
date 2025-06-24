from mcserver.backend.server.server_data import data
import requests as req
import platform
import re
import pathlib
import subprocess
import signal
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

        self.download_jar()

        eula_path = target = pathlib.Path.joinpath(self.path, self.path_name, "eula.txt")
        with open(eula_path, "w") as f:
            f.write("eula=true")

    def start_server(self):
        cwd = pathlib.Path.joinpath(self.path, self.path_name)

        self.process = subprocess.Popen(
            ["java", "-jar", "server.jar"],
            cwd=cwd
        )



    def kill_server(self):
        
        if platform.system() == "Windows":
            self.process.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            self.process.send_signal(signal.SIGINT)

        self.process.wait()



    def restart_server(self):
        self.kill_server()

        self.start_server()

