from collections import namedtuple
import string
import altair as alt
import math
from numpy import datetime64
import pandas as pd

import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import  st_profile_report
import matplotlib as plot
import plotly_express as px
"""
# EDA(Exploratory Data Analysis) on Solar Edge Energy readings
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


nrows=100
data = pd.read_csv("ENERGY.from.20171117_000000.to.20171215_000000.saved.at.20220330_103532.csv")
#print(data.describe)
#print(data['meters__values__date'])
#st.write(data)
#st.bar_chart(data.head(10))
#print(data.dtypes)
data = pd.read_csv("ENERGY.from.20171117_000000.to.20171215_000000.saved.at.20220330_103532.csv")
#print(data.describe)
#print(data['meters__values__date'])
#st.write(data)
#st.bar_chart(data.head(10))
#print(data.dtypes)
#data=data.tail(100)

data['timeUnit']=data['timeUnit'].astype(str)
data['unit']=data['unit'].astype(str)
data['meters__type']=data['meters__type'].astype(str)
data['meters__values__date']=data['meters__values__date'].astype(datetime64)
data['meters__values__value']=data['meters__values__value'].astype(int)
data=data.drop(['timeUnit','unit'],axis=1)
df_1 = data.iloc[:2688,:]
df_2 = data.iloc[2688:5376]
df_3=data.iloc[5376:8064]
df_4=data.iloc[8064:10752]
df_5=data.iloc[10752:13440]
#df_5
df_2['meters__']='FeedIn'
df_1['meters__']='Production'
df_3['meters__']='Purchase'
df_4['meters__']='Self_Consumption'
df_5['meters__']='Consumption'
#df_2
#df_2=df_2.drop(['meters__values__date'],axis=1)
df_2.rename(columns={'meters__values__value':'metersvalues_feedIn','meters__':'meter_type1'}, 
                 inplace=True)
df_1.rename(columns={'meters__values__value':'metersvalues_Production','meters__':'meter_type2'},
                 inplace=True)

df_3.rename(columns={'meters__values__value':'metersvalues_Purchase','meters__':'meter_type3'},
                 inplace=True)
df_4.rename(columns={'meters__values__value':'metersvalues_Self_Consumption','meters__':'meter_type4'}, 
                 inplace=True)
df_5.rename(columns={'meters__values__value':'metersvalues_Consumption','meters__':'meter_type5'},
                 inplace=True)


df_2=df_2.set_index(['meters__values__date'])
df_1=df_1.set_index(['meters__values__date'])
df_3=df_3.set_index(['meters__values__date'])
df_4=df_4.set_index(['meters__values__date'])
df_5=df_5.set_index(['meters__values__date'])
df_1=df_1.drop(['meters__type'],axis=1)
df_2=df_2.drop(['meters__type'],axis=1)
df_3=df_3.drop(['meters__type'],axis=1)
df_4=df_4.drop(['meters__type'],axis=1)
df_5=df_5.drop(['meters__type'],axis=1)

df_concat = pd.concat([df_1, df_2,df_3,df_4,df_5],axis=1)
#df_concat
f_new = df_concat.drop(['meter_type1','meter_type2','meter_type3','meter_type4','meter_type5'],axis=1)
st.area_chart(f_new)
f_new1=ProfileReport(f_new)
padding = 0
import matplotlib.pyplot as plt
# This dataframe has 244 lines, but 4 distinct values for `day`
sum=f_new.sum(axis=0)
fig=sum.plot(kind='pie')
#fig.show()
st.write(fig)
st_profile_report(f_new1)