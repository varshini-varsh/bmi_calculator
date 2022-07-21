import streamlit as st
import pickle as pk
from PIL import Image

st.title("welcome to BMI calculator")
img = Image.open("bmi.jpg")

st.image(img)

weight = st.number_input("Enter your weight in kilogram", step=0.1)
height = st.number_input("Enter your height in cm")

bmi = weight/(height)**2

st.success(f"your bmi is {bmi}")
