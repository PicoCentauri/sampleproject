def add_one(number):
    return number + 1


def subtract_one(number):
    return number - 1


def inverse(number):
    """
    Returns inverse of number

    number : int
    return : inverse of number
    """
    if number == 0:
        raise ZeroDivisionError("For inverting `number` must be non zero!")
    return 1 / number
