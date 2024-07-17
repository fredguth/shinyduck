from shiny.express import expressify, input, render, ui, session
import duckdb

from itables.shiny import DT
from itables import options, show, init_notebook_mode
import urllib.request
from pathlib import Path
options.layout =  {
    "topStart": "pageLength",
    "topEnd": "search",
    "bottomStart": "info",
    "bottomEnd": "paging"
}  # (default value)
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
db_file = app_dir / "db.db"
con = duckdb.connect(str(db_file), read_only=True)

from itables.sample_dfs import get_countries




ui.input_text("qry", "SQL Query", "SELECT * FROM siops.receitas limit 1000000")


@render.express
def table():
    df = con.sql(f"{input.qry().replace("\n", " ")}").df()
    ui.HTML(DT(df, buttons=["copyHtml5", "csvHtml5", "excelHtml5"]))



