import streamlit as st
import math

# Function to perform scientific operations
def scientific_calculator():
    st.title("Scientific Calculator")

    # Select operation type
    operation_type = st.selectbox("Select operation type", ["Basic", "Scientific"])

    # Basic Calculator
    if operation_type == "Basic":
        operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
        num1 = st.number_input("Enter first number", format="%f")
        num2 = st.number_input("Enter second number", format="%f")

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

    # Scientific Calculator
    if operation_type == "Scientific":
        # Choose scientific operation
        operation = st.selectbox("Select scientific operation", ["Square Root", "Power", "Logarithm", "Sine", "Cosine", "Tangent"])
        
        # Input for single-operand functions (e.g., sine, cosine, sqrt)
        if operation in ["Square Root", "Logarithm", "Sine", "Cosine", "Tangent"]:
            num = st.number_input("Enter the number", format="%f")

            if operation == "Square Root":
                result = math.sqrt(num)
                st.success(f"√{num} = {result}")
            elif operation == "Logarithm":
                if num > 0:
                    result = math.log10(num)
                    st.success(f"log10({num}) = {result}")
                else:
                    st.error("Logarithm is undefined for non-positive numbers.")
            elif operation == "Sine":
                result = math.sin(math.radians(num))
                st.success(f"sin({num}) = {result}")
            elif operation == "Cosine":
                result = math.cos(math.radians(num))
                st.success(f"cos({num}) = {result}")
            elif operation == "Tangent":
                result = math.tan(math.radians(num))
                st.success(f"tan({num}) = {result}")
        
        # Input for two-operand functions (e.g., power)
        elif operation == "Power":
            base = st.number_input("Enter the base", format="%f")
            exponent = st.number_input("Enter the exponent", format="%f")
            result = math.pow(base, exponent)
            st.success(f"{base}^{exponent} = {result}")

# Run the scientific calculator
if __name__ == '__main__':
    scientific_calculator()
