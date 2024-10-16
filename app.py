import streamlit as st
import matplotlib.pyplot as plt

# Functions for conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
st.title("Temperature Converter")

# Unit selection
option = st.selectbox("Choose conversion type:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

# Input temperature
if option == "Celsius to Fahrenheit":
    celsius_temp = st.number_input("Enter temperature in Celsius:", value=0.0)
    if celsius_temp < -273.15:
        st.error("Temperature cannot be below absolute zero!")
    else:
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        st.write(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")

else:
    fahrenheit_temp = st.number_input("Enter temperature in Fahrenheit:", value=32.0)
    if fahrenheit_temp < -459.67:
        st.error("Temperature cannot be below absolute zero!")
    else:
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        st.write(f"{fahrenheit_temp}°F is equal to {celsius_temp:.2f}°C")

# Visualization
celsius_values = list(range(-20, 41, 5))
fahrenheit_values = [celsius_to_fahrenheit(c) for c in celsius_values]

plt.figure()
plt.plot(celsius_values, fahrenheit_values, marker='o', label='Celsius to Fahrenheit')
plt.title('Celsius to Fahrenheit Conversion')
plt.xlabel('Celsius (°C)')
plt.ylabel('Fahrenheit (°F)')
plt.axhline(y=32, color='r', linestyle='--', label='Freezing Point (32°F)')
plt.axvline(x=0, color='b', linestyle='--', label='Freezing Point (0°C)')
plt.legend()
st.pyplot(plt)
