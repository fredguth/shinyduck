from shinywidgets import output_widget, render_widget
import ipywidgets as widgets
from pathlib import Path
from shiny import ui, App

ui.include_css(
    Path(__file__).parent / "my-styles.css"
)

tags = [
    ui.input_action_button("btn", "Click me", class_="btn-outline-secondary"), 
    ui.input_action_button("btn2", "Click me", class_="btn-secondary"), 
    output_widget("toggleButtons")]

app_ui = ui.page_fillable(*tags)




def server(input, output, session):
    
    @render_widget
    def toggleButtons():
        return widgets.ToggleButtons(
        options=['Slow', 'Regular', 'Fast'],
        description='Speed:',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
        tooltips=['Description of slow', 'Description of regular', 'Description of fast'],
        layout=widgets.Layout(width='100px')    
    
    )


app = App(app_ui, server)



