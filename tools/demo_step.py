#!/usr/bin/env python3
"""
Example usage of the ODrive python library to monitor and control ODrive devices
"""

import odrive.core
import time
import math

# Find a connected ODrive (this will block until you connect one)
my_drive = odrive.core.find_any(consider_usb=True, consider_serial=False, printer=print)

# my_drive = odrive.core.open_serial("/dev/tty.usbmodem1421", printer=print)

# The above call returns a python object with a dynamically generated type. The
# type hierarchy will correspond to the endpoint list in `MotorControl/protocol.cpp`.
# You can also inspect the object using the dir-function:
#print(dir(my_drive))
#print(dir(my_drive.motor0))
# TODO: maybe provide an introspection method that dumps the whole type hierarchy at once

# To read a value, simply read the property
print("Bus voltage is " + str(my_drive.vbus_voltage) + "V")

# And this is how function calls are done:
my_drive.motor0.set_pos_setpoint(0.0, 0.0, 0.0)
time.sleep(1.0)

# A little sine wave to test
t0 = time.monotonic()
current_time = t0
last_time = t0
mysum = 0

my_drive.motor0.set_pos_setpoint(2000.0, 0.0, 0.0)

time_steps = 400

for x in range(1, time_steps):
    current_time = time.monotonic()
    mysum += (current_time - last_time)
    last_time = current_time
    
    position = my_drive.motor0.encoder.pll_pos
    #print("position: " + str(my_drive.motor0.encoder.pll_pos))
    #time.sleep(0.01)

print(str(mysum/time_steps))
# Some more things you can try:

# Write to a read-only property:
#my_drive.vbus_voltage = 11.0  # fails with `AttributeError: can't set attribute`

# Assign an incompatible value:
#my_drive.motor0.pos_setpoint = "I like trains"  # fails with `ValueError: could not convert string to float`
