# streamlit_app.py
import streamlit as st
import subprocess

st.title("Trade Scanner")

if st.button("Run Scanner"):
    with st.spinner("Running scanner..."):
        try:
            result = subprocess.run(['python', 'scanner.py'], 
                                  capture_output=True, text=True)
            st.success("Scanner completed!")
            st.text(result.stdout)
            if result.stderr:
                st.error(result.stderr)
        except Exception as e:
            st.error(f"Error: {str(e)}")
