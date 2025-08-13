# streamlit_app.py
import streamlit as st
import subprocess

st.title("Trade Scanner")

if st.button("Run Scanner"):
    with st.spinner("Running scanner..."):
        try:
            import os
		script_path = os.path.join(os.getcwd(), 'scanner.py')
		result = subprocess.run(['python', script_path], capture_output=True, text=True, cwd=os.getcwd())
            st.success("Scanner completed!")
            st.text(result.stdout)
            if result.stderr:
                st.error(result.stderr)
        except Exception as e:
            st.error(f"Error: {str(e)}")

