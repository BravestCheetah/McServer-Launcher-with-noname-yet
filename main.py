from nicegui import ui

from mcserver.webui import home

TITLE = "MC Server"


def __get_servers() -> list[str]:
    """
    @TODO: this should be implemented to fetch a list of available servers from
    our backend, the list will be passed to the page renderer so we can create
    the menu entries and load the UI for each server.
    """
    return ["Server A", "Server B", "Server C"]


@ui.page("/")
def index():
    home.render(title=TITLE, servers=__get_servers())


ui.run(title=f"{TITLE}")
