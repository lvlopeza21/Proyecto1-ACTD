# -*- coding: utf-8 -*-

# Ejecute esta aplicación con 
# python app1.py
# y luego visite el sitio
# http://127.0.0.1:8050/ 
# en su navegador.

import dash
from dash import dcc  # dash core components
from dash import html # dash html components
import plotly.express as px
import pandas as pd
import app3 as bk
from dash.dependencies import Input, Output, State
import plotly.express as px



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,title='Dashboard análisis productividad')
server = app.server


#########################################################DATA#######################################################################
# en este primer ejemplo usamos unos datos de prueba que creamos directamente
# en un dataframe de pandas 
df = pd.DataFrame({
    "Fiebre": ["Moderada", "Leve", "Alta", "Moderada", "Leve", "Alta"],
    "Casos": [4, 1, 2, 2, 4, 5],
    "Diagnóstico": ["Positivo", "Positivo", "Positivo", "Negativo", "Negativo", "Negativo"]
})


#ANÁLISIS DESCRIPTIVO

#Gráfica productividad anual
fig = bk.fig

#gráfica análisis por departamento
fig2 = px.bar(df, x="Fiebre", y="Casos", color="Diagnóstico", barmode="group")


#########################################################CSS#######################################################################

titulo_style = {
    'font-family': 'Jomolhari',
    'font-style': 'normal',
    'font-weight': '400',
    'font-size': '40px',
    'line-height': '51px',
    'color': '#000000',
    'width': '1440px',
    'height': '70px',
    'left': '0px',
    'top': '0px',
    'background': '#4E567F'
}

tab_style = {
    'font-family': 'Jomolhari',
    'font-size': '20px',
}

prod_anual={
    'font-family': 'Jomolhari',
    'font-size': '30px',
}

equipo_prod={
    'width': '600px',
   
}
graf_prod={
    'width': '600px',
}

an_dept={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '378px',
    'height': '51px',
    'left': '732px',
    'top': '171px',
}

drop_dep={
    'position': 'absolute',
    'width': '600px',
    'left': '732px',
    'top': '227px',
}

slider_prod={
    'width': '600px'
}

an_graph={
    'position': 'absolute',
    'width': '600px',
    'height': '455px',
    'left': '732px',
    'bottom': '5px',
    
}

slider_analisis={
    'position': 'absolute',
    'width': '600px',
    'height': '455px',
    'left': '732px',
    'top': '719px',
}

not_style={
    'font-family': 'Jomolhari',
    'font-size': '30px',
}

not_graph={
    'width': '600px',
}

slider_analisis3={
   
    'width': '600px',
    
}

prod_promedio={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '578px',
    'height': '51px',
    'left': '732px',
    'top': '720px',

}

slider_analisis4={
    'position': 'absolute',
    'width': '600px',
    'height': '35px',
    'left': '722px',
    'top': '777px',
}

graph4={
    'position': 'absolute',
    'width': '600px',
    'left': '722px',
    'top': '820px',
}

osico={
    'font-family': 'Jomolhari',
    'font-size': '30px',
}

graph5={
    'position': 'absolute',
    'width': '600px',
    'top': '1360px',
}


slider_analisis5={
    'position': 'absolute',
    'width': '600px',
    'top': '1320px',

}

overtim={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'left': '722px',
    'top':'1250px',
    'width': '600px',

}

graph6={
    'position': 'absolute',
    'left': '722px',
    'top': '1380px',
    'width': '600px',
}

slider_analisis6={
    'position': 'absolute',
    'left': '792px',
    'top':'1320px',
    'width': '600px',
    'left': '722px',
}




#########################################################TAB1#######################################################################

