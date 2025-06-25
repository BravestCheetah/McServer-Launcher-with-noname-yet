from mcserver.backend.server import Server

def create_server(name, motd, software, version) -> Server:
    server = Server(software=software, version=version, name=name, motd=motd)
    server.install_server()
    
    return server