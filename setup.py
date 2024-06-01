# setup.py
from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='foo_param',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,  # Read dependencies from requirements.txt
    entry_points={
        'console_scripts': [
            'foo-calc=foo_param.core:calculate_volume',
        ],
    },
    author='Mitchell Creelman',
    author_email='mitchcreelman@gmail.com.com',
    description='A package designed to calculate the Foo et al. parameterization.',
    url='https://github.com/mcreelma/foo_param',
)
