import streamlit as st

def calculate_terminal_value(initial, growth, years):
    terminal_value = initial
    for year in range(years):
        terminal_value += growth * terminal_value
    return terminal_value

st.title("Hello Streamlit")
st.header("Calculate % Growth")

initial = st.number_input("Initial investment in USD")
growth = st.number_input("Growth Rate in %")
years = st.number_input("Growth Period in years")

terminal_value = calculate_terminal_value(initial, growth, int(years))

st.write(f'Terminal value of {initial} after {years} years at a growth rate of {growth}% is {terminal_value}')

