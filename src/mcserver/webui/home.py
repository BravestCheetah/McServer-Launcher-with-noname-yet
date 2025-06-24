from nicegui import ui


def render(title: str, servers: list[str]) -> None:
    """
    Render the home page with a left menu and a tab for each server.

    Args:
        servers: A list of server names to display in the menu.
    """
    # a barebones header that can be customized later with a logo and a title
    with ui.header():
        ui.label(title)

    # this is the dialog opened when the user clicks the "Add Server" button
    with ui.dialog() as new_server, ui.card():
        ui.label("Add Server")
        ui.button("Cancel", on_click=new_server.close)
        ui.button("Add", on_click=new_server.close)  # @TODO: implement adding server

    # render a left menu with references to all the servers passed as parameters,
    # possibly dynamically loading the server information and form from the backend
    with ui.left_drawer().classes("w-full h-56"):
        with ui.tabs().props("vertical").classes("w-full") as tabs:
            ui.tab("HOME")
            for server in servers:
                ui.tab(server)
        ui.button("Add Server", on_click=new_server.open, icon="add")

    # the content of all the tabs is currently loaded on application startup,
    # which is probably good enough since we don't expectet lots of servers on
    # the same machine
    with ui.tab_panels(tabs, value="Server A").classes("w-full"):
        with ui.tab_panel("HOME"):
            ui.label("HOME")
        for server in servers:
            with ui.tab_panel(server):
                ui.label(f"Content of {server}")
