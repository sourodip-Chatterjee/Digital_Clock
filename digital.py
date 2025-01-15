import tkinter as tk
from time import strftime

# Function to update the time display
def update_time():
    current_time = strftime('%H:%M:%S')  # Format: HH:MM:SS 
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1 second

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x100")
root.resizable(False, False)

# Set up the clock display
label = tk.Label(root, font=("Helvetica", 48), background="black", foreground="cyan")
label.pack(expand=True)

# Start the clock
update_time()

# Run the application
root.mainloop()
