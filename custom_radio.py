from shiny.express import input, render, ui


with ui.div({"class": "btn-group-vertical", "role": "group"}):
    ui.input_radio_buttons( 
        "radio",  
        "Radio buttons",  
        {
        "1": ui.HTML(f'<label class="btn btn-outline-primary" for="btnradio1">Radio 1</label>'),
        "2": ui.HTML(f'<label class="btn btn-outline-primary" for="btnradio2">Radio 2</label>'), 
        "3": ui.HTML(f'<label class="btn btn-outline-primary" for="btnradio3">Radio 3</label>')},  
    )  


    # ui.tags.style(".form-check-input:checked[type="radio"], .shiny-input-container .checkbox input:checked[type="radio"], .shiny-input-container .checkbox-inline input:checked[type="radio"], .shiny-input-container .radio input:checked[type="radio"], .shiny-input-container .radio-inline input:checked[type="radio"] { btn-checked }")

