# Task 1: CountDown Iterator

class CountDown:

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The object is its own iterator

    def __next__(self):
        if self.current > 0:
            value = self.current
            self.current -= 1  # Decrease by 1 for the next iteration
            return value
        else:
            raise StopIteration  # Stop when reaching 0


if __name__ == '__main__':
    for i in CountDown(5):
        print(i)