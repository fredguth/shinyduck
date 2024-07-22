from shiny import reactive
from shiny.express import ui, module
from shiny.ui import sidebar

@module
def table(input, output, session, title):    
    my_sidebar = sidebar("Sidebar content", open="closed", title=title, position="right")
    with ui.navset_card_underline(id="tbl_card", selected="Explorar", sidebar=my_sidebar, title=title):    
        
        with ui.nav_panel("Baixar"):
            "Panel A content"
        with ui.nav_panel("Explorar"):
            "Panel B content"
        ui.nav_spacer()
        ui.nav_spacer()
        with ui.nav_panel("Documentação"):
            "Panel C content"
        with ui.nav_panel("Linhagem"):
            "Panel C content"
        with ui.nav_panel("Qualidade"):
            "Panel C content"
        with ui.nav_panel("Ficha Técnica"):
            "Panel C content"
        ui.nav_spacer()
        ui.nav_spacer()
        ui.nav_spacer()
        ui.nav_spacer()
        ui.nav_spacer()
        ui.nav_spacer()
        ui.nav_spacer()