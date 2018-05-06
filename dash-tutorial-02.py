import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime
import pandas as pd
from datetime import datetime

df = pd.read_csv('sementara-100.log',sep='\s+',header=None)
df[6] = df[1]+' '+df[2]
waktu2time = lambda z: datetime.strptime(z,'%Y-%m-%d %H:%M:%S')
df[7] = df[6].apply(waktu2time)
weather = df.loc[:,[7,3,4,5]]
df = pd.DataFrame(weather)
df.rename(columns={7:'Datetime', 3:'ID', 4:'Temp', 5:'Humidity'},inplace=True)
df.set_index('Datetime',inplace=True)

app = dash.Dash()

app.layout = html.Div(children = [
    html.H1(children = 'Hello Dash'),

    html.Div(children = 'Dash : A web application framework for Python'),

    dcc.Graph(
        id = 'example-graph',
        figure = {
            'data' : [
                {'x' : df.index, 'y' : df.Temp,'type' : 'line', 'name' : 'Temp'}
                # {'x' : df.index, 'y' : df.Humidity,'type' : 'line', 'name' : 'Humidity'}
            ],
            'layout' : {
                'title' : 'Weather',
                # 'yaxis' : {
                #     'range' : [0,100]
                # }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)