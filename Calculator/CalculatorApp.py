# Importing the Tkinter GUI
import tkinter as tk

class CalculatorApp:
    # Initialize the attributes of the Calculator
    def __init__(self):
        self.window = tk.Tk() #Creates a object of the Tkinter GUI
        self.window.title("Calculator") # Title of the application
        self.window.geometry("375x667") # Window size of the application
        self.window.resizable(0, 0) # Keeps the window to the fixed size mentioned in self.window.geometry()

        self.total_expression = ""
        self.current_expression = ""
        self.output_container = self.create_output_container()

        self.total_expression_container, self.expression_container = self.create_expression_containers()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    # Function to create the clear and equal buttons
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    # Function to create the containers for the expressions displayed on the calculator
    def create_expression_containers(self):
        total_expression_container = tk.Label(self.output_container, text=self.total_expression, anchor=tk.E, bg="#1C1C1C",
                               fg="#FFFFFF", padx=24, font=("Helvetica", 20))
        total_expression_container.pack(expand=True, fill='both')

        expression_container = tk.Label(self.output_container, text=self.current_expression, anchor=tk.E, bg="#1C1C1C",
                         fg="#FFFFFF", padx=24, font=("Helvetica", 40, "bold"))
        expression_container.pack(expand=True, fill='both')

        return total_expression_container, expression_container


    def create_output_container(self):
        frame = tk.Frame(self.window, height=221, bg="#FFFFFF")
        frame.pack(expand=True, fill="both")
        return frame

    # Function to add the input value to the current expression
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_expression_container()

    # Function to create the numerical buttons on the calculator
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="#505050", fg="#FFFFFF", font=("Helvetica", 25, "bold"),
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # Function to add the operators to the current expression
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_expression_container()
        self.update_expression_container()

    # Function to create the operator buttons
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="#FF9500", fg="#FFFFFF", font=("Helvetica", 20),
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    # Function to perform the actions of the clear button
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_expression_container()
        self.update_total_expression_container()

    # Function to create the clear button
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="Clear", bg="#D4D4D2", fg="#000000", font=("Helvetica", 20),
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    # Function to calculate the total expression
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_expression_container()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_expression_container()

    # Function to create the equal button
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#FF9500", fg="#FFFFFF", font=("Helvetica", 20),
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    # Function to create the containers for the buttons
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # Function to update the value in the total expression container
    def update_total_expression_container(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_expression_container.config(text=expression)

    def update_expression_container(self):
        self.expression_container.config(text=self.current_expression[:11])

    # Executes program until user closes the app
    def run(self):
        self.window.mainloop()

# Main Program
if __name__ == "__main__":
    calc = CalculatorApp()
    calc.run()