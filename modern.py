import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

def predict_number():
    try:
        user_input = int(entry.get())
        if 1 <= user_input <= 10:
            loading_window = ctk.CTk()
            loading_window.title("Prediction in Progress")
            loading_window.geometry("300x129")

            root.update_idletasks()
            root_width = root.winfo_width()
            root_height = root.winfo_height()
            loading_x = 300 + (root_width - 300) // 2
            loading_y = 200 + (root_height - 129) // 2
            loading_window.geometry(f"300x129+{loading_x}+{loading_y}")

            loading_text = ctk.CTkLabel(loading_window, text="Loading...", font=("Helvetica", 16))
            loading_text.pack(pady=20)

            progress_bar = ctk.CTkProgressBar(loading_window)
            progress_bar.pack(pady=10)

            def update_loading_text_and_progress(step):
                if step <= 20:
                    loading_text.configure(text="Analyzing brain waves...")
                elif step <= 40:
                    loading_text.configure(text="Scanning memories...")
                elif step <= 60:
                    loading_text.configure(text="Calculating probabilities...")
                elif step <= 80:
                    loading_text.configure(text="Decoding thoughts...")

                progress = step / 100.0
                progress_bar.set(progress)

                if step < 100:
                    loading_window.update()
                    loading_window.after(100, update_loading_text_and_progress, step + 1)
                else:
                    loading_window.destroy()
                    try:
                        CTkMessagebox(title="Prediction Result", message=f"You are thinking of the number {user_input}", icon="check", width=300, height=190).show()
                    except:
                        pass
            update_loading_text_and_progress(0)

        else:
            try:
                CTkMessagebox(title="Warning", message="Please choose a number between 1 and 10", icon="warning", width=300, height=190).show()
            except:
                pass
    except ValueError:
        try:
            CTkMessagebox(title="Error", message="Something went wrong", icon="cancel", width=300, height=190).show()
        except:
            pass

root = ctk.CTk()
root.title("Number Predictor")


label = ctk.CTkLabel(root, text="Enter a number between 1 and 10:")
label.pack(pady=20)

entry = ctk.CTkEntry(root)
entry.pack(pady=10)

predict_button = ctk.CTkButton(root, text="Read my mind", command=predict_number)
predict_button.pack(pady=10)

# Center the main window on the screen
root.update_idletasks()
x_offset = (root.winfo_screenwidth() - 300) // 2
y_offset = (root.winfo_screenheight() - 190) // 2
root.geometry(f"{300}x{190}+{x_offset}+{y_offset}")
root.resizable(False, False)
root.mainloop()
