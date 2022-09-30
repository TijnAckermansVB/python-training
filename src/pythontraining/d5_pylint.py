"""
This is an exercise to get familiar with Pylint.

You can install pylint with:
pip install pylint

To use pylint, run the following in the terminal/commandline:
pylint pylint_exercise.py
"""


def main():
    """Asks for name."""
    name = input("What is your name? ")
    greet(name)


def greet(name):
    """Aks how a person is doing given a name """
    print(f"Hello {name}, how are you?" )


def make_percentage(number):
    """Calculates percentage given number"""
    percentage = number / 100
    return f'{percentage}%'


if __name__ == "__main__":
    main()
