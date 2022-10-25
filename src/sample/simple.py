def add_one(number):
    return number + 1


def subtract_one(number):
    return number - 1


def inverse(number):
    """
    Divides numbers
    """
    if number == 0:
        raise ZeroDivisionError("For inverting `number` must be non zero!")

    return 1 // number
