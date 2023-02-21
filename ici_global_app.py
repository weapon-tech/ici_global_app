#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install plotly
#pip install openpyxl

# In[2]:


#pip install dash 


# In[3]:


#pip install cufflinks


# In[4]:


import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import datetime
from datetime import date
import json
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# In[5]:


tna_data = pd.read_excel("tna.xlsx")

#tna_data['Total'] = tna_data.sum(axis=1)  # Sum across the row
tna_data['Year'] = pd.DatetimeIndex(tna_data['Date']).year
tna_data['Quarter'] = pd.DatetimeIndex(tna_data['Date']).quarter
tna_data = tna_data.sort_values(by=['Year', 'Quarter'], ascending=True)
#list(tna_data.columns)
#print(tna_data["Date"])


# In[6]:


fig1 = px.bar(tna_data, x="Date", y=["World"],
               title='Figure 1: Total Global Net Assets - 2008-Q1:2022',
               labels=dict(value="$US Trillions", variable="Legend"),
               template="seaborn")
fig1.update_layout(
    yaxis = dict(
        tickvals = [0, 10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000],
        ticktext = ['0', '10', '20', '30', '40', '50', '60','70']
    )
)

    
fig1.show()


# In[7]:


fig2 = px.bar(tna_data, x="Date", y=["Luxembourg", "Ireland",
                                        "Spain", "France","United Kingdom"],
              title='Figure 3: Total Net Assets - 2008-Q1:2022<br><sup>Selected European Jurisdictions',
              labels=dict(value="$US Trillions", variable="Legend"),
              template="seaborn")

fig2.update_layout(
    yaxis = dict(
        tickvals = [0, 2000000, 4000000, 6000000, 8000000, 10000000, 12000000, 14000000,16000000,18000000],
        ticktext = ['0', '2', '4', '6', '8', '10', '12','14','16','18']
    )
)
    
fig2.show()


# In[8]:


fig3 = px.bar(tna_data, x="Date", y=['Australia','China','Japan','South Korea'],
              title='Figure 5: Total Net Assets - 2008-Q1:2022<br><sup>Selected Asia-Pacific Jurisdictions',
              labels=dict(value="$US Trillions", variable="Legend"),
              template="seaborn")

fig3.update_layout(
    yaxis = dict(
        tickvals = [0, 2000000, 4000000, 6000000, 8000000],
        ticktext = ['0', '2', '4', '6', '8']
    )
)

    
fig3.show()


# In[9]:


flows_data = pd.read_excel("flows.xlsx").fillna(0)

#tna_data['Total'] = tna_data.sum(axis=1)  # Sum across the row
flows_data['Year'] = pd.DatetimeIndex(flows_data['Date']).year
flows_data['Quarter'] = pd.DatetimeIndex(flows_data['Date']).quarter
flows_data = flows_data.sort_values(by=['Year', 'Quarter'], ascending=True)
#list(flows_data.columns)


# In[10]:


fig4 = px.bar(flows_data, x="Date", y=["World"],
               title='Figure 2: Total Global Net Sales - 2008-Q1:2022',
               labels=dict(value="$US Trillions", variable="Legend"),
               template="seaborn")
fig4.update_layout(
    yaxis = dict(
        tickvals = [0, 200000, 400000, 600000, 800000, 1000000, 1200000],
        ticktext = ['0', '0.2', '0.4', '0.6', '0.8', '1', '1.2']
    )
)

    
fig4.show()


# In[11]:


fig5 = px.bar(flows_data, x="Date", y=["Luxembourg", "Ireland",
                                        "Spain", "France","United Kingdom"],
               title='Figure 4: Total Net Sales - 2008-Q1:2022<br><sup>Selected European Jurisdictions',
               labels=dict(value="$US Billions", variable="Legend"),
               template="seaborn")

fig5.update_layout(
    yaxis = dict(
        tickvals = [-100000, 0, 100000, 200000, 300000],
        ticktext = ['-100','0', '100', '200', '300']
    )
)
    
fig5.show()


# In[12]:


fig6 = px.bar(flows_data, x="Date",  y=['China','Japan','South Korea',"India"],
               title='Figure 6: Total Net Sales - 2008-Q1:2022<br><sup>Selected Asia-Pacific Jurisdictions',
               labels=dict(value="$US Billions", variable="Legend"),
               template="seaborn")


fig6.show()


# In[13]:


## Initialising App

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "ICI Global Monitoring Report"
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}


# In[14]:


# Page Layout 
fig1.update_layout(clickmode='event+select')
#fig1.update_traces(marker_size=20)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src="/assets/ICI_Global_Logo.png", className="header-logo",
                        style={"display":"inline-block","align-self":"center",'height':'10%', 'width':'10%'}), # Import ICI Global logo.png
                #html.H1(children="ICI Global Monitoring Report",  #Main Headings 
                        #className="header-title",
                       #style={"display":"inline-block"}),
                html.H2(children="Dashboard of selected Regulated Open-ended Mutual Fund metrics",  #Sub heading
                        className="sub-title"),
            ],
            className="header",
        ),
