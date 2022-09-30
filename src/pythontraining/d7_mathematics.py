"""
Simple math functions
"""
import math


def multiply(x, y):
    return x * y


def divide(x, y):
    return round(x / y, 1)


def round_up(x):
    rounded = math.ceil(x)
    return rounded


def hypotenuse(a, b):
    return (a**2 + b**2)**0.5


def count_registrations(registrations):
    return len(registrations)


def create_attendee_list(registrations):
    return [f"{x['first_name']} {x['last_name']}" for x in registrations]
