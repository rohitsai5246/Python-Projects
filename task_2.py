import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        age = int(age_entry.get())

        if weight <= 0 or height <= 0 or age <= 0:
            messagebox.showerror("Error", "Please enter valid positive values!")
            return
        
        bmi = round(weight / (height ** 2), 2)
        category = classify_bmi(bmi, age)

        result_label.config(text=f"Your BMI: {bmi}\nHealth Status: {category}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values!")

def classify_bmi(bmi, age):
    if age <= 18:
        ranges = [(18.5, "Underweight"), (24.9, "Normal"), (29.9, "Overweight"), (float('inf'), "Obese")]
    elif age <= 34:
        ranges = [(19, "Underweight"), (25, "Normal"), (30, "Overweight"), (float('inf'), "Obese")]
    elif age <= 50:
        ranges = [(20, "Underweight"), (26, "Normal"), (31, "Overweight"), (float('inf'), "Obese")]
    else:
        ranges = [(21, "Underweight"), (27, "Normal"), (32, "Overweight"), (float('inf'), "Obese")]

    for limit, category in ranges:
        if bmi <= limit:
            return category
    return "Obese"

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Enter Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Height (cm):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Age:").grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, columnspan=2, pady=10)

root.mainloop()
