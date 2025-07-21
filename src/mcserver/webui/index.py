from nicegui import ui


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

                server_name_label = ui.label("Server Name").style("font-size: 120%")
                ui.space()
                ui.button("Stop", color="red", on_click=lambda: ui.notify('No gui is implemented yet :(', close_button='OK'))


    ui.run()
