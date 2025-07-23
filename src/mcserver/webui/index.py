from nicegui import ui
from slugify import slugify
import src.mcserver.gui_interface

from src.mcserver.backend.data import get_servers, get_server_disp, get_software_data
from src.mcserver.backend.downloader import get_downloader
from src.mcserver.backend.server_manager import delete_server, create_server


selected_server = None


def render(debug: bool = False):


    ui.query("body").style("font-size: 120%")
    

    with ui.tabs().classes("w-full") as top_tabs:

        home_top_tab = ui.tab("Home")
        server_top_tab = ui.tab("Server")
    

    with ui.tab_panels(top_tabs, value=home_top_tab).classes("w-full") as tab_panels:


        with ui.tab_panel(home_top_tab):
            ui.separator()


            def create_server_popup():

                software_select = None

                def software_update():
                    software = software_select.value
                    software_downloader = get_downloader(software)
                    software_versions = software_downloader.get_versions()
                    version_select.options = software_versions
                    version_select.value = software_versions[0]


                with ui.dialog() as dialog, ui.card():
                    ui.label("Create A New Server")

                    with ui.row().classes("w-full"):
                        ui.label("Server Name: ")
                        ui.space()
                        name_input = ui.input(value="My Awesome Server")
                    
                    with ui.row().classes("w-full"):
                        ui.label("MOTD (server description): ")
                        ui.space()
                        motd_input = ui.input(value="Server Created With StructureBlock")

                    with ui.row().classes("w-full items-center"):
                        ui.label("Software: ")
                        ui.space()
                        software_select = ui.select(list(get_software_data().keys()), value=list(get_software_data().keys())[0], on_change=software_update)

                    with ui.row().classes("w-full"):
                        ui.label("Version: ")
                        ui.space()
                        version_select = ui.select(list(get_software_data().keys()), value=list(get_software_data().keys())[0])
                    
                    def create_server_clicked():
                        dialog.close()
                        ui.notification("Creating Server...")
                        create_server(name_input.value, motd_input.value, software_select.value, version_select.value)
                        ui.notification("Server Successfully Created! Refreshing Server List...")
                        software_update()
                        ui.notification("Server List Successfully Refreshed!")

                    ui.button("Create", on_click=create_server_clicked)

                    software_update()

                dialog.open()


            with ui.row().classes("w-full"):

                ui.label("Servers")
                ui.space()
                ui.button("Create", color="green", on_click=create_server_popup)

            ui.separator()
            server_list_container = ui.column().classes("w-full")


            def reload_servers():
                server_list_container.clear()
                servers = [get_server_disp(server) for server in get_servers()]

                for server in servers:
                    with server_list_container:
                        with ui.row().classes("w-full"):

                            ui.label(server)
                            ui.space()
                            ui.button("Open", color="blue", on_click=lambda s=server: open_server(s))
                            ui.button("Delete", color="red", on_click=lambda s=slugify(server): delete_server_popup(s))


            server_name_label = None


            def open_server(name: str):
                global selected_server

                tab_panels.value = server_top_tab
                server_name_label.text = name
                selected_server = slugify(name)
            

            def delete_server_clicked(name: str):
                global selected_server

                if selected_server == name:
                    selected_server = None 
                
                ui.notification(message=f"Deleting {get_server_disp(name)}...")

                delete_server(name)

                ui.notification(message=f"Server Sucessfully Deleted! Reloading Server List...")

                reload_servers()

                ui.notification(message="Server list sucessfully reloaded!")
            

            def delete_server_popup(name: str):
                with ui.dialog() as dialog, ui.card():

                    ui.label(f"Are you sure you want to delete {name}? This will permanently delete the server and all its files (including the world!)")

                    with ui.row().classes("w-full"):

                        ui.button("Cancel", on_click=dialog.close)
                        ui.space()
                        ui.button("Delete", color="red", on_click=lambda s=name: delete_server_clicked(s))
                
                dialog.open()
            
            reload_servers()

        
        with ui.tab_panel(server_top_tab).classes('w-full'):


            ui.separator()


            with ui.row().classes('w-full'):

                server_name_label = ui.label("Server Name")
                ui.space()
                ui.button("Stop", color="red", on_click=lambda: ui.notify('No gui is implemented yet :(', close_button='OK'))
            

            ui.separator()


            with ui.tabs().classes("w-full") as server_tabs:

                console_server_tab = ui.tab("Console")
                settings_server_tab = ui.tab("Settings")
            

            with ui.tab_panels(server_tabs, value=console_server_tab).classes("w-full"):


                with ui.tab_panel(console_server_tab):
                    ui.separator()


                    with ui.scroll_area().classes('w-full h-800 border'):
                        src.mcserver.gui_interface.console_log_container = ui.column()


ui.run()