import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pymysql
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from django.db import models

class Dash(models.Model):

    app = DjangoDash('dash')

    conn = pymysql.connect(db='project', user='admin', passwd='1234',
                        charset='utf8', port=3306, host='13.114.158.172')

    # Parameter 받아와서 SELECT 쿼리에 넣어주기
    param1 = ''
    # 접속자가 누구인지 파라미터 받아오기
    user = ''

    df = pd.read_sql("SELECT FOOD_CODE, UPDATE_DT FROM food_bio WHERE 1=1 "+ param1, conn)

    # app_name = 'dash-mysqledataplot'
    app_name = "dash" 

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.title = user+'히스토리 대시'

    df.info()
    trace = go.Bar(x=df.FOOD_CODE, y=df.UPDATE_DT, name='food_bio')

    app.layout = html.Div(children=[html.H1("CData Extension + Dash", style={'textAlign': 'center'}),
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [trace],
                'layout':
                go.Layout(title='History_대시보드', barmode='stack')
            })
    ], className="container")

    def __str__(self):
        return self.app_name
    
    # if __name__ == '__main__':
    #     app.run_server(debug=True)
    
    