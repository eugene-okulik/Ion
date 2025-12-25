def finish_me(func):
    """
    created a decorator
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        # print(f"function {func.__name__} is started")
        res = func(*args, **kwargs)
        print(f"function {func.__name__} is finished")
        return res

    return wrapper


@finish_me
def example(text):
    print(text)


example("print me")
