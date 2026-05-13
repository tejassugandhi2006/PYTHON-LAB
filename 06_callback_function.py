# Program demonstrating callback function

def greet(name):
    return f"Hello, {name}"

def process_user(callback, name):
    print(callback(name))

process_user(greet, "Ashu")
