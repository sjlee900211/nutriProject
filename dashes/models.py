from django.db import models
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pymysql
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash


class Dash(models.Model):

    app = DjangoDash('dash')

    conn = pymysql.connect(db='project', user='****', passwd='****',
                        charset='utf8', port=3306, host='*************')

    # Parameter 받아와서 SELECT 쿼리에 넣어주기
    param1 = ''
    # 접속자가 누구인지 파라미터 받아오기
    user = ''

    df = pd.read_sql("SELECT FOOD_CODE, UPDATE_DT FROM food_bio WHERE 1=1 "+ param1, conn)


    # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    # app = dash.Dash(__name__, external_stylesheets=external_stylesheets, prevent_initial_callbacks=True, suppress_callback_exceptions=True)
    app.title = user+'히스토리 대시'

    df.info()
    trace = go.Bar(x=df.FOOD_CODE, y=df.UPDATE_DT, name='food_bio')

    app.layout = html.Div(children=[html.H1("History_대시보드", style={'textAlign': 'center'}),
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [trace],
                'layout':
                go.Layout(title='History_대시보드', barmode='stack')
            })
    ], className="container")
    
    # @app.callback(
    #     dash.dependencies.Output('output-color', 'children'),
    #     [dash.dependencies.Input('dropdown-color', 'value')])
    # def callback_color(dropdown_value):
    #     return "The selected color is %s." % dropdown_value

    # @app.callback(
    #     dash.dependencies.Output('output-size', 'children'),
    #     [dash.dependencies.Input('dropdown-color', 'value'),
    #     dash.dependencies.Input('dropdown-size', 'value')])
    # def callback_size(dropdown_color, dropdown_size):
    #     return "The chosen T-shirt is a %s %s one." %(dropdown_size,
    #                                                 dropdown_color)
        
    def as_dash_app(self):
        return self.app
        

    
    # def __str__(self):
    #     return self.app
        
    # if __name__ == '__main__':
    #     app.run_server(debug=True)
    
    