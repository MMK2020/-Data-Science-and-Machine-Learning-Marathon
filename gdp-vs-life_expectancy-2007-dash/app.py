import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Create an object instance of class Dash
app = dash.Dash(__name__)

df = pd.read_csv("gdp-life-exp-2007.csv")

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent",
                 hover_name="country", log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id="life-exp-vs-gdp",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
