from mcserver.backend.server import Server
from mcserver.errors import ServerAlreadyExistsError, ServerDoesNotExistError
from mcserver.backend.data import get_servers, load_server_data, rm_server

def create_server(name, motd, software, version) -> Server:
    if name in get_servers():
        raise ServerAlreadyExistsError
        return

    server = Server(software, version, name, motd)
    server.install_server()
    
    return server

def load_server(name) -> Server:
    if name in get_servers():
        server_data = load_server_data()[name]
        server = Server(server_data["software"], server_data["version"], server_data["disp_name"], server_data["motd"])
        return server

    raise ServerDoesNotExistError(f"Server '{name}' tried to load but was not found.")

def delete_server(name) -> None:

    server = load_server(name)
    rm_server(server, confirm=True)
    server.uninstall_server()
    
