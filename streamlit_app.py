import streamlit as st
import subprocess
import os
import sys

st.title("Trade Scanner")

if st.button("Run Scanner"):
    with st.spinner("Running scanner..."):
        try:
            # Get the correct path to scanner.py
            script_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(script_dir, 'scanner.py')
            
            # Check if scanner.py exists
            if not os.path.exists(script_path):
                st.error(f"Scanner file not found at: {script_path}")
                st.info("Please make sure scanner.py is in the same directory as this app.")
            else:
                # Run the scanner script
                result = subprocess.run([
                    sys.executable, 
                    script_path
                ], capture_output=True, text=True, cwd=script_dir)
                
                if result.returncode == 0:
                    st.success("Scanner completed!")
                    if result.stdout:
                        st.text("Output:")
                        st.code(result.stdout)
                else:
                    st.error("Scanner failed!")
                    if result.stderr:
                        st.text("Error:")
                        st.code(result.stderr)
                        
        except Exception as e:
            st.error(f"Error running scanner: {str(e)}")