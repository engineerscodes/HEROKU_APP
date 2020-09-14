#import os
import delete
import wget
import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html



delete.remove()
'''TO GET DAILY DATA FROM MY CSV FILE '''
url = "https://drive.google.com/uc?export=download&id=1-QseMOhwLVCbijjO2mcMc_xXL3Bd2rM8"
filename = wget.download(url)
app = dash.Dash()
server = app.server

#data19.navee()
data=pd.read_csv('https://drive.google.com/uc?export=download&id=1-QseMOhwLVCbijjO2mcMc_xXL3Bd2rM8')
d=pd.DataFrame(data)
d.drop(d[d.District=='State Pool'].index,inplace=True)
d.drop(d[d.District=='Mahe'].index,inplace=True)
d.drop(d[d.District=='Evacuees'].index,inplace=True)
d.drop(d[d.District=='Banda'].index,inplace=True)
d.drop(d[d.District=='Italians'].index,inplace=True)
d.drop(d[d.District=='Salem'].index,inplace=True)

map_active = go.Scattermapbox(
    customdata=d.loc[:, ['ACTIVE CASES', "CONFIRMED CASES", "DECEASED CASES", "RECOVERED CASES"]],
    name='ACTIVE CASES',
    lon=d['longitude'],
    lat=d['Latitude'],
    mode='markers',
    text=d['District'],
    hovertemplate=
    "<b>%{text}</b><br><br>" +
    "ACTIVE: %{customdata[0]}<br>" +
    "<extra></extra>",
    fillcolor='mediumturquoise',
    showlegend=True,

    marker=go.scattermapbox.Marker(
        size=10,
        color='Red',
        opacity=1
    ),
    opacity=0.5,

)

map_confirmed = go.Scattermapbox(
        customdata=d.loc[:,['ACTIVE CASES',"CONFIRMED CASES","DECEASED CASES","RECOVERED CASES"]],
        name='CONFIRMED CASES',
        lon=d['longitude'],
        lat=d['Latitude'],
        mode='markers',
        text=d['District'],
        hovertemplate=
        "<b>%{text}</b><br><br>" +
        "CONFIRMED : %{customdata[1]}<br>" +
        "<extra></extra>",
        fillcolor='mediumturquoise',
        showlegend=True,

        marker=go.scattermapbox.Marker(
            size=10,
            color='YELLOW',
            opacity=1
        ),
        opacity=0.5,

    )

map_deceased = go.Scattermapbox(
        customdata=d.loc[:,['ACTIVE CASES',"CONFIRMED CASES","DECEASED CASES","RECOVERED CASES"]],
        name='DECEASED CASES',
        lon=d['longitude'],
        lat=d['Latitude'],
        mode='markers',
        text=d['District'],
        hovertemplate=
        "<b>%{text}</b><br><br>" +
        "DECEASED : %{customdata[2]}<br>" +
        "<extra></extra>",
        fillcolor='mediumturquoise',
        showlegend=True,

        marker=go.scattermapbox.Marker(
            size=10,
            color="Green",
            opacity=1,
        ),
        opacity=0.5,

    )
map_recovered = go.Scattermapbox(
    customdata=d.loc[:, ['ACTIVE CASES', "CONFIRMED CASES", "DECEASED CASES", "RECOVERED CASES"]],
    name='RECOVERED CASES',
    lon=d['longitude'],
    lat=d['Latitude'],
    mode='markers',
    text=d['District'],
    hovertemplate=
    "<b>%{text}</b><br><br>" +
    "RECOVERED : %{customdata[3]}<br>" +
    "<extra></extra>",
    fillcolor='mediumturquoise',
    showlegend=True,

    marker=go.scattermapbox.Marker(
        size=10,
        color="BLUE",
        opacity=1,
    ),
    opacity=0.5,

)
layout = go.Layout(
    height=800,
    mapbox_style="stamen-watercolor",
    autosize=True,
    # mapbox_layers=[
    # {
    # "below": 'traces',
    # "sourcetype": "raster",
    # "source": [
    #     "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"

    # ]
    # }
    # ],'''
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"

    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
data = [map_active,map_confirmed,map_deceased,map_recovered]

fig = go.Figure(data=data, layout=layout)
fig.update_layout(title='COVID 19 REAL-TIME REPORT <br>BY NAVEEN')
fig.update_layout(mapbox_style="open-street-map")

app.layout = html.Div([
    dcc.Graph(figure=fig)

])
if __name__ == '__main__':
    app.run_server(debug=False)