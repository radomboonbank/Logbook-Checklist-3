
import streamlit as st
from datetime import datetime, timedelta
import json
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Logbook Checklist", layout="wide")

# Load credentials from secrets
creds_dict = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
scoped_creds = Credentials.from_service_account_info(creds_dict, scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(scoped_creds)

SHEET_ID = st.secrets["SHEET_ID"]
SHEET_NAME = st.secrets["SHEET_NAME"]
sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)

st.title("📋 check-Sheet พนักงานกะ ศูนย์นนทบุรี by Bank")

with st.form("log_form"):
    date = st.date_input("📅 วันที่ตรวจสอบ", value=datetime.today())
    time = st.time_input("⏰ เวลา", value=datetime.now().time(), step=timedelta(minutes=1))

    employee = st.selectbox("👷‍♂️ ชื่อพนักงาน", [
        "นายเสน่ห์ กองรส", "นายฉัตรชัย ดำคำ", "นายจักรี  พันธุ์เขียน", "นายเจตน์  บุญญดิเรก",
        "นายทรงศักดิ์  วนานุกัณฑ์", "นายสิริพงษ์  สินจินา", "นายนิวัฒน์ เก่งกล้า", "นายธีรักชาติ ขำสาย",
        "นายระดมบุญ ทักษณา", "นายลาภชนก  ทิมสถิตย์", "นายสิทธิพงษ์  หลงเจริญ", "นายภาคภูมิ  นิลธกิจ",
        "นายอานุภาพ พฤกษาวาณิชย์", "นายนพนัฐ  มิตรสมาน", "นายสรพล  อึ๊งอาภรณ์", "นายธนกร ทิพย์เที่ยงแท้"
    ])
    receiver = st.selectbox("📫 ชื่อผู้รับกะ", [
        "นายเสน่ห์ กองรส", "นายฉัตรชัย ดำคำ", "นายจักรี  พันธุ์เขียน", "นายเจตน์  บุญญดิเรก",
        "นายทรงศักดิ์  วนานุกัณฑ์", "นายสิริพงษ์  สินจินา", "นายนิวัฒน์ เก่งกล้า", "นายธีรักชาติ ขำสาย",
        "นายระดมบุญ ทักษณา", "นายลาภชนก  ทิมสถิตย์", "นายสิทธิพงษ์  หลงเจริญ", "นายภาคภูมิ  นิลธกิจ",
        "นายอานุภาพ พฤกษาวาณิชย์", "นายนพนัฐ  มิตรสมาน", "นายสรพล  อึ๊งอาภรณ์", "นายธนกร ทิพย์เที่ยงแท้"
    ])
    shift = st.selectbox("📂 ช่วงเวลาตลอดสอบ", ["ตรวจละ 00.00 - 08.00 น.", "ตรวจละ 08.00 - 16.00 น.", "ตรวจละ 16.00 - 24.00 น."])
    department = st.selectbox("🏢 ข้อมูลแผนกที่ตรวจสอบ", ["แผนก หอก1และ2", "แผนก หอก3และ4", "แผนก หอก5"])
    note = st.text_area("❗ หมายเหตุหรือปัญหา", "ถ้ามี")

    submitted = st.form_submit_button("✅ บันทึกข้อมูล")

    if submitted:
        row = [datetime.now().strftime("%Y%m%d%H%M%S"), str(date), str(time), employee, receiver, shift, department, "Alarm All", "ปกติ", note]
        sheet.append_row(row)
        st.success("✅ บันทึกข้อมูลเรียบร้อยแล้ว!")
