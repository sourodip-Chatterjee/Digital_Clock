# Digital Clock with Date

This project is a simple **digital clock** with an integrated **date and day display**, built using Python and the `tkinter` library. The clock updates in real-time and provides a clean graphical interface.

---

## Features

- Displays the current **time** in `HH:MM:SS` format.
- Shows the current **day** and **date** in `Day, DD Month YYYY` format.
- Real-time updates every second.
- Simple and responsive GUI with customizable fonts and colors.

---

## Requirements

To run this application, ensure you have the following installed:

- **Python 3.7+**
- The `tkinter` library (bundled with most Python installations)

---

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/digital-clock-with-date.git
   cd digital-clock-with-date
   ```

2. Run the Python script:
   ```bash
   python digital_clock.py
   ```

3. The clock window will open, displaying the current time and date.

---

## Code Overview

### Key Components

- **Time and Date Formatting**:
  - Time: `strftime('%H:%M:%S')` (e.g., `20:45:32`)
  - Date: `strftime('%A, %d %B %Y')` (e.g., `Monday, 1 January 2023`)

- **Labels**:
  - `time_label`: Displays the current time with a large font size.
  - `date_label`: Displays the current day and date below the time.

- **Real-time Updates**:
  - The `update_time()` function updates the clock every second using `after(1000, update_time)`.

### GUI Design

- **Background**: Black (`#000000`)
- **Time Font**: Cyan (`#00FFFF`), `Helvetica`, size 60.
- **Date Font**: Light Green (`#90EE90`), `Helvetica`, size 30.
- **Window Dimensions**: 600x200 pixels.

---

## Screenshot

![Digital Clock Screenshot](https://via.placeholder.com/600x200.png?text=Digital+Clock+Example)

---

## Future Enhancements

- Add an **alarm feature** to notify users at a specific time.
- Include **time zone selection** for global users.
- Add options to customize colors and fonts through a settings menu.

---

