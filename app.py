import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Function to perform scientific operations
def scientific_calculator():
    st.title("Scientific Calculator")

    # Select operation type
    operation_type = st.selectbox("Select operation type", ["Basic", "Scientific", "Graph"])

    # Basic Calculator
    if operation_type == "Basic":
        operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
        num1 = st.number_input("Enter first number", format="%f")
        num2 = st.number_input("Enter second number", format="%f")

        if st.button("Calculate", key='basic', type='primary', use_container_width=False, help="Perform the basic operation"):
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
    elif operation_type == "Scientific":
        # Choose scientific operation
        operation = st.selectbox("Select scientific operation", ["Square Root", "Power", "Logarithm", "Sine", "Cosine", "Tangent"])

        # Input for single-operand functions (e.g., sine, cosine, sqrt)
        if operation in ["Square Root", "Logarithm", "Sine", "Cosine", "Tangent"]:
            num = st.number_input("Enter the number", format="%f")

            if st.button("Calculate", key='scientific', type='primary'):
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

            if st.button("Calculate", key='power', type='primary'):
                result = math.pow(base, exponent)
                st.success(f"{base}^{exponent} = {result}")

    # Graph Functionality
    elif operation_type == "Graph":
        st.write("Graph Functions")
        
        # Select function to graph
        graph_type = st.selectbox("Select graph function", ["Sine", "Cosine", "Tangent"])

        # Set range for graphing
        x_min = st.number_input("Enter minimum value of x", value=-10)
        x_max = st.number_input("Enter maximum value of x", value=10)

        # Generate x values
        x = np.linspace(x_min, x_max, 400)

        if st.button("Plot Graph", key='graph', type='primary'):
            plt.figure(figsize=(10, 5))
            
            if graph_type == "Sine":
                y = np.sin(x)
                plt.plot(x, y, label="sin(x)")
            elif graph_type == "Cosine":
                y = np.cos(x)
                plt.plot(x, y, label="cos(x)")
            elif graph_type == "Tangent":
                y = np.tan(x)
                plt.plot(x, y, label="tan(x)")
                plt.ylim(-10, 10)  # Limit y values for tangent to avoid infinity jumps

            plt.title(f"{graph_type} Function")
            plt.xlabel("x values")
            plt.ylabel(f"{graph_type}(x)")
            plt.legend()

            st.pyplot(plt)

# Run the scientific calculator
if __name__ == '__main__':
    scientific_calculator()
