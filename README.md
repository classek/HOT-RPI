This script is a door monitor application that can be run on a computer with Python and the GPIO library. 
The script uses three sensors connected to GPIO pins on a Raspberry Pi to measure the Hold Open Time (HOT) of a door.
The sensors are placed at the closed, open and door stop positions of the door, and the script records the time stamps when the door starts to open, when the door is fully open, when the door performs drift compensation and when the door returns to the fully open position.

The application also includes a GUI where a measurement can be started and the expected HOT can be set. 
The expected HOT is compared to the actual HOT and a Pass/Fail result is displayed. 
The script logs all events with time stamps since the measurement started, and the log can be used to observe the door's performance over time.

The script requires Python 3 and the RPi.GPIO library to be installed on the Raspberry Pi. 
The script has been tested and found to have an accuracy of 0.1s and the ability to measure the HOT for at least 24 hours. 
The script is easy to set up and get results from, and can easily be adapted for use with double doors by adding an additional set of sensors.


*HOT = Hold Open Time 

