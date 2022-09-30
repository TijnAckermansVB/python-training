"""
Rename the following variables and function names
"""


def rename_variables_in_this_function():
    # 1
    first_name = input("What is your first name? ")

    # 2
    last_name = "Johnson"

    # 3
    movie_title = "Pulp Fiction"

    # 4
    operating_system = ["Windows", "Linux", "MacOS"]

    # 5
    actors = ["Tom Hanks", "Brad Pitt", "Johnny Depp"]

    # 6
    fruits = ["apple", "banana", "kiwi", "orange"]

    # 7
    grades = {"English": 90, "Biology": 80, "Math": 100}


# Rename this function and its variables
def convert_celsius_to_fahrenheit(celsius):
    """Return temperature converted from Celsius to Fahrenheit"""
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


# Rename this class
class ElectricVehicle:
    """
    A class to define electric vehicles.
    """
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery


"""
Add 'docstrings' to the following functions and classes.
Make sure to follow the Python conventions.
"""


# 1
def square(n):
    """
    Returns the square of n.
    :param n: int
    :return: n**2
    """
    return n * n


# 2
def count_vowels(word):
    """
    Returns the number of vowels in word.
    :param word: str
    :return: number of vowels
    """
    number_of_vowels = 0
    for char in word.lower():
        if char in "aeiou":
            number_of_vowels += 1
    return number_of_vowels


# 3
class Dog:
    """
    A class to represent a dog.
    """

    def __init__(self, name):
        self.name = name

    def bark(self):
        """
        Prints dog name together with say whoof!
        """
        print(f"{self.name} says whoof!")