#PESTAÑA DE ANÁLISIS DESCRIPTIVO
tab1_layout = html.Div([
    #PRODUCTIVIDAD ANUAL
    html.H1(children='Productividad anual por equipo',style=prod_anual),
    #dropdown de productividad anual para la variable EQUIPO
     dcc.Dropdown(
        id='filtro-variable2',style=equipo_prod,
        options=[{'label': x, 'value': x} for x in bk.df['team'].unique()],
        placeholder='Seleccione un equipo'
    ),
    #gráfica de productividad anual
    dcc.Graph(
        id='graph',style=graf_prod,
        figure=bk.fig  # Asume que fig es tu figura para el análisis descriptivo
    ),

    
    #PRODUCTIVIDAD POR DEPARTAMENTO
    html.H1(children='Productividad por departamento',style=an_dept),
    html.Div([dcc.Dropdown(
        id='filtro-variable3',
        options=[{'label': x, 'value': x} for x in bk.df['department'].unique()],
        placeholder='Seleccione un departamento',
    )],style=drop_dep),
    
    dcc.Graph(
        id='graph2',style=an_graph,
        figure= px.bar(title='Seleccione un equipo para ver la productividad')  # Asume que fig es tu figura para el análisis descriptivo
    ),
    
    #NO OF STYLE CHANGE 
    html.H1(children='Not of style change',style=not_style),
    
    dcc.Dropdown(
        id='filtro-variable4',style=slider_analisis3,
        options=[{'label': x, 'value': x} for x in bk.df['team'].unique()],
        placeholder='Seleccione un equipo'
    ),
    
    dcc.Graph(
        id='graph3',style=not_graph,
        figure=bk.fig2, # Asume que fig es tu figura para el análisis descriptivo
    ),
    
    #PROD ACTUAL VS. PROD DESEADA
    html.H1(children='Productividad actual vs. productividad deseada',style=prod_promedio),
    
    html.Div([dcc.Dropdown(
        id='filtro-variable5',
        options=[{'label': x, 'value': x} for x in bk.df['team'].unique()],
        placeholder='Seleccione un equipo'
    )],style=slider_analisis4),
    
    dcc.Graph(
        id='graph4',style=graph4,
        figure=bk.fig3, # Asume que fig es tu figura para el análisis descriptivo
    ),
    
    #IDLE MEN POR DEPARTAMENTO Y IDLE TIME POR DEPARTAMENTO
    html.H1(children='Tiempo oscioso vs. productividad',style=osico),
    
    html.Div([dcc.Dropdown(
        id='filtro-variable6',
        options=['idle_men','idle_time'],
        placeholder='Seleccione una opción'
    )],style=slider_analisis5),
    
    dcc.Graph(
        id='graph5',style=graph5,
        figure=bk.fig4, # Asume que fig es tu figura para el análisis descriptivo
    ),
    
    #Overtime por departamento
    html.H1(children='Overtime por departamento',style=overtim),
    
    html.Div([dcc.Dropdown(
        id='filtro-variable7',
        options=[{'label': x, 'value': x} for x in bk.df['department'].unique()],
        placeholder='Seleccione un departamento'
    )],style=slider_analisis6),
    
    dcc.Graph(
        id='graph6',style=graph6,
        figure=bk.fig5, # Asume que fig es tu figura para el análisis descriptivo
    ),
])

#########################################################TAB2#######################################################################

prod={
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'top': '170px',
}

graph7={
    'position': 'absolute',
    'width': '600px',
}

slider_analisis7={

    'width': '600px',
}

an_dept2={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '378px',
    'height': '51px',
    'left': '732px',
    'top': '200px',
}

an_graph2={
    'position': 'absolute',
    'width': '600px',
    'height': '455px',
    'left': '732px',
    'top': '270px',
    
}

an_dept3={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '378px',
    'height': '51px',
    
    'top': '700px',
}

def generate_table(data):
    return html.Table(className='table', children=[
        html.Thead(
            html.Tr([html.Th('Nombre')])
        ),
        html.Tbody([
            html.Tr([html.Td(name)]) for name in data
        ])
        
    ], style=table)
data=bk.sig


