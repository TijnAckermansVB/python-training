# Exercise 1
try:
    print(undefined_variable)
except NameError:
    print("The variable is not defined")


# Exercise 2
try:
    with open('no_file.txt') as f:
        text = f.read()
except FileNotFoundError:
    print("The file could not be found")


# Exercise 3
try:
    ingredients = ["spam", "ham", "eggs"]
    print(ingredients[9])
except IndexError:
    print("The index exceeds the number of items in the list")
except NameError:
    print("The index variable does not exists")
except TypeError:
    print("The index is not an integer")
except Exception as error:
    print("Unexpected error:", error)


class InvalidEmailError(Exception):
    """Custom exception for invalid email addresses"""


def set_email_address(email):
    if "@" not in email:
        raise InvalidEmailError("Not a valid e-mail address")


try:
    set_email_address("john-at-example.com")
except InvalidEmailError:
    print("Please provide a valid e-mail address")
