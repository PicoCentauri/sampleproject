def add_one(number):
    return number + 1


def subtract_one(number):
    return number - 1


def inverse(number):
<<<<<<< HEAD
    """
    Takes the inverse of the number

    Parameters
    ----------

    number : float
        An arbitrary number.

    Returns
    ----------
    inverse of function : float

    """
    return 1 / number
=======
    if number == 0:
        raise ZeroDivisionError("For inverting `number` must be non zero!")
    return 1 // number
>>>>>>> main
