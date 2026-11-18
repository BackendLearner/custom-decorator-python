
from decorators import uppercase_output, wrap_string, repeat_output

def test_uppercase_output():
    @uppercase_output
    def greet(name):
        return f"Hello, {name}!"

    assert greet("Swati") == "HELLO, SWATI!"



def test_bold_output():

    @wrap_string
    def greet(name):
        return f"Hello, {name}!"

    assert greet("Swati") == "**Hello, Swati!**"


# Testing repeat_output
def test_repeat_output():

    @repeat_output(3)
    def greet():
        return "Hello!"

    assert greet() == ["Hello!", "Hello!", "Hello!"]




