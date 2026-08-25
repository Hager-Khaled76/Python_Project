# Task 4: Call Counter Decorator

def call_counter(func):

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0  # Initialize count attribute on the wrapper
    return wrapper

# --- Testing with Decorator ---
@call_counter
def greet(name):
    return "Hello " + name

if __name__ == '__main__':
    print(greet("Ali"))
    print(greet("Sara"))
    print(greet("Omar"))

    print(f"Total calls = {greet.count}")