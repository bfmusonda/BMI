import streamlit as st

from PIL import Image

st.title("This is my BMI Calculator")


img = Image.open("bmi.jpg")
st.image(img)

# Introduction

st.subheader("Introduction")

st.text("""

BMI is a person’s weight in kilograms divided by the square of height in meters. A high BMI can indicate high body fatness.

If your BMI is less than 18.5, it falls within the underweight range.
If your BMI is 18.5 to <25, it falls within the healthy weight range.
If your BMI is 25.0 to <30, it falls within the overweight range.
If your BMI is 30.0 or higher, it falls within the obesity range.

Obesity is frequently subdivided into categories:

Class 1: BMI of 30 to < 35
Class 2: BMI of 35 to < 40
Class 3: BMI of 40 or higher. 
Class 3 obesity is sometimes categorized as “severe” obesity.

Credits: https://www.cdc.gov/obesity/adult/defining.html

	""")
# Input

def calculate_bmi(weight, height):
    if height == 0:
        st.error("Height cannot be zero. Please enter a valid height.")
        return None
    return round(weight / (height ** 2), 2)

# User inputs
weight = st.number_input("Enter your Weight in KG", step=0.1)
height = st.number_input("Enter your Height in Meters")

# Calculate BMI only if height is valid
bmi = calculate_bmi(weight, height)

if bmi is not None:
    st.success(f"Your BMI is {bmi}")

