Installation

To install the foo_param package, navigate to the directory containing setup.py and run:

sh

pip install .

This will install the package and its dependencies listed in requirements.txt.
Basic Usage

The primary functionality of the foo_param package is to calculate the volume of a sphere given its radius. Below is an example of how to use the calculate_volume function.
Example 1: Calculating the Volume of a Sphere

python

from foo_param.core import calculate_volume

# Define the radius of the sphere
radius = 5

# Calculate the volume
volume = calculate_volume(radius)

# Print the result
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")

Running Example Scripts

We have included example scripts in the examples directory. These scripts demonstrate how to use the package in different scenarios.
Example 2: Calculating Volumes for Multiple Radii

python

# example1.py

from foo_param.core import calculate_volume

def main():
    # Example radius values
    radii = [1, 3, 5, 7]

    # Calculate and print the volume for each radius
    for radius in radii:
        volume = calculate_volume(radius)
        print(f"The volume of a sphere with radius {radius} is {volume:.2f}")

if __name__ == "__main__":
    main()

Run this script with:

sh

python examples/example1.py

Example 3: User Input for Radius

python

# example2.py

from foo_param.core import calculate_volume

def main():
    # Prompt the user to enter the radius of the sphere
    radius = float(input("Enter the radius of the sphere: "))

    try:
        # Calculate the volume of the sphere
        volume = calculate_volume(radius)
        print(f"The volume of a sphere with radius {radius} is {volume:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

Run this script with:

sh

python examples/example2.py

Error Handling

The calculate_volume function will raise a ValueError if the radius provided is negative. Ensure to handle this exception in your code:

python

from foo_param.core import calculate_volume

try:
    volume = calculate_volume(-5)
except ValueError as e:
    print(f"Error: {e}")

Contribution

We welcome contributions to the foo_param package. Please refer to the CONTRIBUTING.md file in the .github directory for guidelines on how to contribute.
License

This project is licensed under the MIT License. See the LICENSE file for details.