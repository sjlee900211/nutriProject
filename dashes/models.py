from django import db
from django.db import models
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from pandas._config.config import options
import pymysql
import plotly.graph_objs as go
import plotly.express as px
from django_plotly_dash import DjangoDash
import numpy as np

class Dash(models.Model):

    app = DjangoDash('dash')
    
    conn = pymysql.connect(db='project', user='admin', passwd='1234',
                        charset='utf8', port=3306, host='13.114.158.172')
    # Parameter 받아와서 SELECT 쿼리에 넣어주기
    param1 = ''
    # 접속자가 누구인지 파라미터 받아오기
    user = ''
    df = pd.read_sql("SELECT FOOD_CODE, UPDATE_DT FROM food_bio WHERE 1=1 "+ param1, conn)
    date = pd.read_sql_query("SELECT FOOD_CODE, UPDATE_DT FROM food_bio WHERE 1=1 "+ param1, conn)
    app.title = user+'히스토리 대시'

    df_date = date[['UPDATE_DT']]
    # print(df_date.head(5))
    trace = go.Bar(x=df.FOOD_CODE, y=df.UPDATE_DT, name='food_bio')
    
    app.layout = html.Div(children=[html.H1("History_대시보드", style={'textAlign': 'center'}),
        html.Div([
            # html.Label("Date"),
            # 시작년월 선택
            html.Div(
                dcc.Dropdown( 
                    id="date1",  
                    placeholder="Select Start date",
                    options=[{'label': i, 'value':i} for i in df_date.values],
                    value = 'UPDATE_DT',
                    # multi=True
                ), 
                style={'width':'50%',  'text-align':'center'},
                
                ),
                

            # 종료년월 선택
            html.Div(
                dcc.Dropdown( 
                    id="date2",
                    placeholder="Select End date",
                    options=[{'label': i, 'value':i} for i in df_date.values],
                ),
                style={'width':'50%',  'text-align':'center'}),
                # # dropdown_select 표시(date1)
                # dcc.Dropdown(id = 'date1_state', options=[], multi=True),
        ], style={"width":"80%", "display":"inline-flex"}),  
        # 로딩 표시------------------
        html.Div(
            dcc.Loading(
                id="loading",
                children=[html.Div(id="loading-output")],#, style={'color':'#aaa', 'display':'flex', 'flex-direction':'row-reverse', 'vertical-align': 'top'})],
                type="circle")),

        html.Br(),                            
        dcc.Graph(
            id='line',
            figure={
                'data': [trace],
                'layout':
                go.Layout(title='', barmode='stack')
            })
    ], className="container")

     # 날짜 선택--------------------------------------------------------------
    @app.callback(
        Output('date1_state', 'options'), Input('date1', 'value'))
    
    def draw_chart(date1):
        conn = pymysql.connect(db='project', user='admin', passwd='1234',
                        charset='utf8', port=3306, host='13.114.158.172')
        df = pd.DataFrame()
        # 선택한 회사의 데이터를 dataframe으로 생성
        pd.read_sql('SELECT FOOD_CODE, UPDATE_DT FROM food_bio WHERE UPDATE_DT = "{}" '.format(date1,conn))
        # 그래프 그리기
        fig = px.line(x=df.FOOD_CODE, y=df.UPDATE_DT, name='food_bio') 
        fig.update_layout(
            title = '',
            yaxis={'tickformat':',d'}
        )
        return fig   
    def as_dash_app(self):
        return self.app

    