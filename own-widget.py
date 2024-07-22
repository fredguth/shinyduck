from typing import List, Optional
from shiny import App, Inputs, Outputs, Session, reactive, render, ui, module
import shinyswatch

# ============================================================
# toggleButtons module
# ============================================================

@module.ui
def toggleButtons_ui() -> ui.TagChild:
    return ui.panel_absolute(
        ui.panel_well(
            ui.output_ui("menu"),
        ),
        draggable=False,
        width="100%",
        height="100%",
        top="0%",
        left="0%"
    )
    

@module.server
def toggleButtons_server(input: Inputs, output: Outputs, session: Session, choices: List[str], selected:Optional[str]=None):
    selected = selected or reactive.value(choices[0])
    @render.ui
    def menu():
        buttons = []
        for choice in choices:
            klass = "btn-primary" if selected() == choice else "btn-scondary"
            buttons.append(ui.input_action_button(f"menubtn_{choices.index(choice)}", f"{choice}", class_=klass))
        return ui.div(*buttons, class_="d-grid gap-2")

    
    def create_choice_listener(choice, index):
        @reactive.effect
        @reactive.event(getattr(input, f"menubtn_{index}"))
        def listener(): selected.set(choice)
        return listener
    
    for choice in choices:
        create_choice_listener(choice, choices.index(choice))



@module.ui
def tableShell_ui() -> ui.TagChild:
    return ui.output_ui("tableShell")

@module.server
def tableShell_server(input, output, session, title:str=""):
    @render.ui
    def tableShell():
        panels = ["Baixar", "Explorar", None, None, "Documentação", "Linhagem", "Qualidade", "Ficha Técnica", None, None, None, None, None]
        children = [ui.nav_panel(c, f"Panel {c} content") if c else ui.nav_spacer() for c in panels]
        sb = ui.sidebar("tbl_sb", open="closed", title=title, position="right")
        return ui.navset_card_underline(id="tbl_card", selected="Explorar", sidebar=sb, title=title, *children)




# =============================================================================
# App that uses module
# =============================================================================
app_ui = ui.page_fluid(
    tableShell_ui(id="shell"),
    # toggleButtons_ui("menu1"),
    # ui.output_ui("shell"),
    
    # theme=shinyswatch.theme.sandstone
)


def server(input, output, session):
    tableShell_server(id="shell", title="Entes")
    # choices = ["Entes", "Receitas", "Despesas"]
    # selected = reactive.value(choices[0])

    # @render.ui
    # def shell():    
    #     tableShell_ui(id="shell", title="Entes"),
    #     ui.br()
        
        
    
    # toggleButtons_server("menu1", choices, selected)
    
    


app = App(app_ui, server)





# # ============================================================
# # Counter module
# # ============================================================
# @module.ui
# def counter_ui(label: str = "Increment counter") -> ui.TagChild:
#     return ui.card(
#         ui.h2("This is " + label),
#         ui.input_action_button(id="button", label=label),
#         ui.output_code(id="out"),
#     )


# @module.server
# def counter_server(input, output, session, starting_value: int = 0):
#     count: reactive.value[int] = reactive.value(starting_value)

#     @reactive.effect
#     @reactive.event(input.button)
#     def _():
#         count.set(count() + 1)

#     @render.code
#     def out() -> str:
#         return f"Click count is {count()}"


# # =============================================================================
# # App that uses module
# # =============================================================================
# app_ui = ui.page_fluid(
#     counter_ui("counter1", "Counter 1"),
#     counter_ui("counter2", "Counter 2"),
# )


# def server(input, output, session):
#     counter_server("counter1")
#     counter_server("counter2")


# app = App(app_ui, server)






