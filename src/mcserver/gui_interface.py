from src.mcserver.backend.data import get_servers, get_server_disp
from nicegui import ui
from slugify import slugify

console_log_container = None
server_list_container = None


def add_log_message(text: str):
    

    if console_log_container:

        with console_log_container:

            from nicegui import ui
            ui.label(text)


        console_log_container.parent.scroll_to(console_log_container)

    else:
        
        print("[Console Not Ready] " + text)


def reload_servers(delete_server_popup, open_server):
    server_list_container.clear()
    servers = [get_server_disp(server) for server in get_servers()]

    for server in servers:
        with server_list_container:
            with ui.row().classes("w-full"):
                ui.label(server)
                ui.space()
                ui.button("Open", color="blue", on_click=lambda s=server: open_server(s))
                ui.button("Delete", color="red", on_click=lambda s=slugify(server): delete_server_popup(s))
