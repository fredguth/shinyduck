from typing import List, Optional
from shiny import App, Inputs, Outputs, Session, reactive, render, ui, module
import shinyswatch

# ============================================================
# toggleButtons module
# ============================================================

@module.ui
def toggleButtons_ui() -> ui.TagChild:
    return ui.output_ui("menu")
    

@module.server
def toggleButtons_server(input: Inputs, output: Outputs, session: Session, choices: List[str], selected:Optional[str]=None):
    selected = selected or reactive.value(choices[0])
    @render.ui
    def menu():
        buttons = []
        for choice in choices:
            klass = "btn-secondary" if selected() == choice else "btn-outline-secondary"
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
        t = f"Tabela: {title}"
        panels = ["Baixar", "Explorar", None, None, "Documentação", "Linhagem", "Qualidade", "Ficha Técnica", None, None, None, None, None]
        children = [ui.nav_panel(c, f"Panel {c} content") if c else ui.nav_spacer() for c in panels]
        sb = ui.sidebar("tbl_sb", open="closed", title=t, position="right")
        return ui.navset_card_underline(id="tbl_card", selected="Explorar", sidebar=sb, title=t, *children)




# =============================================================================
# App that uses module
# =============================================================================


panels = [ui.accordion_panel(p, p) for p in ["Entradas", "Saídas", "Reúsos", "Discussão"]]
tbl_panel = ui.accordion_panel("Tabelas", toggleButtons_ui("main_sidebar"))
accordion = ui.accordion(tbl_panel, *panels)

app_ui = ui.page_sidebar(        
    ui.sidebar(toggleButtons_ui("menu1"), id="main_sb", open="open", title="Base: SIOPS", position="left"),
    tableShell_ui(id="shell"),
    # ui.tags.style(".bslib-sidebar-layout > .main { padding: 10px; padding-top: 0px;}"),
)


def server(input, output, session):
    
    choices = ["Entes", "Receitas", "Despesas"]
    selected = reactive.value(choices[0])
    toggleButtons_server("menu1", choices, selected)
    tableShell_server(id="shell", title="Entes")

    
    
    
    


app = App(app_ui, server)

