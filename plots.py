import pandas as pd
import plotly.express as px

def scatter():
    df = pd.read_csv('data.csv',delimiter=';')
    fig = px.scatter(df, x='n1',y='lns1')
    fig.show()

scatter()
