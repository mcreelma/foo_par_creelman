# The goal of this example script is to illustrate a use case  for the calculate_volume function from the foo_param module. 
# The script defines a list of radii values and calculates the volume of a sphere for each radius using the calculate_volume function. 
# The results are then printed to the console.

# Import the calculate_volume function from the core module
from foo_param.core import calculate_volume

# Define the main function
def main():
    # list of radii values
    radii = [1, 3, 5, 7]

    # Calculate and print the volume for each radius
    for radius in radii:
        volume = calculate_volume(radius)
        print(f"The volume of a sphere with radius {radius} is {volume:.2f}")

# Call the main function
if __name__ == "__main__":
    main()
