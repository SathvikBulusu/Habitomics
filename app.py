from dash import html, Dash , dash_table , dcc , Output , Input , callback, _dash_renderer  #dcc stands for dash core components 

import plotly.express as px
import pandas as pd 
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
_dash_renderer._set_react_version("18.2.0")

df = pd.read_csv('Preprocessed Dataset.csv')



app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dmc.MantineProvider([
    dmc.Title('A Detailed understanding of Habitomics',size="h2"),
    html.Hr(),
    dmc.RadioGroup(
    [dmc.Radio(i , value=i) for i in ['CPI','IntrestRates','Gdp','median_price','Household-income','usp','mort-rate','Annual_unemp']],
    id='my-dmc-radio-item',
    value='Gdp',
    size='sm'  
),

 dmc.Grid([
        dmc.GridCol([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], span=6),
        dmc.GridCol([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6),
    ]),

])

@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-dmc-radio-item', component_property='value')
)

def update_graph(col_chosen):
    fig = px.histogram(df, x='Year', y=col_chosen, histfunc='avg')
    return fig

if __name__=='__main__':
    app.run(debug=True)