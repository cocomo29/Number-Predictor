import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def update_loading_text_and_progress(step):
    if step == 0:
        loading_text.config(text="Analyzing brain waves...")
    elif step == 25:
        loading_text.config(text="Scanning memories...")
    elif step == 50:
        loading_text.config(text="Calculating probabilities...")
    elif step == 75:
        loading_text.config(text="Decoding thoughts...")

    if step < 100:
        loading_window.after(1000, update_loading_text_and_progress, step + 25)
    else:
        loading_window.destroy()
        showinfo("Prediction Result", f"You predicted: {user_input.get()}")

def predict_number():
    try:
        user_val = int(user_input.get())
        if 1 <= user_val <= 10:
            global loading_window, loading_text
            loading_window = tk.Toplevel(root)
            loading_window.title("Prediction in Progress")
            loading_text = tk.Label(loading_window, text="Loading...", font=("Helvetica", 12))
            loading_window.geometry("300x129")
            loading_text.pack(pady=20)
            
            # Center the loading window on the screen
            loading_window.update_idletasks()
            loading_window.geometry(f"{loading_window.winfo_width()}x{loading_window.winfo_height()}+{229}+{160}")
            
            loading_window.after(0, update_loading_text_and_progress, 0)
            
            progress = ttk.Progressbar(loading_window, mode="indeterminate", length=200, maximum=25)
            progress.pack(pady=10)
            progress.start()
        else:
            showinfo("Warning", "Please choose a number between 1 and 10")
    except ValueError:
        showinfo("Error", "Something went wrong. Please enter a valid number between 1 and 10.")

root = tk.Tk()
root.title("Number Predictor")

label = tk.Label(root, text="Enter a number between 1 and 10:")
label.pack(pady=20)

user_input = tk.Entry(root)
user_input.pack(pady=10)

predict_button = tk.Button(root, text="Predict", command=predict_number)
predict_button.pack(pady=10)

# Center the main window on the screen
root.update_idletasks()
x_offset = (root.winfo_screenwidth() - 270) // 2
y_offset = (root.winfo_screenheight() - 150) // 2
root.geometry(f"{270}x{150}+{x_offset}+{y_offset}")
root.resizable(False, False)

root.mainloop()
