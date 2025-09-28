import tkinter as tk
from tkinter import ttk
from math import sqrt, sin, cos, tan, radians, pow, log, log10, factorial, pi, e

# ----------------- Functions -----------------
def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        result = sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def trig_function(func):
    try:
        angle = radians(float(entry.get()))
        if func == "sin":
            result = sin(angle)
        elif func == "cos":
            result = cos(angle)
        elif func == "tan":
            result = tan(angle)
        entry.delete(0, tk.END)
        entry.insert(0, str(round(result, 5)))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def power():
    try:
        value = entry.get().split("^")
        if len(value) == 2:
            result = pow(float(value[0]), float(value[1]))
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        else:
            entry.insert(tk.END, "^")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def log_function(base=10):
    try:
        num = float(entry.get())
        result = log10(num) if base == 10 else log(num)
        entry.delete(0, tk.END)
        entry.insert(0, str(round(result, 5)))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def factorial_func():
    try:
        num = int(entry.get())
        result = factorial(num)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ----------------- GUI -----------------
root = tk.Tk()
root.title("⚡ Advanced Scientific Calculator")
root.geometry("430x650")
root.config(bg="#1e1e2f")



style = ttk.Style()
style.configure("TButton",
                font=("Arial", 14, "bold"),
                padding=10,
                relief="flat",
                background="#333",
                foreground="white")

# Entry box

entry = tk.Entry(root, font=("Arial", 22), borderwidth=5, relief="ridge", justify="right", bg="#2d2d3a", fg="white")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=15, ipady=15, sticky="nsew")
# Add your name at top-right
name_label = tk.Label(root, text="Ravi Chouksey", font=("Arial", 12, "bold"),
                      bg="#1e1e2f", fg="#00cec9", anchor="e")
name_label.grid(row=0, column=0, columnspan=5, sticky="ne", padx=10, pady=5)

# Buttons layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("⌫", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("√", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("^", 4, 4),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3), ("ln", 5, 4),
    ("π", 6, 0), ("e", 6, 1), ("!", 6, 2), ("(", 6, 3), (")", 6, 4)
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, bg="#7ac4b5", fg="white", font=("Arial", 16, "bold"),
                  command=evaluate).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text == "C":
        tk.Button(root, text=text, bg="#c28080", fg="white", font=("Arial", 16, "bold"),
                  command=clear).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text == "⌫":
        tk.Button(root, text=text, bg="#857559", fg="black", font=("Arial", 16, "bold"),
                  command=backspace).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text == "√":
        tk.Button(root, text=text, bg="#566c7e", fg="white", font=("Arial", 16, "bold"),
                  command=square_root).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text == "^":
        tk.Button(root, text=text, bg="#857eb6", fg="white", font=("Arial", 16, "bold"),
                  command=power).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text in ["sin", "cos", "tan"]:
        tk.Button(root, text=text, bg="#7ab4b3", fg="black", font=("Arial", 16, "bold"),
                  command=lambda t=text: trig_function(t)).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text == "log":
        tk.Button(root, text=text, bg="#927069", fg="black", font=("Arial", 16, "bold"),
                  command=lambda: log_function(10)).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text == "ln":
        tk.Button(root, text=text, bg="#8a5b5b", fg="white", font=("Arial", 16, "bold"),
                  command=lambda: log_function("e")).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text == "!":
        tk.Button(root, text=text, bg="#477a6c", fg="black", font=("Arial", 16, "bold"),
                  command=factorial_func).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text == "π":
        tk.Button(root, text=text, bg="#c9bc92", fg="black", font=("Arial", 16, "bold"),
                  command=lambda: button_click(str(pi))).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    elif text == "e":
        tk.Button(root, text=text, bg="#9994db", fg="white", font=("Arial", 16, "bold"),
                  command=lambda: button_click(str(e))).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    else:
        tk.Button(root, text=text, bg="#bad3da", fg="white", font=("Arial", 16, "bold"),
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

# Auto expand rows/columns
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
