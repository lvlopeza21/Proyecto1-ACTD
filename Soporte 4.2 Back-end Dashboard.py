import pandas as pd
import statsmodels.api as sm
import plotly.express as px
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

df=pd.read_csv("data.txt")



from sklearn.preprocessing import LabelEncoder

df['department'] = df['department'].replace('finishing ', 'finishing')

lol=df.groupby('department')['actual_productivity'].mean().reset_index()

lol2=df.groupby('no_of_style_change')['actual_productivity'].mean().reset_index()

#GRÁFICA PRODUCTIVIDAD ANUAL
fig = px.bar(df, x="date", y="actual_productivity",title="Productividad actual total")

#Gráfica de productividad total por departamento 
gr = px.bar(x=lol['department'], y=lol['actual_productivity'],title="Productividad promedio por departamento")
gr.update_layout(
                  xaxis_title='Departamento',
                  yaxis_title='Productividad promedio actual')

#gráfica not of style change
fig2 = px.bar(x=lol2['no_of_style_change'], y=lol2['actual_productivity'],color_discrete_sequence=['purple'],title='Productividad promedio')
fig2.update_layout(
                  xaxis_title='no of style change',
                  yaxis_title='Productividad promedio actual')

#graf productividad actual vs productividad deseada
fig3 = px.bar(df, x="date", y=["targeted_productivity","actual_productivity"],title='productividad esperada vs. actual diaria')

#grafica idle men y idle time vs productividad
fig4 = px.bar(df, x="date", y="idle_men",color_discrete_sequence=['purple'])

#gráfica overtime
fig5 = px.scatter(df, y="actual_productivity", x="over_time",color_discrete_sequence=['purple'],title='Productividad vs. overtime')


#MODELO DE REGRESIÓN
df2=pd.read_csv("/Users/camilalopez/Downloads/base/data.txt")

df2 = pd.get_dummies(df2, columns=['team'], dtype = int)
df2 = pd.get_dummies(df2, columns=['quarter'], dtype = int)
df2 = pd.get_dummies(df2, columns=['day'], dtype = int)

df2['department'] = df2['department'].replace('finishing ', 'finishing')

df_sinWIP=df2.drop('wip', axis=1)

df_sinWIP = pd.get_dummies(df_sinWIP, columns=['department'], dtype = int)

df_sinWIP.columns

features = ['targeted_productivity', 'smv', 'over_time', 'incentive',
            'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers',
            'team_1', 'team_2', 'team_3', 'team_4', 'team_5',
            'team_6', 'team_7', 'team_8', 'team_9', 'team_10', 'team_11', 
            'quarter_Quarter1', 'quarter_Quarter2', 'quarter_Quarter3',
            'quarter_Quarter4', 'day_Monday', 'day_Saturday',
            'day_Sunday', 'day_Thursday', 'day_Tuesday', 
            'department_finishing']

X = df_sinWIP[features]
Y = df_sinWIP['actual_productivity']




X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)

X_train = sm.add_constant(X_train)

model = sm.OLS(Y_train, X_train).fit()

residuals =model.resid

#print(model.summary())

#length 300
Y_pred = model.predict(sm.add_constant(X_test))

# Gráfico de dispersión de X vs Residuos

fig6=px.scatter(x=X_train['smv'], y=residuals, title='Residuos')

fig6.add_hline(y=0, line_dash="dash", line_color="red")

fig7=px.scatter(x=Y_pred,y=Y_test)
fig7.update_layout(
                  xaxis_title='Productividad esperada',
                  yaxis_title='Productividad real')

fig7.add_trace(px.line(x=[Y_pred.min(), Y_pred.max()], 
                      y=[Y_pred.min(), Y_pred.max()]).data[0])


#variables signifivativas
sig=['targeted_productivity', 'smv', 'incentive',
    'idle_men', 'no_of_style_change', 'no_of_workers','team_1', 
    'team_6', 'team_8',  'team_11', 'quarter_Quarter1', 'quarter_Quarter2', 
    'quarter_Quarter3','quarter_Quarter4']

nosig=['over_time', 
            'idle_time', 'team_2', 'team_3', 'team_4', 'team_5',
            'team_7', 'team_9', 'team_10',
            'day_Monday', 'day_Saturday',
            'day_Sunday', 'day_Thursday', 'day_Tuesday', 
            'department_finishing']



new_features = ['targeted_productivity', 'smv', 'incentive', 'idle_men', 
                'team_1', 'team_2', 'team_3', 'team_4', 'team_5', 'team_6', 
                'team_7', 'team_8', 'team_9', 'team_10', 'team_11'
                ,'no_of_style_change', 'no_of_workers', 'quarter_Quarter1', 
                'quarter_Quarter2', 'quarter_Quarter3', 'quarter_Quarter4'
                ]


datos = {
    'Modelo': ['Nuevo','Mejorado'],
    'R-ajustado': [0.348,0.355],
    'MSE': [0.026, 0.026],
    'Durbin-Watson': [1.958, 1.953]
}

