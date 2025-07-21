from functools import cache
import yaml
from slugify import slugify
import pathlib
from shutil import rmtree

from mcserver.errors import ServerAlreadyExistsError, ServerDeleteNoConfirm, ServerDoesNotExistError
from mcserver.settings import SOFTWARE_DATA_FILE, SERVER_DATA


@cache
def get_software_data() -> dict:
    with open(SOFTWARE_DATA_FILE, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data["softwares"]


def get_software_names():
    return list(get_software_data().keys())


def get_software_metadata(software: str) -> dict:
    return get_software_data()[software]



def load_server_data(server) -> dict:

    data_path = SERVER_DATA / server / ".StructureBlock" / "data.yaml"

    with open(data_path, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    return data


def save_server_data(server, data) -> dict:
    
    data_path = SERVER_DATA / server / ".StructureBlock" / "data.yaml"

    with open(data_path, "w") as f:
        yaml.dump(data, f)



#   NOTICE TO DEVS: TO MAKE IT EASIER TO QUICKLY EDIT DIFFERENT THINGS ALL EDITS START WITH A COMPLETE LOAD AND END IN A COMPLETE SAVE.

def add_server(disp_name, motd, version, software) -> None:

    name = slugify(disp_name)

    if pathlib.Path.exists(SERVER_DATA / name / ".StructureBlock"):
        raise ServerAlreadyExistsError("There was an error adding a server to the server metadata: Server Already Exists")
        return
    
    pathlib.Path.mkdir(SERVER_DATA / name / ".StructureBlock")

    server_data = {
        "disp_name": disp_name,
        "motd": motd,
        "version": version,
        "software": software,
    }

    save_server_data(name, server_data)

def rm_server(name: str, confirm: bool = False) -> None:
    if confirm:
        if pathlib.Path.exists(SERVER_DATA / name):

            rmtree(SERVER_DATA / name)
            return
        
        raise ServerDoesNotExistError("Server Deletion Failed, Server Not Found")
    
    raise ServerDeleteNoConfirm("Server Deletion Failed, Confirmation False")

def edit_server(name, key, value) -> None:

    data = load_server_data(name)

    data[key] = value

    save_server_data(name, data)
    
def get_servers() -> list:

    servers = [f.name for f in SERVER_DATA.iterdir() if f.is_dir()]
    return servers