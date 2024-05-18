import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Invalid operation"

        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Error: Invalid input")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='black')

# Set the window size to be twice as large
root.geometry("400x200")

# Create entry widgets for numbers
entry_num1 = tk.Entry(root, width=20, bg='black', fg='white')
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=20, bg='black', fg='white')
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Create label for operation choice
label_operation = tk.Label(root, text="Operation:", bg='black', fg='white')
label_operation.grid(row=1, column=0, padx=10, pady=10)

# Create dropdown menu for operation choice
operation_var = tk.StringVar(root)
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")
dropdown_operation = tk.OptionMenu(root, operation_var, *operation_choices)
dropdown_operation.config(bg='black', fg='white')
dropdown_operation["menu"].config(bg='black', fg='white')
dropdown_operation.grid(row=1, column=1, padx=10, pady=10)

# Create button to perform calculation
button_calculate = tk.Button(root, text="Calculate", command=calculate, bg='black', fg='white')
button_calculate.grid(row=2, columnspan=2, padx=10, pady=10)

# Create label to display result
label_result = tk.Label(root, text="Result: ", bg='black', fg='white')
label_result.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