table={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '20px',
    'width': '378px',
    'height': '151px',
    'top': '790px',
    'border': '4px solid purple',
    'border-collapse': 'collapse',
    'margin': 'auto', 
    'text-align': 'center',
    'left': '60px',
    'vertical-align': 'middle',
}

ev={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '378px',
    'height': '51px',
    'right': '280px',
    'top': '700px',
}

slider_analisis8={
    'position': 'absolute',
    'width': '600px',
    'height': '51px',
    'right': '60px',
    'top': '750px',
}

metr={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '25px',
    'width': '378px',
    'height': '51px',
    'right': '280px',
    'top': '800px',
    'backgroundColor': '#F8F0FF',
}

result={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '380px',
    'height': '51px',
    'right': '270px',
    'top': '920px',
    
}

boton={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '20px',
    'width': '380px',
    'height': '51px',
    'right': '270px',
    'top': '1100px',
    
}

slider_analisis9={
    'position': 'absolute',
    'width': '378px',
    'height': '51px',
    'top': '740px',
}

# Contenido de la pestaña del modelo
tab2_layout = html.Div([
    html.H1(children='Efecto de cada variable sobre la productividad actual',style=prod),
    # Aquí puedes incluir tus visualizaciones u otros elementos para la segunda pestaña
     html.Div([dcc.Dropdown(
        id='filtro-variable_8',
        options=['targeted_productivity', 'smv', 'over_time', 'incentive',
            'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers',
            'team_1', 'team_2', 'team_3', 'team_4', 'team_5',
            'team_6', 'team_7', 'team_8', 'team_9', 'team_10', 'team_11', 
            'quarter_Quarter1', 'quarter_Quarter2', 'quarter_Quarter3',
            'quarter_Quarter4', 'day_Monday', 'day_Saturday',
            'day_Sunday', 'day_Thursday', 'day_Tuesday', 
            'department_finishing'],
        placeholder='Seleccione una variable'
    )],style=slider_analisis7),
    
    dcc.Graph(
        id='graph8',style=graph7,
        figure=bk.fig6, # Asume que fig es tu figura para el análisis descriptivo
    ),
    
    html.H1(children='Productividad real vs. productividad esperada',style=an_dept2),
    
    dcc.Graph(
        id='graph12',style=an_graph2,
        figure= bk.fig7,
    ),
    
    html.H1(children='Variables',style=an_dept3),
    
    html.Div(id='table'),
    html.H1(children='Evaluación del modelo',style=ev),
    
         html.Div([dcc.Dropdown(
             id='filtro-variable_11',
                options=[
            {'label': 'R-adjusted', 'value': '0.355'},
            {'label': 'Durbin Watson', 'value': '1.953'},
            {'label': 'MSE', 'value': '0.026'}
        ],
                placeholder='Seleccione una métrica'
    )],style=slider_analisis8),
    
    html.H1(id='metri',style=metr),     
    
    html.H1(children='Como el modelo no es globalmente significativo, se va realizar un modelo solamente con las variables significativas',style=result),    
    
    html.Button(children='Ir al nuevo modelo',id='but',n_clicks=0,style=boton), 
    
    html.Div([dcc.Dropdown(
        id='filtro-variable_12',
        options=[
        {'label': 'Significativas', 'value': 't1'},
        {'label': 'No significativas', 'value': 't2'},
        ],
        placeholder='Seleccione una opción'
    )],style=slider_analisis9),
])


ej={
    'font-family': 'Jomolhari',
    'font-size': '30px',
}

drop1={
    'width': '600px',
}

graph31={
    'width': '600px',
}

Fp={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '600px',
    'height': '151px',
    'left': '782px',
    'top': '170px',
    
}

p={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '600px',
    'height': '51px',
    'left': '782px',
    'top': '270px',
    'backgroundColor': '#F8F0FF',
}
bot={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '600px',
    'height': '51px',
    'left': '782px',
    'top': '370px',
}

