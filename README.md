# Foo Parameterization Package

Welcome to the documentation for the `foo_param` package, which provides a neat and tidy package to include calculations of the Foo et al. parameterization.

## Overview

The `foo_param` package is designed to compute the volume of a sphere given its radius using the methodology outlined by Foo et al. (2017). 

The core of the package centers around the following 

$$
V = \frac{4}{3} \pi r^3
$$

Where V is the Foo Parameter, and r is the input radius.

This package is intended to be a community project with the expectation of continuous development and contributions from various users over the years.

## Key Features

- **Simple API**: Easily calculate the volume of a sphere with a single function call.
- **Error Handling**: Gracefully handles invalid input, such as negative radius values.
- **Community-Driven**: Designed to be extended and improved by a wide range of contributors.

## Installation

The `foo_param` package, is designed to be easy to install in any python environment or manager. 
Simply activate your environment of choice and type:

```sh
pip install foo_param
```

Once the package has been installed, you can use any of the core functionalities in your python code

# Usage Sample
Here is a quick example of how to use the foo_param package for a python script:

```py
from foo_param import calculate_volume

# Define the radius of the sphere
radius = 5

# Calculate the volume
volume = calculate_volume(radius)

# Print the result
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")

```

For more detailed usage instructions and examples, please refer to the Usage Guide.


# Contributing 

Foo param is developed with a philosophy of open and continuous development. To this end, we have included best practices for contributing in the docs section of this package



# Getting Help

If you encounter any issues or have questions, feel free to open an issue on our GitHub repository.

This project is licensed under the MIT License. See the LICENSE file for details.
