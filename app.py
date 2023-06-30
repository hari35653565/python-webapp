import streamlit as st

def calculate_terminal_value(initial, years, growth_rate):
    terminal_value = initial * (1 + growth_rate) ** years
    return terminal_value

st.title("Hello Streamlit")
st.header("Calculate Terminal Value")

initial_investment = st.number_input("Initial investment in USD")
investment_years = st.number_input("Investment period in years")
growth_rate = st.number_input("Growth rate in %")

terminal_value = calculate_terminal_value(initial_investment, investment_years, growth_rate / 100)

st.write(f"Terminal value of {initial_investment} after {investment_years} years at a growth rate of {growth_rate}% is {terminal_value:.2f}")
