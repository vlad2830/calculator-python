import tkinter as tk
from tkinter import ttk
from src.calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.root.configure(bg='#f0f0f0')
        
        self.calculator = Calculator()
        self.current_number = ""
        self.first_number = None
        self.operation = None
        
        # Создаем и настраиваем дисплей
        self.display_var = tk.StringVar(value="0")
        self.display = ttk.Entry(
            root,
            textvariable=self.display_var,
            justify="right",
            font=('Arial', 20),
            state='readonly'
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Определяем кнопки
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        
        style = ttk.Style()
        style.configure('Calculator.TButton', font=('Arial', 14))
        
        for (text, row, col) in buttons:
            button = ttk.Button(
                root,
                text=text,
                style='Calculator.TButton',
                command=lambda t=text: self.button_click(t)
            )
            button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        
        # Настраиваем растяжение строк и столбцов
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        if value.isdigit() or value == '.':
            self.current_number += value
            self.display_var.set(self.current_number)
        
        elif value in ['+', '-', '*', '/']:
            if self.current_number:
                self.first_number = float(self.current_number)
                self.operation = value
                self.current_number = ""
        
        elif value == '=':
            if self.first_number is not None and self.current_number and self.operation:
                second_number = float(self.current_number)
                try:
                    if self.operation == '+':
                        result = self.calculator.add(self.first_number, second_number)
                    elif self.operation == '-':
                        result = self.calculator.subtract(self.first_number, second_number)
                    elif self.operation == '*':
                        result = self.calculator.multiply(self.first_number, second_number)
                    elif self.operation == '/':
                        result = self.calculator.divide(self.first_number, second_number)
                    
                    self.display_var.set(str(result))
                    self.first_number = result
                    self.current_number = ""
                    self.operation = None
                except ValueError as e:
                    self.display_var.set("Ошибка")
                    self.clear()
        
        elif value == 'C':
            self.clear()
    
    def clear(self):
        self.current_number = ""
        self.first_number = None
        self.operation = None
        self.display_var.set("0")

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()