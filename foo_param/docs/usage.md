# Basic Usage

The primary functionality of the foo_param package is to calculate the volume of a sphere given its radius. This is currently performed with the calculate_volume function, the usage of which will be outlined in this document

## Example: Calculating the Volume of a Sphere
This outlines the body of a python script for testing a given radius of a sphere. This is the same sample from the initial readme
```py

from foo_param.core import calculate_volume

# Define the radius of the sphere
radius = 5

# Calculate the volume
volume = calculate_volume(radius)

# Print the result
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")

```

# Running Example Scripts

We have included example scripts in the examples directory. These scripts further demonstrate how to use the package in different scenarios.

# example1.py

This script calculates the foo parameter for multiple radii inputs. The results of these calculations is then sent to the terminal. The body of the example script is as follows:

```py
# Import the calculate_volume function from the core module
from foo_param.core import calculate_volume

# list of radii values
radii = [1, 3, 5, 7]

# Calculate and print the volume for each radius
for radius in radii:
    volume = calculate_volume(radius)
    print(f"The volume of a sphere with radius {radius} is {volume:.2f}")
```

This script can be run with the following command:

```sh
python example1.py
```

# example2.py
This script calculates the foo parameter for a user-determined radius input. The result of which is displayed in the terminal. The body of the example script is as follows:

```py
from foo_param.core import calculate_volume

radius = float(input("Enter the radius of the sphere: "))

try:
    # Calculate the volume of the sphere
    volume = calculate_volume(radius)
    print(f"The volume of a sphere with radius {radius} is {volume:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
# Error Handling

The calculate_volume function will raise a ValueError if the radius provided is negative in order to prevent illogical results from input values.