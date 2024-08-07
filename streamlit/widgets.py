import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")
age = st.slider("Select your age", 0, 100, 18)

options = ["Python", "Java", "C++", "C", "JavaScript"]
choice = st.selectbox("Choose your favourite language: ",options)

if name:
    st.write(f"Hello, {name}")
st.write(f"Your age is: {age}")
st.write(f"You selected: {choice}")

data = {
    "Name": ["Alex", "Kane", "John", "Glenn"],
    "Age" : [32, 37, 30, 36],
    "City": ["Birmingham", "Wellington", "San Francisco", "Melbourne"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)