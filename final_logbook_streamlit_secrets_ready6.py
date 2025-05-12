
import streamlit as st
from datetime import datetime, timedelta

# ส่วนอื่นของโค้ด
time = st.time_input("⏰ เวลา", value=datetime.now().time(), step=timedelta(minutes=1))
