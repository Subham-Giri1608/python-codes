import tkinter as tk
from tkinter import ttk
import math

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    choice = int(combobox_choice.get())

    if choice == 1:
        result.set(f"The addition of two numbers is: {num1 + num2}")
    elif choice == 2:
        result.set(f"The subtraction of two numbers is: {num1 - num2}")
    elif choice == 3:
        result.set(f"The multiplication of two numbers is: {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            result.set(f"The division of two numbers is: {num1 / num2}")
        else:
            result.set("Cannot divide by zero!")
    elif choice == 5:
        result.set(f"{num1} raised to the power of {num2} is: {num1 ** num2}")
    elif choice == 6:
        result.set(f"The square root of {num1} is: {math.sqrt(num1)}")
    elif choice == 7:
        result.set(f"The modulus of {num1} and {num2} is: {num1 % num2}")
    elif choice == 8:
        result.set(f"The sine of {num1} is: {math.sin(math.radians(num1))}")
    elif choice == 9:
        result.set(f"The cosine of {num1} is: {math.cos(math.radians(num1))}")
    elif choice == 10:
        result.set(f"The tangent of {num1} is: {math.tan(math.radians(num1))}")
    elif choice == 11:
        result.set(f"The natural logarithm of {num1} is: {math.log(num1)}")
    elif choice == 12:
        if num1 >= 0 and num1.is_integer():
            result.set(f"The factorial of {num1} is: {factorial(int(num1))}")
        else:
            result.set("Factorial is only defined for non-negative integers.")
    else:
        result.set("Invalid Input, please choose the correct input from the above options")

# Create the main window
window = tk.Tk()
window.title("Advanced Calculator")

# Create input fields and labels
label_num1 = ttk.Label(window, text="Enter your First number:")
entry_num1 = ttk.Entry(window)

label_num2 = ttk.Label(window, text="Enter your Second number:")
entry_num2 = ttk.Entry(window)

label_choice = ttk.Label(window, text="Choose operation:")
options = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation",
        "Square Root", "Modulus", "Sine", "Cosine", "Tangent", "Natural Logarithm", "Factorial"]
combobox_choice = ttk.Combobox(window, values=options, state="readonly")

# Create a button to perform calculations
calculate_button = ttk.Button(window, text="Calculate", command=calculate)

# Create a label to display the result
result = tk.StringVar()
result_label = ttk.Label(window, textvariable=result)

# Place widgets in the window
label_num1.pack()
entry_num1.pack()

label_num2.pack()
entry_num2.pack()

label_choice.pack()
combobox_choice.pack()

calculate_button.pack()

result_label.pack()

# Start the main loop
window.mainloop()
