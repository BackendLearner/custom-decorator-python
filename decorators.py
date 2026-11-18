
from functools import wraps

def uppercase_output(func):

    @wraps(func)
    def wrapper(*args):
        result = func(*args)

        if isinstance(result, str):
            return result.upper()

        return result

    return wrapper


def wrap_string(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        if isinstance(result, str):
            return f"**{result}**"

        return result

    return wrapper

# 3. Repeat decorator
def repeat_output(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            return [result for _ in range(times)]

        return wrapper

    return decorator