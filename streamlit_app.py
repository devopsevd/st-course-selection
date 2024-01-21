# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
from st_aggrid import AgGrid

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
# for row in df.itertuples():
#     st.write(f"{row.core} has a :{row.short}:")

# df = conn.read(
#     worksheet="summary",
#     ttl="10m",
#     usecols=[0, 1,2,3],
#     nrows=15,
# )

AgGrid(df)
