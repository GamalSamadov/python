from importlib.metadata import entry_points
from setuptools import setup

setup(
    name="taskaty",
    version='0.1.0',
    description='A simple command-line task app written by Python',
    author='Jamal Kamal',
    install_requires=['tabulate'],
    entry_points={
        'console_scripts': [
            'taskaty=taskaty:main'
        ],
    },
)
