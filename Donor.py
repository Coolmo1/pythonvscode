"""
Create a menu for Registration and Database
Design a blood donation database that can get donor input
A, B, AB and O
-Name -Contact Number (use text)
-Blood group (use radio or selectbox) -Disease/Infection (use radio or selectbox)

-Submit donor details

Next, save these in a csv file and show the database in a Database page in the menu
"""

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

menu = st.sidebar.selectbox("Menu",["Registration","Donor Database"])

df = pd.read_csv("Donor.csv")

st.sidebar.write("Made By Moyo👍❤️")



if menu == "Registration":
    st.title("Come and donate")
    col1,col2 = st.columns(2)
    with col1:
        name = st.text_input("Enter in your name")
        age = st.number_input("Enter in your age",18)
        contactinfo = st.text_input("Enter your phone number or email")

    with col2:
       blood = st.radio("Blood type",["A","B","AB","O"])
       d = st.radio("Are you pronde to having disease or diseases",["yes","no"])

    if st.button("submit"):
        if name and age and contactinfo and blood and d:
            donordict = {"Name": [name], "Age" : [age], "Contactinformation" : [contactinfo], "Blood Type" : [blood], "Diseases" : [d]}
            donordf = pd.DataFrame(donordict)
            newdonordf = pd.concat([df,donordf])
            newdonordf.to_csv("Donor.csv",index = False)
            st.success("Your info has been successfully added")

        else:
            st.error("You need to fill in all the boxes")

if menu == "Donor Database":
    st.dataframe(df,use_container_width=True)


          


