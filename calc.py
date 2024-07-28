import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x400")
        self.resizable(0, 0)
        self.configure(bg='yellow')
        
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        
        result_frame = tk.Frame(self, bg='grey')
        result_frame.pack(expand=True, fill='both')

        result_entry = tk.Entry(result_frame, textvariable=self.result_var, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
        result_entry.pack(expand=True, fill='both', padx=10, pady=10)
        
        button_frame = tk.Frame(self, bg='grey')
        button_frame.pack(expand=True, fill='both')

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'Clear', '0', '=', '+'
        ]

        row = 0
        col = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            bg_color = 'red' if button == 'Clear' else 'black'
            b = tk.Button(button_frame, text=button, font=('Arial', 18), bg=bg_color, fg='white', borderwidth=0, command=action)
            b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
            button_frame.rowconfigure(i, weight=1)
        
    def on_button_click(self, char):
        if char == 'Clear':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "ERROR"
        else:
            self.expression += str(char)
        
        self.result_var.set(self.expression)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