a={
    'position': 'absolute',
    'font-family': 'Jomolhari',
    'font-size': '30px',
    'width': '600px',
    'height': '51px',
    'left': '782px',
    'top': '470px',
    'backgroundColor': '#F8F0FF',
}

tab3_layout = html.Div([
    html.H1(children='Modelo reducido vs. Modelo completo',style=prod),
    html.Div([dcc.Dropdown(
        id='filtro-variable31',
        options=[
        'R-ajustado',
        'Durbin-Watson',
        'MSE',
        ],
    )],style=drop1),
    
    dcc.Graph(
        id='graph31',style=graph31,
    ),
    
    
    html.H1(children='Prueba F parcial para comprobar si el nuevo modelo es mejor al modelo inicial',style=Fp),
    
    html.H1(children='P-value: 0.29',style=p),
    
    html.Button(children='Conclusión',id='buton',n_clicks=0,style=bot),
    
    html.H1(id='conc'),
])


# Crear el layout principal del dashboard con pestañas
app.layout = html.Div(children=[
    # Título del dashboard
    html.H1(children='Análisis de desempeño de producción',style=titulo_style),
   
    # Dos pestañas del dashboard
    dcc.Tabs(id='tabs', value="tab1",style=tab_style, children=[
        dcc.Tab(label='Análisis descriptivo', value='tab1', children=[tab1_layout]),
        dcc.Tab(label='Modelo inicial', value='tab2', children=[tab2_layout]),
        dcc.Tab(label='Modelo mejorado', value='tab3', children=[tab3_layout]),
    ]),
    
    

])


#########################################################TAB1#######################################################################

@app.callback(
    Output('graph', 'figure'),
    [Input('filtro-variable2', 'value')])
def update_graph(selected_team):
    if selected_team is not None:
        # Filtrar el DataFrame para obtener solo los datos del equipo seleccionado
        df_filtered = bk.df[bk.df['team'] == selected_team]
        
        # Crear la figura del gráfico con los datos filtrados
        fig = px.line(df_filtered, x='date', y='actual_productivity', title=f'Productividad del Equipo {selected_team}')
    else:
        # Si no se ha seleccionado ningún equipo, mostrar un gráfico vacío
        fig = bk.fig
    
    return fig

@app.callback(
    Output('graph2', 'figure'),
    [Input('filtro-variable3', 'value')])
def update_graph(selected_team):
    if selected_team is not None:
        # Filtrar el DataFrame para obtener solo los datos del equipo seleccionado
        df_filtered = bk.df[bk.df['department'] == selected_team]
        
        # Crear la figura del gráfico con los datos filtrados
        fig = px.bar(df_filtered, x='date', y='actual_productivity', title=f'Productividad diaria del Departamento {selected_team}')
    else:
        # Si no se ha seleccionado ningún equipo, mostrar un gráfico vacío
        fig = bk.gr
    
    return fig


@app.callback(
    Output('graph3', 'figure'),
    [Input('filtro-variable4', 'value')])
def update_graph(selected_team):
    if selected_team is not None:
        # Filtrar el DataFrame para obtener solo los datos del equipo seleccionado
        df_filtered = bk.df[bk.df['team'] == selected_team]
        
        # Crear la figura del gráfico con los datos filtrados
        fig = px.bar(df_filtered, y='actual_productivity', x='no_of_style_change', title=f'Productividad del Equipo {selected_team}',color_discrete_sequence=['purple'])
    else:
        # Si no se ha seleccionado ningún equipo, mostrar un gráfico vacío
        fig=bk.fig2
    
    return fig


@app.callback(
    Output('graph4', 'figure'),
    [Input('filtro-variable5', 'value')])
def update_graph(selected_team):
    if selected_team is not None:
        # Filtrar el DataFrame para obtener solo los datos del equipo seleccionado
        df_filtered = bk.df[bk.df['team'] == selected_team]
        
        # Crear la figura del gráfico con los datos filtrados
        fig = px.bar(df_filtered, x='date', y=["targeted_productivity","actual_productivity"], title=f'Productividad del Equipo {selected_team}',color_discrete_sequence=['purple','yellow'])
    else:
        # Si no se ha seleccionado ningún equipo, mostrar un gráfico vacío
        fig=bk.fig3
    
    return fig

