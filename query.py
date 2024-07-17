# import duckdb
# from shiny import module, reactive, render, ui
# from itables.shiny import DT
# from itables import init_notebook_mode
# from shinyswatch import theme
# theme.sandstone()

# init_notebook_mode(all_interactive=True)

# @module.ui
# def query_output_ui(remove_id, qry="FROM siops.receitas limit 1000"):
#     return (
#         ui.card(
#             {"id": remove_id},
#             ui.card_header(f"{remove_id}"),
#             ui.layout_columns(
                
#                     ui.input_text_area(
#                         "sql_query",
#                         "",
#                         value=qry,
#                         width="100%",
#                         height="120px",
#                     ),
                    
                
#                 [
#                         ui.input_action_button("run", "Run", class_="btn btn-primary"),
#                         ui.input_action_button(
#                             "rmv", "Remove", class_="btn btn-secondary"
#                         ),
#                     ],
                
#                 col_widths={"xl": [9, 3], "lg": [8, 3], "md": [6, 3], "sm": [12, 3]},
#             ),
#             ui.output_data_frame("results"),
#         ),
#     )


# @module.server
# def query_output_server(
#     input, output, session, con: duckdb.DuckDBPyConnection, remove_id
# ):
#     # @render.data_frame
#     @reactive.event(input.run)
#     def results():
#         qry = input.sql_query().replace("\n", " ")
#         # return render.DataTable(con.query(qry).to_df(), height='800px')
#         return ui.HTML(DT(con.query(qry).to_df()))

#     @reactive.effect
#     @reactive.event(input.rmv)
#     def _():
#         ui.remove_ui(selector=f"div#{remove_id}")
