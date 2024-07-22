import shinyswatch
import ipywidgets as widgets
from shiny import reactive
from shiny.express import input, render, ui, module, expressify
from shiny.ui import page_navbar, sidebar, Sidebar
from shinywidgets import render_widget
import shinywidgets

from functools import partial
from tbl import table
# from menu import menu_tabelas
ui.page_opts(fillable=True)


ui.tags.style(".bslib-sidebar-layout > .main { padding: 0px }")
tables = ["Entes", "Receitas", "Despesas"]

ui.page_opts(fillable=True)


@expressify
def menu_tabelas(selected=0):
    
    return [
        ui.input_action_button("btn_" + tbl, tbl, class_=f"{'btn btn-secondary' if i==selected else None} mb-2") for i, tbl in enumerate(tables)
    ]

    



with ui.sidebar(id="main_sidebar", gap=10, title="Base: SIOPS"):
    with ui.accordion():
        with ui.accordion_panel("Tabelas"):
            menu_tabelas(0)
        with ui.accordion_panel("Entradas"):
            "Entradas"
        with ui.accordion_panel("Saídas"):
            "Saídas"
        with ui.accordion_panel("Reúsos"):
            "Discussão"
        with ui.accordion_panel("Discussão"):
            "Discussão"
        
 

table(id="entes", title="Tabela: Entes")