#         html.Div(
#             children=[
#                 html.Div(            
#                     children="Date Range",   #Date Range heading
#                     className="menu-title"
#                     ),
#                 dcc.DatePickerRange(    # Create Data range selection functionality
#                     id="date-range",
#                     min_date_allowed=(2003,1,1),
#                     max_date_allowed=ipos.Date.max().date(),
#                     start_date=ipos.Date.min().date(),
#                     end_date=ipos.Date.max().date(),
#                     display_format='DD MMM YY',
#                 ),
#             ],
#         className="menu",
#         ),
#             html.Div(id='output-container'),              
        html.Div([
            dcc.Tabs([
                dcc.Tab(label="Global",children=[
                    html.H3(children="Global Overview",   #Global section overview header
                            className="chart-title"),
                    html.Div(                            # Wrap all charts into one divison
                        children=[
                            html.Div(
                                children=dcc.Graph(
                                    id='Figure 1: Total Global Net Assets - 2008-Q1:2022',
                                    figure=fig1, config={"displayModeBar":True},
                                ),
                                className="card",
                            ),
                            html.Div(
                                children=dcc.Graph(
                                    id='Figure 2: Total Global Net Sales - 2008-Q1:2022',
                                    figure=fig4, config={"displayModeBar":True},
                                ),
                                className="card",
                            ),
                        ],
                        className="wrapper"
                    ),
                ]),
                dcc.Tab(label="European Funds",children=[
                html.H3(children="European Regional Overview",   #European overview
                           className="chart-title"),
                    html.Div(                            # Wrap all charts into one divison
                        children=[
                            html.Div(
                                children=dcc.Graph(
                                    id='Figure 3: Total Net Assets - 2008-Q1:2022<br><sup>Selected European Jurisdictions',
                                    figure=fig2, config={"displayModeBar":True},
                                ),
                                className="card",
                            ),
                            html.Div(
                                children=dcc.Graph(
                                    id='Figure 4: Total Net Sales - 2008-Q1:2022<br><sup>Selected European Jurisdictions',
                                    figure=fig5, config={"displayModeBar":True},
                                ),
                                className="card",
                            ),
                        ],
                        className="wrapper"
                    ),
                    
                ]),
                dcc.Tab(label="Asia-Pacific Funds",children=[
                    html.H3(children="Asia-Pacific Overview",   #APAC Overview
                           className="chart-title"), 
                    html.Div(                            # Wrap all charts into one divison
                        children=[
                            html.Div(
                                children=dcc.Graph(
                                    id='Figure 5: Total Net Assets - 2008-Q1:2022<br><sup>Selected Asia-Pacific Jurisdictions',
                                    figure=fig3, config={"displayModeBar":True},
                                ),
                                className="card",
                            ),
                            html.Div(
                                children=dcc.Graph(
                                    id='Figure 6: Total Net Sales - 2008-Q1:2022<br><sup>Selected Asia-Pacific Jurisdictions',
                                    figure=fig6, config={"displayModeBar":True},
                                ),
                                className="card",
                            ),
                        ],
                        className="wrapper"
                    ),
                ]),
            ]),         
        ]),
])


# In[ ]:


## App callbacks 

@app.callback(
    Output('hover-data', 'children'),
    Input('basic-interactions', 'hoverData'))
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)

@app.callback(
    [Output('Figure 1: Total Global Net Assets - 2008-Q1:2022',"figure")],
    [
        Input('date-range',"start_date"),
        Input('date-range',"end_date"),
    ],
)
def update_charts(start_date,end_date):
    mask = (
    (stock_data.Date>=start_date)
    &(stock_data.Date<=end_date)
    )
    filtered_data=data.loc[mask, :]
    fig0 = px.line(stock_data, x=filtered_data["Date"], y=filtered_data["Total"],
         color='Year',title = 'Figure 1: Total Global Net Assets - 2008-Q1:2022',
                 labels=dict(value="$US Trillions", variable="Legend")
                )
    return fig0
#     dash.dependencies.Output('output-container','children'),
#     [dash.dependencies.Input('date-range','start_date'),
#      dash.dependencies.Input('date-range','end_date')])
# def update_output(start_date,end_date):
#     string_prefix = "You have selected: "
#     if start_date is not None:
#         start_date_object = date.fromisoformat(start_date)
#         start_date_string = start_date_object,strftime('%B %d, %y')
#         string_prefix = string_prefix + "Start Date: " +start_date_string + '|'
#     if end_date is not None:
#         end_date_object = date.fromisoformat(end_date)
#         end_date_string = end_date_object,strftime('%B %d, %y')
#         string_prefix = string_prefix + "End Date: " +end_date_string
#     if len(string_prefix) == len ("You have selected: "):
#         return "Please select a date"
#     else: 
#         return string_prefix

@app.callback(
    Output('click-data', 'children'),
    Input('basic-interactions', 'clickData'))
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)

@app.callback(
    Output('selected-data', 'children'),
    Input('basic-interactions', 'selectedData'))
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)

@app.callback(
    Output('relayout-data', 'children'),
    Input('basic-interactions', 'relayoutData'))
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)

if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:




