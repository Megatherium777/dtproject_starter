import numpy as np
import os


# example of printing a message
# message = "\nHello World!\n"
# print(message)


# example of using an import
# dependencies add in .txt files
# print(np.add(3, 5))

# running a project on the robot
vehicle_name = os.environ['VEHICLE_NAME']
message = f"\nHello from {vehicle_name}!\n"
print(message)
