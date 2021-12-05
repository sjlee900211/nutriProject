from django import db
from django.db import models
from dash.dependencies import Input, Output, MATCH, ALL, ALLSMALLER
import dash_core_components as dcc
import dash_html_components as html
from dash import callback_context
import pandas as pd
from pandas._config.config import option_context, options
import pymysql
import plotly.graph_objs as go
import plotly.express as px
from django_plotly_dash import DjangoDash
import numpy as np
import dash
from datetime import datetime, timedelta
import json

conn = pymysql.connect(db='project', user='admin', passwd='1234',
                        charset='utf8', port=3306, host='13.114.158.172')
class Dash(models.Model):
    
    param1 = '20211130'
    start = datetime.strptime(param1, "%Y%m%d")-timedelta(days=30)
    end = datetime.strptime(param1, "%Y%m%d")
    
    # print(start,end)
    # 접속자가 누구인지 파라미터 받아오기
    user = 1
    # Dropdown용 날짜용 쿼리
    app = DjangoDash('dash')
    app.layout = html.Div([
        #쿼리용 데이터 숨기기
        dcc.Input(
            id='sql-query',
            # value="SELECT count(mealtimes) AS cnt, created_at FROM user_upload_info WHERE user_id = {} AND DATE(created_at) BETWEEN {} AND {} GROUP BY created_at".format(user, start, end),
            value="SELECT count(mealtimes) AS cnt, created_at FROM user_upload_info WHERE user_id = {} GROUP BY created_at".format(user),
            style={'width': '100%',
                   'display': 'none'},
            type='text',
            
        ),
        html.Button('Run Query', 
                    id='run-query',
                     style={'display': 'none'}
                    ),

        html.Hr(),

        html.Div([
            html.Div(id='table-container', className="four columns"),

            html.Div([
                html.Div([
                    html.Div([
                        html.Label('Start date'),
                        dcc.Dropdown(
                            id='dropdown-x',
                            clearable=False,
                            # multi = True,
                            value="SELECT created_at FROM user_upload_info WHERE user_id = {} GROUP BY created_at".format(user)
                        )
                    ], className="six columns"),
                    html.Div([
                        html.Label('End date'),
                        dcc.Dropdown(
                            id='dropdown-y',
                            clearable=False,
                        )
                    ], className="six columns")
                ], className="row"),
                html.Div(dcc.Graph(id='graph'), style={"width":"100%"}, className="ten columns")
            ], className="eight columns")
        ], className="row"),

        # hidden store element
        html.Div(id='table-store', style={'display': 'none'})
    ])


    @app.callback(
        dash.dependencies.Output('table-store', 'children'),
        [dash.dependencies.Input('run-query', 'n_clicks')],
        state=[dash.dependencies.State('sql-query', 'value')])
    
    def sql(number_of_times_button_has_been_clicked, sql_query):
        dff = pd.read_sql_query(
            sql_query,
            conn
        )
        return dff.to_json()
    
    # def x():
    
        # def create_options_x(selected_startdate):
    #     dff = pd.read_json(selected_startdate)
    #     date_x = pd.DatetimeIndex(dff['created_at']).strftime("%Y%m%d")
    #     fig = px.line(dff, x=dff['dropdown-x'], y=dff['dropdown-y'])
    #     return [{'label': i, 'value': i} for i in date_x]
    
    # @app.callback(
    #     dash.dependencies.Output('graph', 'figure'),
    #     [dash.dependencies.Input('table-store', 'children'),
    #     dash.dependencies.Input('dropdown-x', 'value'),
    #     dash.dependencies.Input('dropdown-y', 'value')])
    @app.callback(
        dash.dependencies.Output('graph', 'figure'),
        [dash.dependencies.Input('table-store', 'children')])    
    # def dff_to_table(dff_json, dropdown_x1, dropdown_x2):
    def dff_to_table(dff_json, dropdown_x1):
    # def dff_to_table(dff_json):
        dff = pd.read_json(dff_json)
        # x = pd.DatetimeIndex(dff['created_at']).strftime("%Y/%m/%d %H:%M")
        # x = pd.DatetimeIndex(dff['created_at']).strftime("%Y%m%d")
        y = dff['cnt']       
        return {
            'data': [{
                'x': dff[dropdown_x1],
                'y': y,
                # 'x': x,
                # 'y': y,
                'type': 'line'
            }],

        }

    # 날짜 선택-----------------------------------------------
    # @app.callback(
    #     dash.dependencies.Output('dropdown-x', 'options'),
    #     [dash.dependencies.Input('table-store', 'children')])
    # def create_options_x(selected_startdate):
    #     dff = pd.read_json(selected_startdate)
    #     date_x = pd.DatetimeIndex(dff['created_at']).strftime("%Y/%m/%d")
    #     return [{'label': i, 'value': i} for i in date_x]        
    @app.callback(
        dash.dependencies.Output('dropdown-x', 'options'),
        [dash.dependencies.Input('table-store', 'children')])
    def create_options_x(dff_json):
        dff = pd.read_json(dff_json)
        date_x = pd.DatetimeIndex(dff['created_at']).strftime("%Y%m%d")
        # seleted_x = (date_x['created_at']> dff_json) & (date_x['created_at']<= dff_json)
        return [{'label': i, 'value': i} for i in date_x]


    # @app.callback(
    #     dash.dependencies.Output('dropdown-y', 'options'),
    #     [dash.dependencies.Input('table-store', 'children')])
    # def create_options_y(dff_json):
    #     dff = pd.read_json(dff_json)
    #     date_y = pd.DatetimeIndex(dff['created_at']).strftime("%Y%m%d")
    #     return [{'label': i, 'value': i} for i in date_y]

    # @app.callback(
    #     dash.dependencies.Output('graph', 'figure'),
    #     [dash.dependencies.Input('table-store', 'children'),
    #     dash.dependencies.Input('dropdown-x', 'value'),
    #     dash.dependencies.Input('dropdown-y', 'value')])
   
    # def update_chart(selected_startdate, selected_enddate):
    #     ctx = dash.callback_context

    #     if not ctx.triggered:
    #         button_id = 'No clicks yet'
    #     else:
    #         button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    #     ctx_msg = json.dumps({
    #         'states': ctx.states,
    #         'triggered': ctx.triggered,
    #         'inputs': ctx.inputs
    #     }, indent=2)

    #     return html.Div([
    #         html.Table([
    #             html.Tr([html.Th('Button 1'),
    #                     html.Th('Button 2'),
    #                     html.Th('Most Recent Click')]),
    #             html.Tr([html.Td(selected_startdate or 0),
    #                     html.Td(selected_enddate or 0),
    #                     html.Td(button_id)])
    #         ]),
    #         html.Pre(ctx_msg)
    #     ])    
        # triggered_id = callback_context.triggered[0]['prop_id']
                    
        # dff = pd.read_json(selected_startdate, selected_enddate)   
        # return {
        #     'data': [{
        #         'x': dff[selected_startdate],
        #         'y': dff[selected_enddate],
        #         'type': 'line'
        #     }],

        # }

    app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
    
    def as_dash_app(self):
        return self.app    