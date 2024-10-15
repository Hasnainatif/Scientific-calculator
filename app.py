import streamlit as st

# Function to perform basic arithmetic operations
def calculator():
    st.title("Simple Calculator")

    # Select operation
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Input numbers
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")

    # Perform calculation
    if operation == "Add":
        result = num1 + num2
        st.success(f"{num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"{num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"{num1} * {num2} = {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"{num1} / {num2} = {result}")
        else:
            st.error("Error! Division by zero.")

# Run the calculator function in the Streamlit app
if __name__ == '__main__':
    calculator()
