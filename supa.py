import streamlit as st
import pandas as pd
from supabase import create_client

SUPABASE_URL="https://hejcslylimllszoyxpfj.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhlamNzbHlsaW1sbHN6b3l4cGZqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDIwOTAsImV4cCI6MjA4MTYxODA5MH0.cvMTIZ3yeNS2qMgWJaCeYxe1nqEjkVdDcdGBb60wzHY"

supabase=create_client(SUPABASE_URL,SUPABASE_KEY)

st.title("HDFC BANK(supabase)")

menu=("REGISTER","VIEW")
choice=st.sidebar.selectbox("Menu",menu)

if choice=="REGISTER":
    name=st.text_input("Enter Name")
    age=st.number_input("AGE",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    balance=st.number_input("BALANCE",min_value=1000)
    if st.button("Save"):
        supabase.table("users").insert({
            "name":name,
            "age":age,
            "account":account,
            "balance":balance}).execute()
        st.success("user added successfully")

if choice=="VIEW":
    st.subheader("view users")
    data=supabase.table("users").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)
