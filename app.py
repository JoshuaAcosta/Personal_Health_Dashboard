import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Health Dashboard', page_icon=':bar_chart:', layout='wide')

#Reading data from csv file

def get_scale_data():
    cols = ["weight", "body_fat", "muscle_mass", "water", "bmi", "date"]
    df = pd.read_csv('data/history.csv', names=cols, header=0)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    df['body_fat'] = df['body_fat'].str.strip('%').astype('float')
    return df

def get_a1c_data():
    df = pd.read_csv('data/a1c.csv')
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df



df = get_scale_data()
df2 = get_a1c_data()

last_updated = df.date.max()

st.title(':bar_chart: Health Dashboard')
st.header(f'Last Updated: {last_updated}')

#Top KPI

current_weight = df.query('date == date.max()')['weight'].values[0]
current_bmi = df.query('date == date.max()')['bmi'].values[0]
current_bodyfat = df.query('date == date.max()')['body_fat'].values[0]
starting_weight = 318
goal_weight = 220
lbs_lost = round(starting_weight - current_weight,1)
lbs_left = round(current_weight - goal_weight,1)
goal_bmi = 24
bmi_delta = round(current_bmi-goal_bmi,1)
goal_body_fat = 15.0
starting_body_fat = 45.7
body_fat_delta = round(float(current_bodyfat) - goal_body_fat,1)
body_fat_lost = round(starting_body_fat - float(current_bodyfat),1)


left_column, mid_column, right_column = st.columns(3)

with left_column:
    st.subheader(f"current weight: {current_weight} lbs")
    st.subheader(f"lbs lost: {lbs_lost}")
    st.subheader(f"lbs delta: {lbs_left}")

with mid_column:
    st.subheader(f"Current BMI: {current_bmi}")
    st.subheader(f"BMI delta: {bmi_delta}")

with right_column:
    st.subheader(f"Current Body Fat: {current_bodyfat}")
    st.subheader(f"Body Fat Loss: {body_fat_lost}")
    st.subheader(f"Body Fat Delta: {body_fat_delta}")


# Charts

left_column2, mid_column2= st.columns(2)

fig = px.line(df, x='date', y='weight', title='Weight By Date')
fig2 = px.line(df, x='date', y='bmi', title='BMI By Date')
fig3 = px.line(df, x='date', y='body_fat', title='Body Fat % By Date')
fig4 = px.line(df2, x='date', y='reading', title='A1C% By Date')

left_column2.plotly_chart(fig, user_container_width=True)
mid_column2.plotly_chart(fig2, user_container_width=True)

left_column3, mid_column3= st.columns(2)
left_column3.plotly_chart(fig3, user_container_width=True)
mid_column3.plotly_chart(fig4, user_container_width=True)

#right_column2.plotly_chart(fig3, user_container_width=True)
#st.plotly_chart(fig3, user_container_width=True)