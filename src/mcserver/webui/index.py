from nicegui import ui


def render(debug: bool = False):
    
    with ui.tabs().classes("w-full") as top_tabs:

        home_top_tab = ui.tab("Home")
        server_top_tab = ui.tab("Server")

    
    with ui.tab_panels(top_tabs, value=server_top_tab).classes("w-full"):

        with ui.tab_panel(home_top_tab):
            ui.separator()

            ui.label("home tab")

        
        with ui.tab_panel(server_top_tab):
            ui.separator()


            with ui.row().classes('w-half items-center justify-center'):

                ui.label("Server Name")
                ui.space()
                ui.button("Stop", color="red")



    ui.run()