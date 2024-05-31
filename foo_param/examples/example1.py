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
