import tkinter as tk
from tkinter import ttk, messagebox

class NumberSystemCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Number System Calculator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Color scheme
        bg_color = "#2c3e50"
        fg_color = "#ecf0f1"
        button_color = "#3498db"
        
        self.root.configure(bg=bg_color)
        
        # Title
        title_label = tk.Label(root, text="Number System Calculator", 
                              font=("Arial", 20, "bold"), 
                              bg=bg_color, fg=fg_color)
        title_label.pack(pady=20)
        
        # Main frame
        main_frame = tk.Frame(root, bg=bg_color)
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Operation selection
        operation_frame = tk.Frame(main_frame, bg=bg_color)
        operation_frame.pack(pady=10)
        
        tk.Label(operation_frame, text="Choose Operation:", 
                font=("Arial", 12), bg=bg_color, fg=fg_color).pack()
        
        self.operation_var = tk.StringVar(value="convert")
        
        operations = [
            ("Convert", "convert"),
            ("Addition", "add"),
            ("Subtraction", "subtract")
        ]
        
        button_frame = tk.Frame(operation_frame, bg=bg_color)
        button_frame.pack(pady=5)
        
        for text, value in operations:
            tk.Radiobutton(button_frame, text=text, variable=self.operation_var,
                          value=value, font=("Arial", 10), bg=bg_color, 
                          fg=fg_color, selectcolor=button_color,
                          command=self.update_ui).pack(side="left", padx=10)
        
        # Input frame
        self.input_frame = tk.Frame(main_frame, bg=bg_color)
        self.input_frame.pack(pady=20, fill="both", expand=True)
        
        self.bases = ["Binary", "Decimal", "Octal", "Hexadecimal"]
        
        self.create_convert_ui()
        
        # Result frame
        result_frame = tk.Frame(main_frame, bg=bg_color)
        result_frame.pack(pady=10, fill="x")
        
        tk.Label(result_frame, text="Result:", font=("Arial", 12, "bold"),
                bg=bg_color, fg=fg_color).pack()
        
        self.result_text = tk.Text(result_frame, height=4, font=("Arial", 11),
                                   bg="#34495e", fg=fg_color, relief="flat")
        self.result_text.pack(fill="x", padx=10, pady=5)
        
        # Calculate button
        calc_button = tk.Button(main_frame, text="CALCULATE", 
                               font=("Arial", 12, "bold"),
                               bg=button_color, fg=fg_color,
                               command=self.calculate, cursor="hand2",
                               relief="flat", padx=20, pady=10)
        calc_button.pack(pady=10)
        
        # Clear button
        clear_button = tk.Button(main_frame, text="Clear", 
                                font=("Arial", 10),
                                bg="#e74c3c", fg=fg_color,
                                command=self.clear_all, cursor="hand2",
                                relief="flat", padx=15, pady=5)
        clear_button.pack()
    
    def update_ui(self):
        # Clear input frame
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        operation = self.operation_var.get()
        
        if operation == "convert":
            self.create_convert_ui()
        else:
            self.create_arithmetic_ui()
    
    def create_convert_ui(self):
        bg_color = "#2c3e50"
        fg_color = "#ecf0f1"
        
        # Number input
        tk.Label(self.input_frame, text="Enter Number:", 
                font=("Arial", 11), bg=bg_color, fg=fg_color).grid(row=0, column=0, sticky="w", pady=5)
        self.num_entry = tk.Entry(self.input_frame, font=("Arial", 11), width=30)
        self.num_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # From base
        tk.Label(self.input_frame, text="From Base:", 
                font=("Arial", 11), bg=bg_color, fg=fg_color).grid(row=1, column=0, sticky="w", pady=5)
        self.from_base = ttk.Combobox(self.input_frame, values=self.bases, 
                                     state="readonly", font=("Arial", 11), width=28)
        self.from_base.set("Decimal")
        self.from_base.grid(row=1, column=1, pady=5, padx=10)
        
        # To base
        tk.Label(self.input_frame, text="To Base:", 
                font=("Arial", 11), bg=bg_color, fg=fg_color).grid(row=2, column=0, sticky="w", pady=5)
        self.to_base = ttk.Combobox(self.input_frame, values=self.bases, 
                                   state="readonly", font=("Arial", 11), width=28)
        self.to_base.set("Binary")
        self.to_base.grid(row=2, column=1, pady=5, padx=10)
    
    def create_arithmetic_ui(self):
        bg_color = "#2c3e50"
        fg_color = "#ecf0f1"
        
        # First number
        tk.Label(self.input_frame, text="First Number:", 
                font=("Arial", 11), bg=bg_color, fg=fg_color).grid(row=0, column=0, sticky="w", pady=5)
        self.num1_entry = tk.Entry(self.input_frame, font=("Arial", 11), width=30)
        self.num1_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # Second number
        tk.Label(self.input_frame, text="Second Number:", 
                font=("Arial", 11), bg=bg_color, fg=fg_color).grid(row=1, column=0, sticky="w", pady=5)
        self.num2_entry = tk.Entry(self.input_frame, font=("Arial", 11), width=30)
        self.num2_entry.grid(row=1, column=1, pady=5, padx=10)
        
        # Input base
        tk.Label(self.input_frame, text="Input Base:", 
                font=("Arial", 11), bg=bg_color, fg=fg_color).grid(row=2, column=0, sticky="w", pady=5)
        self.input_base = ttk.Combobox(self.input_frame, values=self.bases, 
                                      state="readonly", font=("Arial", 11), width=28)
        self.input_base.set("Decimal")
        self.input_base.grid(row=2, column=1, pady=5, padx=10)
        
        # Output base
        tk.Label(self.input_frame, text="Output Base:", 
                font=("Arial", 11), bg=bg_color, fg=fg_color).grid(row=3, column=0, sticky="w", pady=5)
        self.output_base = ttk.Combobox(self.input_frame, values=self.bases, 
                                       state="readonly", font=("Arial", 11), width=28)
        self.output_base.set("Decimal")
        self.output_base.grid(row=3, column=1, pady=5, padx=10)
    
    def get_base_value(self, base_name):
        bases = {
            "Binary": 2,
            "Decimal": 10,
            "Octal": 8,
            "Hexadecimal": 16
        }
        return bases.get(base_name, 10)
    
    def format_result(self, value, base):
        if base == 2:
            return bin(value)[2:] if value >= 0 else bin(value)
        elif base == 8:
            return oct(value)[2:] if value >= 0 else oct(value)
        elif base == 16:
            return hex(value)[2:].upper() if value >= 0 else hex(value)
        else:
            return str(value)
    
    def calculate(self):
        try:
            operation = self.operation_var.get()
            
            if operation == "convert":
                num = self.num_entry.get().strip()
                from_base = self.get_base_value(self.from_base.get())
                to_base = self.get_base_value(self.to_base.get())
                
                # Convert to decimal first
                decimal_value = int(num, from_base)
                
                # Convert to target base
                result = self.format_result(decimal_value, to_base)
                
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(1.0, f"{self.from_base.get()}: {num}\n")
                self.result_text.insert(tk.END, f"{self.to_base.get()}: {result}\n")
                self.result_text.insert(tk.END, f"Decimal value: {decimal_value}")
                
            else:  # Addition or Subtraction
                num1 = self.num1_entry.get().strip()
                num2 = self.num2_entry.get().strip()
                input_base = self.get_base_value(self.input_base.get())
                output_base = self.get_base_value(self.output_base.get())
                
                # Convert to decimal
                val1 = int(num1, input_base)
                val2 = int(num2, input_base)
                
                # Perform operation
                if operation == "add":
                    result_decimal = val1 + val2
                    op_symbol = "+"
                else:
                    result_decimal = val1 - val2
                    op_symbol = "-"
                
                # Format result
                result = self.format_result(result_decimal, output_base)
                
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(1.0, f"{num1} {op_symbol} {num2} ({self.input_base.get()})\n")
                self.result_text.insert(tk.END, f"Result ({self.output_base.get()}): {result}\n")
                self.result_text.insert(tk.END, f"Decimal value: {result_decimal}")
        
        except ValueError as e:
            messagebox.showerror("Error", "Invalid number for the chosen base!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def clear_all(self):
        self.result_text.delete(1.0, tk.END)
        
        operation = self.operation_var.get()
        if operation == "convert":
            self.num_entry.delete(0, tk.END)
        else:
            self.num1_entry.delete(0, tk.END)
            self.num2_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberSystemCalculator(root)
    root.mainloop()
