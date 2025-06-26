# Create a function named calculator_body()
# Within it, create 3 columns using the st.columns() function
# Note, in the video, this column function was still in beta
import streamlit as st

def calculator_body():
    st.write("---")
    # Create three columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Input1")
        num1 = st.number_input(label = "Enter first integer", step=1)
    with col2:
        st.header("Input2")
        num2 = st.number_input(label = "Enter second integer", step=2) # step=2 is just an example, you can use any step value you want
        # It changes the increment/decrement value when using the up/down arrows
        # You can also use step=0.1 for decimal numbers
        # or step=0.01 for more precision
    with col3:
        st.header("Operations")
        operator = st.selectbox(label = "Select an operator", 
                                options = ["Add", "Subtract", "Multiply", "Divide"])
    if st.button("Click here to calculate!"):
        if num2 == 0 and operator == "Divide":
            st.error("Cannot divide by zero! Enter a different number")
        else:
            calculator_function(num1, num2, operator)

def calculator_function(num1, num2, operator):
    if operator == "Add":
        result = num1 + num2
    elif operator == "Subtract":
        result = num1 - num2
    elif operator == "Multiply":
        result = num1 * num2
    elif operator == "Divide":
        result = num1 / num2
    else:
        result = None
    
    if result is not None:
        st.success(f"The result of {operator}ing {num1} and {num2} is: **{result}**")
    else:
        st.error("Invalid operation selected.")
