import re


def is_valid_isbn(isbn):
    """
    Performs a more detailed ISBN validation.
    :param isbn: ISBN to validate.
    :return: Boolean indicating if ISBN is valid.

    Though i have just putten a simple algo to check the isbn for simplisity
    """

    if len(isbn) > 9:
        return True
    # Simplified version; real validation would be more complex
    # return bool(re.match(r"^\d{10}(\d{3})?$", isbn))


def is_valid_email(email):
    """
    Uses a regular expression to check if the provided email is valid.
    :param email: Email to validate.
    :return: Boolean indicating if email is valid.
    """
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))


def is_non_empty_string(s):
    """
    Checks if the provided string is non-empty.
    :param s: String to check.
    :return: Boolean indicating if string is non-empty.
    """
    return isinstance(s, str) and bool(s.strip())


def is_positive_integer(number):
    """
    Validates if the provided input is a positive integer.
    :param number: Input to validate.
    :return: Boolean indicating if the input is a positive integer.
    """
    return str(number).isdigit() and int(number) > 0
