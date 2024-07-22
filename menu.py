from shiny import reactive
from shiny.express import render, ui, module



tables = ["Entes", "Receitas", "Despesas"]


@module
def menu_tabelas(selected=0):
    return [ui.p("Tabelas", style="control-label pb-0")] + [
        ui.input_action_button("btn_" + tbl, tbl) for tbl in tables
    ]




    
    
    # p = ui.p("Tabelas", style="control-label pb-0")
    # btns = [
    #     ui.input_action_button("btn_" + tbl, tbl, _class=f"{"btn btn-success" if i==selected}") for i, tbl in enumerate(tables)
    # ]
    # return [p]
# from shiny import App, Inputs, Outputs, Session, reactive, req, ui

# app_ui = ui.page_fluid(
#     ui.input_action_button("update", "Update other buttons and link"),
#     ui.br(),
#     ui.input_action_button("goButton", "Go"),
#     ui.br(),
#     ui.input_action_button("goButton2", "Go 2", icon="🤩"),
#     ui.br(),
#     ui.input_action_button("goButton3", "Go 3"),
#     ui.br(),
#     ui.input_action_link("goLink", "Go Link"),
# )


# def server(input: Inputs, output: Outputs, session: Session):
#     @reactive.effect
#     def _():
#         req(input.update())
#         # Updates goButton's label and icon
#         ui.update_action_button("goButton", label="New label", icon="📅")
#         # Leaves goButton2's label unchanged and removes its icon
#         ui.update_action_button("goButton2", icon=[])
#         # Leaves goButton3's icon, if it exists, unchanged and changes its label
#         ui.update_action_button("goButton3", label="New label 3")
#         # Updates goLink's label and icon
#         ui.update_action_link("goLink", label="New link label", icon="🔗")