from shiny.express import expressify, input, render, ui, session
import duckdb
from shiny import render, reactive
from itables.shiny import DT
from itables import options, show, init_notebook_mode
import urllib.request
from pathlib import Path
from threading import Timer
from ratelimit import debounce, throttle


options.layout =  {
    "topStart": "pageLength",
    "topEnd": "search",
    "bottomStart": "info",
    "bottomEnd": "paging"
}  
options.maxBytes = 1024 * 1024
options.language = dict(info = "Mostrando _START_ a _END_ de _TOTAL_ registros.", search = "Pesquisar:")
options.classes = "display nowrap compact"
options.paging = True
options.searching = True
options.ordering = True
options.info = True
options.lengthChange = False
options.autoWidth = True
options.responsive = True
options.keys = True
options.buttons = []
options.style="width:100%;margin:auto",
_ = session.on_ended(lambda: "Session ended!")
init_notebook_mode()

app_dir = Path(__file__).parent
db_file = app_dir / "local.db"



if not Path.exists(db_file):
    con = duckdb.connect(str(db_file), read_only=False)
    con.install_extension('httpfs')
    con.load_extension('httpfs')
    print('Loading data...')
    con.sql(f"CREATE TABLE trips AS SELECT * from read_parquet('https://blobs.duckdb.org/data/yellow_tripdata_2010-01.parquet')")
    print('Data loaded')
    con.close()

con = duckdb.connect(str(db_file), read_only=True)

ui.input_text("qry", "SQL Query", "SELECT * from trips limit 10")


@render.express
def table():
    
    @debounce(1) # wait ... seconds before changing input.qry
    @reactive.Calc
    def d_qry(): return input.qry().replace('\n', ' ')   
    
    df = con.sql(f"{d_qry()}").df()
    ui.HTML(DT(df)) # the rendering of DT with buttons flickers with debounce


