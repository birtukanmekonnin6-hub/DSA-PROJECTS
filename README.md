# Functional Analog Clock 🕒

## Project Description

This project is a functional analog clock developed using Python's built-in Turtle graphics library.

The clock displays the current time using three hands: hour, minute, and second hands. It also displays the digital time and current date. The clock updates automatically to keep the displayed time accurate.

The project also includes additional features such as pause and resume functionality and timezone selection.

## Features

- **Analog Clock:** Displays hour, minute, and second hands.
- **Clock Face:** Includes 12 hour numbers, minute markings, and hour markings.
- **Digital Time:** Displays the current time in 12-hour format with AM/PM.
- **Date Display:** Shows the current day, month, and year.
- **Automatic Updates:** Updates the clock every second.
- **Pause and Resume:** Allows users to pause and resume the clock.
- **Timezone Selection:** Allows users to change the displayed timezone.
- **Custom Design:** Uses different colors and hand sizes to make the clock easy to read.

## Technologies Used

- Python
- Turtle Graphics
- Datetime Module
- Math Module
- ZoneInfo Module

## Requirements

- Python 3.9 or later.
- A computer that supports Python Turtle graphics.

**Note:** On some Windows installations, the `tzdata` package may be required for timezone support.

Install it using:

```bash
pip install tzdata
```

## How to Run the Project

1. Make sure Python is installed on your computer.
2. Download or clone this project.
3. Open the project folder in VS Code or another Python editor.
4. Run the following command in the terminal:

```bash
python analog_clock.py
```

5. The analog clock window will appear and start displaying the current time.

## Keyboard Controls

| Key | Function |
|---|---|
| Space | Pause or resume the clock |
| Z | Change the timezone |

### Available Timezones

The following timezones are provided as examples:

- `Africa/Addis_Ababa`
- `Europe/London`
- `Asia/Tokyo`
- `America/New_York`

When you press **Z**, enter one of the timezone names in the dialog box.

## Project Structure

```text
Functional-Analog-Clock/
│
├── analog_clock.py
└── README.md
```

## Learning Objectives

Through this project, I practiced:

- Using Python functions to organize a program.
- Working with the Turtle graphics library.
- Understanding coordinate systems and angles.
- Using mathematical calculations to position clock hands.
- Working with Python's datetime module.
- Using timers to update a graphical application.
- Handling keyboard events and user input.
- Working with timezones using the ZoneInfo module.

## Author

Developed as a Python programming assignment.