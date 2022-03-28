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


nrows=10
data = pd.read_csv("iris.csv")
#st.write(data)
st.bar_chart(data.head(10))
