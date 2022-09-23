import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go


def render_tab(df):

    layout = html.Div([html.H1('Kanały sprzedaży',style={'text-align':'center'}),
                        html.Div([html.Div([dcc.Dropdown(id='store2_dropdown',
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='barh-store2-subcat')],style={'width':'50%'}),
                        html.Div([dcc.Dropdown(id='store_dropdown',
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='barh-store-subcat')],style={'width':'50%'})],
                        style={'display':'flex'}), html.Div(id='temp-out')
                        ])

    return layout