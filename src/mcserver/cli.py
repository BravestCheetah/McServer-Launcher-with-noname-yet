import click

from mcserver.backend.server import Server


@click.command()
@click.option("--name", type=str, help="The name of the server")
@click.option("--software", type=str, help="The software to use")
@click.option("--version", type=str, help="The version to use")
def main(name: str, software: str, version: str):
    server = Server(name=name, software=software, version=version)
    server.install_server()
    server.start_server()
