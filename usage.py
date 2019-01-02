import dash_leaflet as dll
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    dll.Map(
        id='leaflet-map',
        center=[51.505, -0.09],
        zoom=13,
        children=[
            dll.TileLayer(id='tile-layer'),
            dll.Marker(
                position=[51.505, -0.09],
                children=[dll.Popup(children="Foo Bar")]
            )
        ]
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
