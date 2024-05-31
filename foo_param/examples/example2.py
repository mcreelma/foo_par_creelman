# This script prompts the user to enter the radius of a sphere and calculates its volume.
# The calculate_volume function from the foo_param module is used to calculate the volume of the sphere.
# The user input is validated to ensure that the radius is a non-negative number.

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