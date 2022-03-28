from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# My First App

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


import pandas as pd
import pandas_profiling
import streamlit as st

#from streamlit_gallery.utils import readme
from streamlit_pandas_profiling import st_profile_report
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

# DATA_URL = () 
nrows=10
data = pd.read_csv("iris.csv")
lowercase = lambda x: str(x).lower()
data.rename(lowercase, axis='columns', inplace=True)
#data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

st.subheader('Raw data')
st.write(data.head(10))
st.bar_chart(data.head(10))
pr = ProfileReport(data.head(5))

st_profile_report(pr)
#print(data.dtypes)
#print(data.head(10))
