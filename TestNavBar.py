# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:23:56 2020

@author: a
"""

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

# make a reuseable navitem for the different examples

# custom navbar based on https://getbootstrap.com/docs/4.1/examples/dashboard/
dashboard = dbc.Navbar(
    [
        dbc.Col(dbc.NavbarBrand("Dashboard", href="www.google.fr"), sm=3, md=2),
        dbc.Col(dbc.Input(type="search", placeholder="Search here")),
        dbc.Col(
            dbc.Nav(dbc.NavItem(dbc.NavLink("Sign out")), navbar=True),
            width="auto",
        ),
    ],
    color="dark",
    dark=True,
)

app.layout = html.Div(
    dashboard
)




if __name__ == "__main__":
    app.run_server(debug=False, port=8888)