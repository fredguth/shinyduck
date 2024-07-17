from shiny.express import expressify, input, render, ui, session
import duckdb

from itables.shiny import DT
from itables import options, show, init_notebook_mode
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

# df = get_countries(html=False)



ui.input_text("qry", "SQL Query", "SELECT * FROM siops.receitas limit 100000")


@render.express
def table():
    df = con.sql(f"{input.qry().replace("\n", " ")}").df()
    ui.HTML(DT(df, buttons=["copyHtml5", "csvHtml5", "excelHtml5"]))















# from shinyswatch import theme
# import urllib.request
# from pathlib import Path

# import duckdb
# from query import query_output_server, query_output_ui
# # from shiny import App, reactive, ui
# from shiny.express import ui, render, input


# from itables.sample_dfs import get_countries
# from itables.shiny import DT
# from itables import options
# options.layout =  {
#     "topStart": "pageLength",
#     "topEnd": "search",
#     "bottomStart": "info",
#     "bottomEnd": "paging"
# }  # (default value)
# options.maxBytes = 1024 * 1024
# options.language = dict(info = "Mostrando _START_ a _END_ de _TOTAL_ registros.", search = "Pesquisar:")
# options.classes = "display nowrap compact"
# options.paging = True
# options.searching = True
# options.ordering = True
# options.info = True
# options.lengthChange = False
# options.autoWidth = True
# options.responsive = True
# options.keys = True
# options.buttons = []
# options.style="width:100%;margin:auto",


# app_dir = Path(__file__).parent
# db_file = app_dir / "db.db"
# con = duckdb.connect(str(db_file), read_only=True)
# df = con.sql("FROM siops.receitas limit 1000").df()


# ui.input_text_area("sql_query", "SQL Query", value="SELECT * FROM siops.receitas limit 1000")

# @render.ui
# def sql_result():
    
#     df = con.sql(f"{input.sql_query()}").df()
#     return ui.HTML(DT(df))


# # def load_csv(con, csv_name, table_name):
# #     csv_url = f"https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-12-20/{csv_name}.csv"
# #     local_file_path = app_dir / f"{csv_name}.csv"
# #     urllib.request.urlretrieve(csv_url, local_file_path)
# #     con.sql(
# #         f"CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{local_file_path}')"
# #     )


# # if not Path.exists(db_file):
# #     con = duckdb.connect(str(db_file), read_only=True)
# #     load_csv(con, "weather_forecasts", "weather")
# #     load_csv(con, "cities", "cities")
# #     con.close()


# app_ui = ui.page_sidebar(
#     ui.sidebar(
#         ui.input_action_button("add_query", "Add Query", class_="btn btn-primary"),
#         ui.input_action_button(
#             "show_meta", "Show Metadata", class_="btn btn-primary"
#         ),
#         ui.markdown(
#             """
#             This app lets you explore a dataset using SQL and duckdb.
#             The data is stored in an on-disk [duckdb](https://duckdb.org/) database,
#             which leads to extremely fast queries.
#             """
#         ),
#     ),
#     ui.HTML(DT(get_countries(html=False))),  
#     # ui.tags.div(
#     #     # query_output_ui("initial_query", remove_id="initial_query"),
#     #     ui.HTML(DT(get_countries(html=False))),
#     #     id="module_container",
#     # ),
#     title="DuckDB query explorer",
#     class_="bslib-page-dashboard",
#     theme=theme.sandstone, 
# )


# def server(input, output, session):
#     mod_counter = reactive.value(0)

#     query_output_server("initial_query", con=con, remove_id="initial_query")

#     @reactive.effect
#     @reactive.event(input.add_query)
#     def _():
#         counter = mod_counter.get() + 1
#         mod_counter.set(counter)
#         id = "query_" + str(counter)
#         ui.insert_ui(
#             selector="#module_container",
#             where="afterBegin",
#             ui=query_output_ui(id, remove_id=id),
#         )
#         query_output_server(id, con=con, remove_id=id)

#     @reactive.effect
#     @reactive.event(input.show_meta)
#     def _():
#         counter = mod_counter.get() + 1
#         mod_counter.set(counter)
#         id = "query_" + str(counter)
#         ui.insert_ui(
#             selector="#module_container",
#             where="afterBegin",
#             ui=query_output_ui(
#                 id, qry="SELECT * from information_schema.columns", remove_id=id
#             ),
#         )
#         query_output_server(id, con=con, remove_id=id)


# app = App(app_ui, server)
