from nicegui import ui
import src.mcserver.gui_interface

def render(debug: bool = False):


    ui.query("body").style("font-size: 120%")
    

    with ui.tabs().classes("w-full") as top_tabs:

        home_top_tab = ui.tab("Home")
        server_top_tab = ui.tab("Server")
    

    with ui.tab_panels(top_tabs, value=server_top_tab).classes("w-full"):


        with ui.tab_panel(home_top_tab):
            ui.separator()

            ui.label("home tab")

        
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