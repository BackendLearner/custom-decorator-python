from decorators import uppercase_output, bold_output, repeat_output

@uppercase_output
def greet(name):
    return f"Hello, {name}!"


@bold_output
def welcome(name):
    return f"Welcome, {name}!"


@repeat_output(3)
def message():
    return "Python is easy!"


name = input("Enter your name: ")

print(greet(name))
print(welcome(name))
print(message())
