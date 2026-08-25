# Task 2: Even Numbers Generator

def evens_up_to(n):
    current = 2
    while current <= n:
        yield current
        current += 2

if __name__ == '__main__':
    for x in evens_up_to(10):
        print(x)