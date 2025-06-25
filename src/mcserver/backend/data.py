from functools import cache
import yaml
from slugify import slugify

from mcserver.errors import ServerAlreadyExistsError, ServerDeleteNoConfirm
from mcserver.settings import SOFTWARE_DATA_FILE, SERVER_DATA_FILE


@cache
def get_software_data() -> dict:
    with open(SOFTWARE_DATA_FILE, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data["softwares"]


def get_software_names():
    return list(get_software_data().keys())


def get_software_metadata(software: str) -> dict:
    return get_software_data()[software]



def load_server_data() -> dict:

    with open(SERVER_DATA_FILE, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    
    if data == None:
        data = {
            "my-awesome-server": {
            "name": "My Awesome Server!",
            "motd": "This is my MOTD",
            "version": "1.19.2",
            "software": "vanilla", 
            }

        }

    return data


def save_server_data(data) -> dict:
    
    with open(SERVER_DATA_FILE, "w") as f:
        yaml.dump(data, f)



#   NOTICE TO DEVS: TO MAKE IT EASIER TO QUICKLY EDIT DIFFERENT THINGS ALL EDITS START WITH A COMPLETE LOAD AND END IN A COMPLETE SAVE.

def add_server(disp_name, motd, version, software) -> None:

    data = load_server_data()
    name = slugify(disp_name)

    if name in data:
        raise ServerAlreadyExistsError("There was an error adding a server to the server metadata: Server Already Exists")
        return
    
    data_name = name

    server_data = {
        "disp_name": disp_name,
        "motd": motd,
        "version": version,
        "software": software,
    }

    data[data_name] = server_data

    save_server_data(data)

def rm_server(name: str, confirm: bool = False) -> None:
    if confirm:
        data = load_server_data()
        data.pop(name)
        save_server_data(data)
        return
    
    raise ServerDeleteNoConfirm("Server Deletion Failed, Confirmation False")

def edit_server(name, key, value) -> None:

    data = load_server_data()

    data[name][key] = value

    save_server_data(data)

def get_servers() -> list:
    data = load_server_data()
    return list(data.keys())