@app.callback(
    Output('graph5', 'figure'),
    [Input('filtro-variable6', 'value')])
def update_graph(selected_team):
    if selected_team is not None:
        
        # Crear la figura del gráfico con los datos filtrados
        fig = px.scatter(bk.df, x='actual_productivity', y=selected_team, title=f'Productividad vs. {selected_team}')
    else:
        # Si no se ha seleccionado ningún equipo, mostrar un gráfico vacío
        fig=px.bar(title='Seleccione una opción')
    
    return fig

@app.callback(
    Output('graph6', 'figure'),
    [Input('filtro-variable7', 'value')])
def update_graph(selected_team):
    if selected_team is not None:
        # Filtrar el DataFrame para obtener solo los datos del equipo seleccionado
        df_filtered = bk.df[bk.df['department'] == selected_team]
        
        # Crear la figura del gráfico con los datos filtrados
        fig = px.scatter(df_filtered, x='over_time', y='actual_productivity', title=f'Productividad de Overtime {selected_team}')
    else:
        # Si no se ha seleccionado ningún equipo, mostrar un gráfico vacío
        fig = bk.fig5
    
    return fig


#########################################################TAB2#######################################################################
@app.callback(
    Output('graph8', 'figure'),
    [Input('filtro-variable_8', 'value')])
def update_graph(selected_team):
    if selected_team is not None:
        # Crear la figura del gráfico con los datos filtrados
        fig=px.scatter(data_frame=bk.X_train,x=selected_team, y=bk.residuals, title=f'Residuos vs. {selected_team}')

        fig.add_hline(y=0, line_dash="dash", line_color="red")
    else:
        # Si no se ha seleccionado ningún equipo, mostrar un gráfico vacío
        fig = px.bar(title='Seleccione una variable')
    
    return fig


@app.callback(
    Output('metri', 'children'),
    [Input('filtro-variable_11', 'value')])
def update_graph(value):
    if value is not None:
        return f'El valor de la metrica es {value}'
    else:
        return 'Por favor seleccione una métrica'
    
 
@app.callback(
    Output('tabs', 'value'),
    [Input('but', 'n_clicks')],
    [State('tabs', 'value')]
)
def switch_tab(n_clicks, current_tab):
    if n_clicks > 0 and current_tab == 'tab2':
        return 'tab3'
    return current_tab


@app.callback(
    Output('table', 'children'),
    [Input('filtro-variable_12', 'value')]
)
def update_table(selected_value):
    if selected_value is not None:
        if selected_value == 't1':
            return generate_table(bk.sig)
        elif selected_value == 't2':
            return generate_table(bk.nosig)
    else:
        return 'Por favor seleccione las variables que desea ver'


#########################################################TAB3#######################################################################

@app.callback(
    Output('graph31', 'figure'),
    [Input('filtro-variable31', 'value')])
def update_graph(selected_team):
    if selected_team is not None:
        # Crear la figura del gráfico con los datos filtrados
        fig = px.bar(bk.datos, x=selected_team, y='Modelo', title=f'Evaluación modelos')
    else:
        # Si no se ha seleccionado ningún equipo, mostrar un gráfico vacío
        fig = px.bar(title='Seleccione una métrica')
    
    return fig


@app.callback(
    Output('conc', 'children'),
    [Input('buton', 'n_clicks')]
)
def switch_tab(n_clicks):
    if n_clicks > 0:
        return html.H1(children='El modelo completo es mejor que el modelo inicial, por ende para mejorar la productividad la empresa debe enfocarse en incrementar los incentivos a los equipos, además debe disminuir el tiempo ocioso.',style=a)
    

if __name__ == '__main__':
    app.run_server(debug=True)
