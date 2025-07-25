import streamlit as st 

def render_header():
    st.sidebar.title("Options Pricing & Greeks Analysis")
    
    # Credits section
    st.sidebar.markdown(
        "<div style='text-align: left;'>"
        "<p style='color: #666; font-size: 0.8em;'>"
        "Created by "
        "<a href='https://www.linkedin.com/in/saimanish-prabhakar-3074351a0/' "
        "target='_blank' style='color: #1f77b4;'>Saimanish Prabhakar</a>"
        "</p>"
        "</div>",
        unsafe_allow_html=True
    )
    st.sidebar.markdown("---")