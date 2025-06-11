import tkinter as tk
from tkinter import messagebox

def check_number():
    try:
        num = int(entry_number.get())
        if num > 7:
            messagebox.showinfo("Result", "Hello")
        else:
            messagebox.showinfo("Result", "The number is not greater than 7")
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")

def check_name():
    name = entry_name.get()
    if name == "John":
        messagebox.showinfo("Result", "Hello, John")
    else:
        messagebox.showinfo("Result", "There is no such name")

def check_array():
    try:
        raw_array = entry_array.get()
        array = [int(x.strip()) for x in raw_array.split(",")]
        multiples = [str(num) for num in array if num % 3 == 0]
        if multiples:
            messagebox.showinfo("Result", f"Multiples of 3: {', '.join(multiples)}")
        else:
            messagebox.showinfo("Result", "No multiples of 3 found")
    except ValueError:
        messagebox.showerror("Error", "Array must contain only numbers")


window = tk.Tk()
window.title("Task Window")
window.geometry("600x300")

#for number
tk.Label(window, text="1. Enter the number:").pack()
entry_number = tk.Entry(window)
entry_number.pack()
tk.Button(window, text="Check number", command=check_number).pack(pady=5)

# for name
tk.Label(window, text="2. Enter the name:").pack()
entry_name = tk.Entry(window)
entry_name.pack()
tk.Button(window, text="Check name", command=check_name).pack(pady=5)

# for array
tk.Label(window, text="3. Enter array (ex: 3,6,7):").pack()
entry_array = tk.Entry(window)
entry_array.pack()
tk.Button(window, text="Check array", command=check_array).pack(pady=5)
window.mainloop()
