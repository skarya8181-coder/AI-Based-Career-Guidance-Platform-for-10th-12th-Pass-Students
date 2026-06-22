import plotly.express as px
import pandas as pd


def radar_chart(scores:dict, title='Aptitude Radar'):
    df = pd.DataFrame({'skill': list(scores.keys()), 'score': list(scores.values())})
    fig = px.line_polar(df, r='score', theta='skill', line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), title=title)
    return fig


def salary_bar(careers):
    df = pd.DataFrame(careers)
    fig = px.bar(df, x='career', y=['freshers', 'avg', 'experienced'], barmode='group')
    fig.update_layout(margin=dict(l=20,r=20,t=40,b=20), title='Salary Comparison')
    return fig
