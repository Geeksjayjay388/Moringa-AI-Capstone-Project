import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from datetime import datetime

class NumberSystemCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Number System Calculator")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # History storage
        self.history = []
        
        # Color schemes
        self.themes = {
            "dark": {
                "bg": "#1a1a2e",
                "fg": "#eee",
                "accent": "#16213e",
                "button": "#0f3460",
                "button_hover": "#533483",
                "error": "#e94560"
            },
            "light": {
                "bg": "#f5f5f5",
                "fg": "#333",
                "accent": "#fff",
                "button": "#4a90e2",
                "button_hover": "#357abd",
                "error": "#e74c3c"
            }
        }
        
        self.current_theme = "dark"
        self.colors = self.themes[self.current_theme]
        
        self.root.configure(bg=self.colors["bg"])
        
        # Create menu bar
        self.create_menu()
        
        # Create main container
        self.create_ui()
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save History", command=self.save_history)
        file_menu.add_command(label="Load History", command=self.load_history)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Toggle Theme", command=self.toggle_theme)
        view_menu.add_command(label="View History", command=self.show_history_window)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Bitwise Operations", command=self.show_bitwise_window)
        tools_menu.add_command(label="ASCII Converter", command=self.show_ascii_window)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="How to Use", command=self.show_help)
        help_menu.add_command(label="About", command=self.show_about)
    
    def create_ui(self):
        # Title with styling
        title_frame = tk.Frame(self.root, bg=self.colors["bg"])
        title_frame.pack(pady=15)
        
        title_label = tk.Label(title_frame, text="🔢 Advanced Number System Calculator", 
                              font=("Arial", 22, "bold"), 
                              bg=self.colors["bg"], fg=self.colors["fg"])
        title_label.pack()
        
        subtitle = tk.Label(title_frame, text="Convert • Calculate • Analyze", 
                           font=("Arial", 10, "italic"), 
                           bg=self.colors["bg"], fg=self.colors["fg"])
        subtitle.pack()
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors["bg"])
        main_container.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Left panel (Operations)
        left_panel = tk.Frame(main_container, bg=self.colors["accent"], relief="raised", bd=2)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Operation selection
        operation_frame = tk.Frame(left_panel, bg=self.colors["accent"])
        operation_frame.pack(pady=15, padx=15)
        
        tk.Label(operation_frame, text="Choose Operation:", 
                font=("Arial", 13, "bold"), bg=self.colors["accent"], fg=self.colors["fg"]).pack()
        
        self.operation_var = tk.StringVar(value="convert")
        
        operations = [
            ("Convert", "convert", "🔄"),
            ("Addition", "add", "➕"),
            ("Subtraction", "subtract", "➖"),
            ("Multiplication", "multiply", "✖️"),
            ("Division", "divide", "➗"),
            ("Modulo", "modulo", "%")
        ]
        
        button_grid = tk.Frame(operation_frame, bg=self.colors["accent"])
        button_grid.pack(pady=10)
        
        row, col = 0, 0
        for text, value, emoji in operations:
            btn = tk.Button(button_grid, text=f"{emoji} {text}", 
                          command=lambda v=value: self.select_operation(v),
                          font=("Arial", 10), bg=self.colors["button"], 
                          fg=self.colors["fg"], cursor="hand2",
                          relief="flat", padx=15, pady=8, width=12)
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        # Input frame
        self.input_frame = tk.Frame(left_panel, bg=self.colors["accent"])
        self.input_frame.pack(pady=15, padx=15, fill="both", expand=True)
        
        self.bases = ["Binary", "Decimal", "Octal", "Hexadecimal"]
        
        self.create_convert_ui()
        
        # Buttons frame
        buttons_frame = tk.Frame(left_panel, bg=self.colors["accent"])
        buttons_frame.pack(pady=10)
        
        calc_button = tk.Button(buttons_frame, text="🧮 CALCULATE", 
                               font=("Arial", 12, "bold"),
                               bg=self.colors["button"], fg=self.colors["fg"],
                               command=self.calculate, cursor="hand2",
                               relief="flat", padx=25, pady=12)
        calc_button.grid(row=0, column=0, padx=5)
        
        clear_button = tk.Button(buttons_frame, text="🗑️ Clear", 
                                font=("Arial", 11),
                                bg=self.colors["error"], fg=self.colors["fg"],
                                command=self.clear_all, cursor="hand2",
                                relief="flat", padx=20, pady=10)
        clear_button.grid(row=0, column=1, padx=5)
        
        copy_button = tk.Button(buttons_frame, text="📋 Copy Result", 
                               font=("Arial", 11),
                               bg="#27ae60", fg=self.colors["fg"],
                               command=self.copy_result, cursor="hand2",
                               relief="flat", padx=20, pady=10)
        copy_button.grid(row=0, column=2, padx=5)
        
        # Right panel (Results & Info)
        right_panel = tk.Frame(main_container, bg=self.colors["accent"], relief="raised", bd=2)
        right_panel.pack(side="right", fill="both", expand=True)
        
        # Result frame
        result_label_frame = tk.Frame(right_panel, bg=self.colors["accent"])
        result_label_frame.pack(pady=10, fill="x")
        
        tk.Label(result_label_frame, text="📊 Result:", font=("Arial", 13, "bold"),
                bg=self.colors["accent"], fg=self.colors["fg"]).pack()
        
        self.result_text = tk.Text(right_panel, height=8, font=("Courier New", 11),
                                   bg=self.colors["bg"], fg="#00ff00", 
                                   relief="sunken", bd=2, wrap="word")
        self.result_text.pack(fill="both", expand=True, padx=15, pady=5)
        
        # All bases display
        all_bases_label = tk.Label(right_panel, text="🔢 All Base Representations:", 
                                   font=("Arial", 12, "bold"),
                                   bg=self.colors["accent"], fg=self.colors["fg"])
        all_bases_label.pack(pady=(10, 5))
        
        self.all_bases_text = tk.Text(right_panel, height=6, font=("Courier New", 10),
                                      bg=self.colors["bg"], fg=self.colors["fg"],
                                      relief="sunken", bd=2, wrap="word")
        self.all_bases_text.pack(fill="both", expand=True, padx=15, pady=5)
        
        # Step by step explanation
        step_label = tk.Label(right_panel, text="📝 Step-by-Step:", 
                             font=("Arial", 12, "bold"),
                             bg=self.colors["accent"], fg=self.colors["fg"])
        step_label.pack(pady=(10, 5))
        
        self.step_text = tk.Text(right_panel, height=6, font=("Arial", 9),
                                bg=self.colors["bg"], fg=self.colors["fg"],
                                relief="sunken", bd=2, wrap="word")
        self.step_text.pack(fill="both", expand=True, padx=15, pady=(5, 15))
    
    def select_operation(self, operation):
        self.operation_var.set(operation)
        self.update_ui()
    
    def update_ui(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        operation = self.operation_var.get()
        
        if operation == "convert":
            self.create_convert_ui()
        else:
            self.create_arithmetic_ui()
    
    def create_convert_ui(self):
        tk.Label(self.input_frame, text="Enter Number:", 
                font=("Arial", 11, "bold"), bg=self.colors["accent"], 
                fg=self.colors["fg"]).grid(row=0, column=0, sticky="w", pady=8, padx=5)
        self.num_entry = tk.Entry(self.input_frame, font=("Arial", 12), width=25,
                                 bg=self.colors["bg"], fg=self.colors["fg"], 
                                 insertbackground=self.colors["fg"])
        self.num_entry.grid(row=0, column=1, pady=8, padx=5)
        
        tk.Label(self.input_frame, text="From Base:", 
                font=("Arial", 11, "bold"), bg=self.colors["accent"], 
                fg=self.colors["fg"]).grid(row=1, column=0, sticky="w", pady=8, padx=5)
        self.from_base = ttk.Combobox(self.input_frame, values=self.bases, 
                                     state="readonly", font=("Arial", 11), width=23)
        self.from_base.set("Decimal")
        self.from_base.grid(row=1, column=1, pady=8, padx=5)
        
        tk.Label(self.input_frame, text="To Base:", 
                font=("Arial", 11, "bold"), bg=self.colors["accent"], 
                fg=self.colors["fg"]).grid(row=2, column=0, sticky="w", pady=8, padx=5)
        self.to_base = ttk.Combobox(self.input_frame, values=self.bases, 
                                   state="readonly", font=("Arial", 11), width=23)
        self.to_base.set("Binary")
        self.to_base.grid(row=2, column=1, pady=8, padx=5)
    
    def create_arithmetic_ui(self):
        tk.Label(self.input_frame, text="First Number:", 
                font=("Arial", 11, "bold"), bg=self.colors["accent"], 
                fg=self.colors["fg"]).grid(row=0, column=0, sticky="w", pady=8, padx=5)
        self.num1_entry = tk.Entry(self.input_frame, font=("Arial", 12), width=25,
                                   bg=self.colors["bg"], fg=self.colors["fg"],
                                   insertbackground=self.colors["fg"])
        self.num1_entry.grid(row=0, column=1, pady=8, padx=5)
        
        tk.Label(self.input_frame, text="Second Number:", 
                font=("Arial", 11, "bold"), bg=self.colors["accent"], 
                fg=self.colors["fg"]).grid(row=1, column=0, sticky="w", pady=8, padx=5)
        self.num2_entry = tk.Entry(self.input_frame, font=("Arial", 12), width=25,
                                   bg=self.colors["bg"], fg=self.colors["fg"],
                                   insertbackground=self.colors["fg"])
        self.num2_entry.grid(row=1, column=1, pady=8, padx=5)
        
        tk.Label(self.input_frame, text="Input Base:", 
                font=("Arial", 11, "bold"), bg=self.colors["accent"], 
                fg=self.colors["fg"]).grid(row=2, column=0, sticky="w", pady=8, padx=5)
        self.input_base = ttk.Combobox(self.input_frame, values=self.bases, 
                                      state="readonly", font=("Arial", 11), width=23)
        self.input_base.set("Decimal")
        self.input_base.grid(row=2, column=1, pady=8, padx=5)
        
        tk.Label(self.input_frame, text="Output Base:", 
                font=("Arial", 11, "bold"), bg=self.colors["accent"], 
                fg=self.colors["fg"]).grid(row=3, column=0, sticky="w", pady=8, padx=5)
        self.output_base = ttk.Combobox(self.input_frame, values=self.bases, 
                                       state="readonly", font=("Arial", 11), width=23)
        self.output_base.set("Decimal")
        self.output_base.grid(row=3, column=1, pady=8, padx=5)
    
    def get_base_value(self, base_name):
        bases = {"Binary": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
        return bases.get(base_name, 10)
    
    def format_result(self, value, base):
        if value < 0:
            sign = "-"
            value = abs(value)
        else:
            sign = ""
            
        if base == 2:
            return sign + bin(value)[2:]
        elif base == 8:
            return sign + oct(value)[2:]
        elif base == 16:
            return sign + hex(value)[2:].upper()
        else:
            return sign + str(value) if sign else str(value)
    
    def show_all_bases(self, decimal_value):
        self.all_bases_text.delete(1.0, tk.END)
        self.all_bases_text.insert(tk.END, f"Binary:       {self.format_result(decimal_value, 2)}\n")
        self.all_bases_text.insert(tk.END, f"Octal:        {self.format_result(decimal_value, 8)}\n")
        self.all_bases_text.insert(tk.END, f"Decimal:      {decimal_value}\n")
        self.all_bases_text.insert(tk.END, f"Hexadecimal:  {self.format_result(decimal_value, 16)}\n")
    
    def explain_conversion(self, num, from_base, to_base, decimal_value, result):
        self.step_text.delete(1.0, tk.END)
        
        from_base_val = self.get_base_value(from_base)
        to_base_val = self.get_base_value(to_base)
        
        self.step_text.insert(tk.END, f"Step 1: Input '{num}' in {from_base} (base {from_base_val})\n")
        self.step_text.insert(tk.END, f"Step 2: Convert to Decimal = {decimal_value}\n")
        self.step_text.insert(tk.END, f"Step 3: Convert Decimal to {to_base} (base {to_base_val})\n")
        self.step_text.insert(tk.END, f"Step 4: Result = {result}\n")
    
    def explain_arithmetic(self, num1, num2, operation, input_base, result_decimal, result, output_base):
        self.step_text.delete(1.0, tk.END)
        
        ops = {
            "add": ("+", "Addition"),
            "subtract": ("-", "Subtraction"),
            "multiply": ("×", "Multiplication"),
            "divide": ("÷", "Division"),
            "modulo": ("%", "Modulo")
        }
        
        op_symbol, op_name = ops.get(operation, ("+", "Operation"))
        
        self.step_text.insert(tk.END, f"Step 1: Input numbers in {input_base}\n")
        self.step_text.insert(tk.END, f"   Number 1: {num1}\n")
        self.step_text.insert(tk.END, f"   Number 2: {num2}\n")
        self.step_text.insert(tk.END, f"Step 2: Perform {op_name}\n")
        self.step_text.insert(tk.END, f"Step 3: Result in Decimal = {result_decimal}\n")
        self.step_text.insert(tk.END, f"Step 4: Convert to {output_base} = {result}\n")
    
    def calculate(self):
        try:
            operation = self.operation_var.get()
            
            if operation == "convert":
                num = self.num_entry.get().strip()
                from_base = self.from_base.get()
                to_base = self.to_base.get()
                from_base_val = self.get_base_value(from_base)
                to_base_val = self.get_base_value(to_base)
                
                decimal_value = int(num, from_base_val)
                result = self.format_result(decimal_value, to_base_val)
                
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(1.0, f"Input ({from_base}):  {num}\n")
                self.result_text.insert(tk.END, f"Output ({to_base}): {result}\n")
                self.result_text.insert(tk.END, f"\nDecimal Value: {decimal_value}")
                
                self.show_all_bases(decimal_value)
                self.explain_conversion(num, from_base, to_base, decimal_value, result)
                
                self.add_to_history(f"Convert: {num} ({from_base}) → {result} ({to_base})")
                
            else:
                num1 = self.num1_entry.get().strip()
                num2 = self.num2_entry.get().strip()
                input_base = self.input_base.get()
                output_base = self.output_base.get()
                input_base_val = self.get_base_value(input_base)
                output_base_val = self.get_base_value(output_base)
                
                val1 = int(num1, input_base_val)
                val2 = int(num2, input_base_val)
                
                ops = {
                    "add": (lambda a, b: a + b, "+"),
                    "subtract": (lambda a, b: a - b, "-"),
                    "multiply": (lambda a, b: a * b, "×"),
                    "divide": (lambda a, b: a // b if b != 0 else 0, "÷"),
                    "modulo": (lambda a, b: a % b if b != 0 else 0, "%")
                }
                
                if operation in ops:
                    calc_func, op_symbol = ops[operation]
                    
                    if operation in ["divide", "modulo"] and val2 == 0:
                        messagebox.showerror("Error", "Cannot divide by zero!")
                        return
                    
                    result_decimal = calc_func(val1, val2)
                    result = self.format_result(result_decimal, output_base_val)
                    
                    self.result_text.delete(1.0, tk.END)
                    self.result_text.insert(1.0, f"{num1} {op_symbol} {num2} ({input_base})\n")
                    self.result_text.insert(tk.END, f"Result ({output_base}): {result}\n")
                    self.result_text.insert(tk.END, f"\nDecimal Value: {result_decimal}")
                    
                    self.show_all_bases(result_decimal)
                    self.explain_arithmetic(num1, num2, operation, input_base, result_decimal, result, output_base)
                    
                    self.add_to_history(f"{operation.title()}: {num1} {op_symbol} {num2} = {result} ({output_base})")
        
        except ValueError:
            messagebox.showerror("Error", "Invalid number for the chosen base!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def clear_all(self):
        self.result_text.delete(1.0, tk.END)
        self.all_bases_text.delete(1.0, tk.END)
        self.step_text.delete(1.0, tk.END)
        
        operation = self.operation_var.get()
        if operation == "convert":
            self.num_entry.delete(0, tk.END)
        else:
            self.num1_entry.delete(0, tk.END)
            self.num2_entry.delete(0, tk.END)
    
    def copy_result(self):
        try:
            result = self.result_text.get(1.0, tk.END).strip()
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            messagebox.showinfo("Success", "Result copied to clipboard!")
        except:
            messagebox.showerror("Error", "No result to copy!")
    
    def add_to_history(self, entry):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({"time": timestamp, "operation": entry})
    
    def save_history(self):
        if not self.history:
            messagebox.showwarning("Warning", "No history to save!")
            return
        
        filename = filedialog.asksaveasfilename(defaultextension=".json",
                                               filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            with open(filename, 'w') as f:
                json.dump(self.history, f, indent=4)
            messagebox.showinfo("Success", "History saved successfully!")
    
    def load_history(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            with open(filename, 'r') as f:
                self.history = json.load(f)
            messagebox.showinfo("Success", "History loaded successfully!")
    
    def show_history_window(self):
        if not self.history:
            messagebox.showinfo("History", "No history available!")
            return
        
        history_win = tk.Toplevel(self.root)
        history_win.title("Calculation History")
        history_win.geometry("600x400")
        history_win.configure(bg=self.colors["bg"])
        
        tk.Label(history_win, text="📜 Calculation History", font=("Arial", 16, "bold"),
                bg=self.colors["bg"], fg=self.colors["fg"]).pack(pady=10)
        
        text_widget = tk.Text(history_win, font=("Courier New", 10),
                             bg=self.colors["accent"], fg=self.colors["fg"])
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)
        
        for entry in reversed(self.history):
            text_widget.insert(tk.END, f"[{entry['time']}] {entry['operation']}\n")
        
        text_widget.config(state="disabled")
    
    def toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        messagebox.showinfo("Theme", "Please restart the application to apply the new theme.")
    
    def show_bitwise_window(self):
        bitwise_win = tk.Toplevel(self.root)
        bitwise_win.title("Bitwise Operations")
        bitwise_win.geometry("500x400")
        bitwise_win.configure(bg=self.colors["bg"])
        
        tk.Label(bitwise_win, text="🔧 Bitwise Operations", font=("Arial", 16, "bold"),
                bg=self.colors["bg"], fg=self.colors["fg"]).pack(pady=10)
        
        frame = tk.Frame(bitwise_win, bg=self.colors["accent"])
        frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        tk.Label(frame, text="Number 1 (Decimal):", bg=self.colors["accent"], 
                fg=self.colors["fg"]).grid(row=0, column=0, pady=5, sticky="w")
        bit_num1 = tk.Entry(frame, width=20)
        bit_num1.grid(row=0, column=1, pady=5)
        
        tk.Label(frame, text="Number 2 (Decimal):", bg=self.colors["accent"], 
                fg=self.colors["fg"]).grid(row=1, column=0, pady=5, sticky="w")
        bit_num2 = tk.Entry(frame, width=20)
        bit_num2.grid(row=1, column=1, pady=5)
        
        result_text = tk.Text(frame, height=10, width=50, bg=self.colors["bg"], 
                             fg=self.colors["fg"])
        result_text.grid(row=2, column=0, columnspan=2, pady=10)
        
        def calculate_bitwise():
            try:
                n1 = int(bit_num1.get())
                n2 = int(bit_num2.get())
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"AND: {n1 & n2} (Binary: {bin(n1 & n2)[2:]})\n")
                result_text.insert(tk.END, f"OR:  {n1 | n2} (Binary: {bin(n1 | n2)[2:]})\n")
                result_text.insert(tk.END, f"XOR: {n1 ^ n2} (Binary: {bin(n1 ^ n2)[2:]})\n")
                result_text.insert(tk.END, f"NOT {n1}: {~n1} (Binary: {bin(~n1)})\n")
                result_text.insert(tk.END, f"Left Shift {n1} << 1: {n1 << 1}\n")
                result_text.insert(tk.END, f"Right Shift {n1} >> 1: {n1 >> 1}\n")
            except:
                messagebox.showerror("Error", "Invalid input!")
        
        tk.Button(frame, text="Calculate", command=calculate_bitwise,
                 bg=self.colors["button"], fg=self.colors["fg"]).grid(row=3, column=0, 
                                                                       columnspan=2, pady=5)
    
    def show_ascii_window(self):
        ascii_win = tk.Toplevel(self.root)
        ascii_win.title("ASCII Converter")
        ascii_win.geometry("500x300")
        ascii_win.configure(bg=self.colors["bg"])
        
        tk.Label(ascii_win, text="📝 ASCII Converter", font=("Arial", 16, "bold"),
                bg=self.colors["bg"], fg=self.colors["fg"]).pack(pady=10)
        
        frame = tk.Frame(ascii_win, bg=self.colors["accent"])
        frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        tk.Label(frame, text="Enter Text:", bg=self.colors["accent"], 
                fg=self.colors["fg"]).pack()
        text_entry = tk.Entry(frame, width=40)
        text_entry.pack(pady=5)
        
        result_text = tk.Text(frame, height=10, width=50, bg=self.colors["bg"], 
                             fg=self.colors["fg"])
        result_text.pack(pady=10)
        
        def convert_ascii():
            text = text_entry.get()
            result_text.delete(1.0, tk.END)
            
            result_text.insert(tk.END, "ASCII Values (Decimal):\n")
            result_text.insert(tk.END, " ".join([str(ord(c)) for c in text]) + "\n\n")
            
            result_text.insert(tk.END, "Binary:\n")
            result_text.insert(tk.END, " ".join([bin(ord(c))[2:].zfill(8) for c in text]) + "\n\n")
            
            result_text.insert(tk.END, "Hexadecimal:\n")
            result_text.insert(tk.END, " ".join([hex(ord(c))[2:].upper() for c in text]))
        
        tk.Button(frame, text="Convert", command=convert_ascii,
                 bg=self.colors["button"], fg=self.colors["fg"]).pack(pady=5)
    
    def show_help(self):
        help_text = """
        HOW TO USE:
        
        1. Choose an operation (Convert, Add, Subtract, etc.)
        2. Enter your numbers
        3. Select the input and output bases
        4. Click CALCULATE
        5. View results in multiple formats
        
        FEATURES:
        - Convert between Binary, Octal, Decimal, Hexadecimal
        - Arithmetic operations in any base
        - Step-by-step explanations
        - View all base representations
        - Save/Load calculation history
        - Bitwise operations tool
        - ASCII converter tool
        - Dark/Light theme toggle
        """
        messagebox.showinfo("Help", help_text)
    
    def show_about(self):
        about_text = """
        Advanced Number System Calculator
        Version 2.0
        
        A comprehensive tool for number base conversions
        and arithmetic operations.
        
        Created for educational and professional use.
        """
        messagebox.showinfo("About", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberSystemCalculator(root)
    root.mainloop()
