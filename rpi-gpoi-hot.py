import RPi.GPIO as GPIO
import time
import tkinter as tk
from tkinter import Label

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the sensors
closed_sensor_pin = 23
open_sensor_pin = 24
door_stop_sensor_pin = 25

# Define the expected hold open time
expected_hold_open_time = 24 # hours

# Initialize the GPIO pins for the sensors as inputs
GPIO.setup(closed_sensor_pin, GPIO.IN)
GPIO.setup(open_sensor_pin, GPIO.IN)
GPIO.setup(door_stop_sensor_pin, GPIO.IN)

# Define the function for measuring hold open time
def measure_hold_open_time():
    start_time = time.time()
    hold_open_time = 0

    # Check if the door is closed
    if GPIO.input(closed_sensor_pin) == 1:
        status_label.config(text="Door is closed.")
        while hold_open_time < expected_hold_open_time:
            # Check if the door is open
            if GPIO.input(open_sensor_pin) == 1:
                open_time = time.time()
                # Check if the door has hit the door stop
                while GPIO.input(door_stop_sensor_pin) == 0:
                    pass
                door_stop_time = time.time()
                drift_compensation_time = door_stop_time - open_time
                hold_open_time = door_stop_time - start_time
                status_label.config(text="Hold Open Time: " + str(hold_open_time) + " seconds.")
                # Repeat every 6 hours
                time.sleep(6 * 3600 - drift_compensation_time)
            else:
                # Check if the door has closed
                if GPIO.input(closed_sensor_pin) == 0:
                    hold_open_time = time.time() - start_time
                    status_label.config(text="Hold Open Time: " + str(hold_open_time) + " seconds.")
                    break
                else:
                    time.sleep(0.1)
    else:
        status_label.config(text="Door is open.")

# Initialize the GUI
root = tk.Tk()
root.title("Hold Open Time Measurement")

status_label = Label(root, text="Press Start to begin measurement.")
status_label.pack()

start_button = tk.Button(root, text="Start", command=measure_hold_open_time)
start_button.pack()

# Start the GUI
root.mainloop()

