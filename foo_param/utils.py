# foo_param/utils.py
def validate_radius(radius):
    """
    Validate that the radius is a non-negative number.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    bool: True if the radius is valid, else False.
    """
    return radius >= 0
