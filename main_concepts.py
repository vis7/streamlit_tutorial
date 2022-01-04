import pandas as pd
import streamlit as st
import numpy as np
import time

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

st.write("... and now we\'re done!")
