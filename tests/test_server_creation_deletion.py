from src.mcserver.backend.server_manager import create_server, delete_server
from src.mcserver.settings import *
from src.mcserver.backend.data import get_servers, load_server_data
from shutil import rmtree

print(get_servers())

try:
    rmtree(SERVER_DATA / "server")
except Exception:
    pass

server = create_server("server", "", "paper", "1.20.1")
print("Successfully created server, server data:")
print(load_server_data("server"))
delete_server("server")
print("sucessfully deleted server")