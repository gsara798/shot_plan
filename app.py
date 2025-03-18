import streamlit as st
import pandas as pd

# Cargar los datos
file_path = "Shot_plan.xlsx"
data = {
    "General": pd.read_excel(file_path, index_col=0, sheet_name='General'),
    "Target": pd.read_excel(file_path, index_col=0, sheet_name='Target'),
    "Drivers": pd.read_excel(file_path, index_col=0, sheet_name='Drivers'),
    "Beams": pd.read_excel(file_path, index_col=0, sheet_name='Beams'),
    "Diagnostics": pd.read_excel(file_path, index_col=0, sheet_name='Diagnostics'),
    "Expected": pd.read_excel(file_path, index_col=0, sheet_name='Expected')
}

# Función de búsqueda
def search_rid(rid, data_dict):
    results = {}
    for key, df in data_dict.items():
        if rid in df.index:
            results[key] = df.loc[rid]
    return results

# UI en Streamlit
st.title("Shot Plan Dashboard")

# Entrada de usuario para buscar RID
rid_to_search = st.number_input("RID:", min_value=0, step=1)

if st.button("Search"):
    search_results = search_rid(rid_to_search, data)
    if search_results:
        for sheet, result in search_results.items():
            st.subheader(f"Results in {sheet}")
            st.dataframe(result)
    else:
        st.warning("RID was not found.")
