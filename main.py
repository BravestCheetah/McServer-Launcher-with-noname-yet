import argparse

from nicegui import ui

from mcserver.webui import index

TITLE = "MC Server"

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true")
debug = parser.parse_args().debug


def __get_servers() -> list[str]:
    """
    @TODO: this should be implemented to fetch a list of available servers from
    our backend, the list will be passed to the page renderer so we can create
    the menu entries and load the UI for each server.
    """
    return ["server-a", "server-b", "server-c"]


@ui.page("/")
@ui.page("/{page}")
def page(page: str = "home"):
    index.render(title=TITLE, page=page, servers=__get_servers(), debug=debug)


def main():
    ui.run(title=f"{TITLE}")


if __name__ in {"__main__", "__mp_main__"}:
    main()
