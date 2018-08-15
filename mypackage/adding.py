def add(a, b):
    return a + b


def add_with_exception(a, b):
    if a > 0 and b > 0:
        return add(a, b)

    raise ValueError