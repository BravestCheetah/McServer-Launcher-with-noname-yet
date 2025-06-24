from nicegui import ui

from .debug import render as render_debug
from .home import render as render_home


def render(
    title: str,
    page: str,
    servers: list[str],
    debug: bool = False,
) -> None:
    """
    Render the home page with a left menu and a tab for each server.

    Args:
        page: the slugified string name of the page to render on load
        servers: A list of server names to display in the menu.
    """

    def on_tab_change(e):
        ui.navigate.history.push(f"/{e.args}")

    def _add_server_dialog() -> ui.dialog:
        with ui.dialog() as add_server_dialog, ui.card():
            ui.label("Add Server")
            ui.button(
                "Cancel",
                on_click=add_server_dialog.close,
            )
            ui.button(
                "Add", on_click=add_server_dialog.close
            )  # @TODO: implement adding server

        return add_server_dialog

    with ui.header():
        ui.label(title)

    add_server_dialog = _add_server_dialog()

    with ui.left_drawer().classes("w-full h-56"):
        with ui.tabs().props("vertical") as tabs:
            ui.tab("home")
            if debug:
                ui.tab("debug")
            for server in servers:
                ui.tab(server)
        ui.button("Add Server", on_click=add_server_dialog.open, icon="add")

    tabs.on("update:model-value", on_tab_change)

    with ui.tab_panels(tabs, value=page).classes("w-full"):
        with ui.tab_panel("home"):
            render_home()
        with ui.tab_panel("debug"):
            render_debug()
        for server in servers:
            with ui.tab_panel(server):
                ui.label(f"Content of {server}")
