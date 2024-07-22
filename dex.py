import shinyswatch

from shiny import reactive
from shiny.express import input, render, ui, module
from shiny.ui import page_navbar, sidebar, Sidebar
from shinywidgets import render_widget
from functools import partial

ui.page_opts(fillable=True)

# @module
# def table(input, output, session, title):
#     ui.page_opts(
#         title=title,
#         page_fn=partial(page_navbar, id="page"),
#     )


#     with ui.nav_panel("Visualizar"):
#         "Page C content"

#     with ui.nav_panel("Baixar"):
#         with ui.navset_card_tab(id="tab", title="Title", sidebar=):
#             with ui.nav_panel("A"):
#                 "Panel A content"

#             with ui.nav_panel("B"):
#                 "Panel B content"

#             with ui.nav_panel("C"):
#                 "Panel C content"


#     with ui.nav_panel("Documentação"):
#         "Page A content"

#     with ui.nav_panel("Qualidade"):
#         "Page B content"

#     with ui.nav_panel("Ficha Técnica"):
#         "Page B content"


ui.tags.style(".bslib-sidebar-layout > .main { padding: 0px }")
tables = ["Entes", "Receitas", "Despesas"]
# ui.page_opts(theme=shinyswatch.theme.sandstone)
ui.page_opts(fillable=True)


def menu():
    return [ui.p("Tabelas", style="control-label pb-0")] + [
        ui.input_action_button("btn_" + tbl, tbl) for tbl in tables
    ]


with ui.sidebar(id="main_sidebar", gap=.5):
    menu()

    ui.input_selectize("loc1", "Location 1", choices=tables, selected="Entes")
    ui.input_selectize("loc2", "Location 2", choices=tables, selected="Receitas")
    ui.input_selectize("loc3", "Location 3", choices=tables, selected="Despesas")

children = [menu()]
my_sidebar = sidebar("Sidebar content", open="closed", title="Sidebar title", position="right")


with ui.navset_card_underline(id="tbl_menu", selected="B", title="Entes", sidebar=my_sidebar):

    with ui.nav_panel("A"):
        "Panel A content"
    with ui.nav_panel("B"):
        "Panel B content"

    with ui.nav_panel("C"):
        "Panel C content"
    ui.nav_spacer()
    ui.nav_spacer()


# "Table"
# table(id="entes", title="Entes")
