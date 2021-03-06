import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([html.H1('Dash Layout'), dcc.Graph(id='Example',
figure={
    'data': [
    {'x': [1,2,3,4,5], 'y': [8,3,6,2,9], 'type': 'line', 'name': 'boats'},
    {'x': [1,2,3,4,5], 'y': [4,6,2,8,3], 'type': 'bar', 'name': 'cars'}
],
'layout': {
    'title': 'Basic Dash Example'
}
})])

if __name__ == '__main__':
    app.run_server(debug=True)
