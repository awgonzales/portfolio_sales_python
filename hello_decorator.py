# Defining a decorator
def my_decorator(func):
    def wrapper():
        print("This works before the function")
        func()
        print("This works after the function")
    return wrapper

@my_decorator
def say_hello():
    """
    say hello
    """
    print("Hello")
@my_decorator
def say_goodbye():
    """
    say goodbye
    """
    message = "Goodbye"
    return message
    
    
if __name__ == "__main__""":
    say_hello()
    print(say_goodbye)
