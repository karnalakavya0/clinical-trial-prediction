
import streamlit as st
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("updated_data.csv")

# Extract unique values for dropdowns
development_units = df["Development Unit"].dropna().unique().tolist()
phases = df["phase"].dropna().unique().tolist()
countries = df["studystatus"].dropna().unique().tolist()  # Assuming studystatus relates to country
new_indications = df["new_indication"].dropna().unique().tolist()
bindings = df["blinding"].dropna().unique().tolist()
pediatrics = df["pediatriconly"].dropna().unique().tolist()

# Streamlit UI
st.title("Clinical Trial Prediction Site Initialization")
if st.button("Get Started"):
    st.session_state["page"] = "prediction"

# Prediction Page
if st.session_state.get("page") == "prediction":
    st.header("Clinical Trial Prediction")
    
    dev_unit = st.selectbox("Development Unit", development_units)
    phase = st.selectbox("Phase", phases)
    country = st.selectbox("Country", countries)
    new_indication = st.selectbox("New Indication", new_indications)
    binding = st.selectbox("Binding", bindings)
    pediatric = st.selectbox("Pediatric", pediatrics)
    
    if st.button("Predict"):
        # Placeholder model: Replace with actual model
        ctt_fp_weeks = np.random.randint(10, 50)
        fp_fsi_weeks = np.random.randint(5, 30)
        total_weeks = ctt_fp_weeks + fp_fsi_weeks
        
        st.write(f"CTT-FP Weeks: {ctt_fp_weeks}")
        st.write(f"FP-FSI Weeks: {fp_fsi_weeks}")
        st.write(f"Total Weeks: {total_weeks}")
