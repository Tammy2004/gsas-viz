import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import csv
from io import StringIO

st.title("GSAS Peak Visualizer")

uploaded_file = st.file_uploader("Upload GSAS CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, skiprows=38, delim_whitespace=True, engine='python')
    
    st.write("Preview of Data:")
    st.dataframe(df.head())

    # separate columns into individuals
    st.write("Parsed column names:", list(df.columns))


    x = df["x"]
    y_obs = df["y_obs"]
    
    # Simulated predicted peak (just Gaussian for now)
    center = st.slider("Peak center", min_value=float(x.min()), max_value=float(x.max()), value=30.0)
    width = st.slider("Peak width", 0.1, 5.0, 1.0)
    intensity = st.slider("Peak intensity", 10.0, 500.0, 100.0)
    
    y_calc = intensity * np.exp(-((x - center) ** 2) / (2 * width ** 2))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_obs, mode='lines', name='Observed'))
    fig.add_trace(go.Scatter(x=x, y=y_calc, mode='lines', name='Calculated'))
    st.plotly_chart(fig)
