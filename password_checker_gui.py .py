import tkinter as tk


def check_strength(event=None):
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in "!@#$%^&*()-_+=" for char in password):
        score += 1

    # Strength and color logic
    if score <= 2:
        strength_text = "Weak ❌"
        color = "red"
    elif score <= 4:
        strength_text = "Medium ⚠️"
        color = "orange"
    else:
        strength_text = "Strong ✅"
        color = "green"

    result_label.config(
        text=f"Strength: {strength_text}\nScore: {score}/5",
        fg=color
    )


# Main window
app = tk.Tk()
app.title("Secure Password Analyzer")
app.geometry("350x250")
app.resizable(False, False)

# Title
title_label = tk.Label(app, text="Password Strength Checker", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Password entry
entry = tk.Entry(app, show="*", width=25, font=("Arial", 12))
entry.pack(pady=10)

# Live update binding (THIS enables real-time checking)
entry.bind("<KeyRelease>", check_strength)

# Result label
result_label = tk.Label(app, text="Start typing your password...", font=("Arial", 12))
result_label.pack(pady=15)

# Run app
app.mainloop()
