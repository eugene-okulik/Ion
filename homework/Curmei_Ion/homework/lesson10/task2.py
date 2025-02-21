def repeat_n_decorator(count=1):
    def repeat_me(func):
        """
        created a decorator which executing function count times
        :param func:
        :return:
        """

        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return repeat_me


@repeat_n_decorator(count=2)
def print_me(text):
    print(text)


print_me('print me')


# or

def repeat(func):
    def wrapper(*args, count=1, **kwargs):
        for _ in range(count):
            func(*args, **kwargs)

    return wrapper


@repeat
def scan_anything(text):
    print(text)


scan_anything("scan me", count=2)
