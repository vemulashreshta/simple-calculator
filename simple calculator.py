import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        
        self.expression = ""
        self.result_var = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Result display
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        result_entry.grid(row=0, column=0, columnspan=4)
        
        # Digit buttons
        digits = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 1)
        ]
        for (text, row, col) in digits:
            self.create_button(text, row, col, self.add_to_expression)
        
        # Operation buttons
        operations = [
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('sqrt', 4, 0), ('^', 4, 2), ('C', 5, 0), ('=', 5, 3)
        ]
        for (text, row, col) in operations:
            self.create_button(text, row, col, self.perform_operation)
        
    def create_button(self, text, row, col, command):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                           command=lambda t=text: command(t))
        button.grid(row=row, column=col)
        
    def add_to_expression(self, value):
        self.expression += str(value)
        self.result_var.set(self.expression)
        
    def perform_operation(self, operation):
        try:
            if operation == 'C':
                self.expression = ""
            elif operation == '=':
                self.expression = str(eval(self.expression))
            elif operation == 'sqrt':
                self.expression = str(math.sqrt(float(self.expression)))
            elif operation == '^':
                self.expression += '**'
            else:
                self.expression += operation
            self.result_var.set(self.expression)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.expression = ""
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
