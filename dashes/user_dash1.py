import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pymysql
import plotly.graph_objs as go
from django.db import models

class Dash(models.Model):
	conn = pymysql.connect(db='project', user='admin', passwd='1234',
						charset='utf8', port=3306, host='13.114.158.172')

	# Parameter 받아와서 SELECT 쿼리에 넣어주기
	param1 = ''

	df = pd.read_sql("SELECT FOOD_CODE, UPDATE_DT FROM food_bio WHERE 1=1 "+ param1, conn)

	app_name = 'dash-mysqledataplot'

	external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

	app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
	app.title = 'CData + Dash'

	df.info()
	trace = go.Bar(x=df.FOOD_CODE, y=df.UPDATE_DT, name='food_bio')

	app.layout = html.Div(children=[html.H1("CData Extension + Dash", style={'textAlign': 'center'}),
		dcc.Graph(
			id='example-graph',
			figure={
				'data': [trace],
				'layout':
				go.Layout(title='MySQL Orders Data', barmode='stack')
			})
	], className="container")

	if __name__ == '__main__':
		app.run_server(debug=True)