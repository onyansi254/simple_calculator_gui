import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root, width=312, height=272.5, bg="grey")
        btns_frame.pack()

        self.create_buttons(btns_frame)

    def create_buttons(self, frame):
        buttons = [
            '7', '8', '9', 'C',
            '4', '5', '6', '/',
            '1', '2', '3', '*',
            '0', '.', '=', '+'
        ]

        row_val = 0
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            b = tk.Button(frame, text=button, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=action)
            b.grid(row=row_val, column=col_val, padx=1, pady=1)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        zero_button = tk.Button(frame, text='0', fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click_event('0'))
        zero_button.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        minus_button = tk.Button(frame, text='-', fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click_event('-'))
        minus_button.grid(row=4, column=2, padx=1, pady=1)

    def click_event(self, key):
        if key == 'C':
            self.expression = ""
            self.input_text.set("")
        elif key == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(key)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("312x324")
    calculator = Calculator(root)
    root.mainloop()
