import tkinter as tk
from time import strftime

# Function to update the time and date display
def update_time():
    current_time = strftime('%H:%M:%S')  # Time in HH:MM:SS format
    current_date = strftime('%A, %d %B %Y')  # Day, Date Month Year format
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)  # Update every 1 second

# Create the main application window
root = tk.Tk()
root.title("Digital Clock with Date")
root.geometry("600x200")  # Adjusted size for better visibility
root.resizable(False, False)
root.configure(background="black")

# Set up the time display
time_label = tk.Label(
    root,
    font=("Helvetica", 60),
    background="Black",
    foreground="cyan"
)
time_label.pack(pady=10)

# Set up the date display
date_label = tk.Label(
    root,
    font=("Helvetica", 30),
    background="black",
    foreground="light green"
)
date_label.pack(pady=5)

# Start the clock
update_time()

# Run the application
root.mainloop()
