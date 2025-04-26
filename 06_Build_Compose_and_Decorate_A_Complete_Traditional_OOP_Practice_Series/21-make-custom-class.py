class Countdown:
    def __init__(self, start):
        self.start = start  # Starting number for countdown
        self.current = start  # Initialize current to start

    def __iter__(self):
        return self  # Return the iterable object itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop iteration when countdown reaches 0
        self.current -= 1
        return self.current + 1  # Return the current value before decrementing

# Example usage
countdown = Countdown(5)

# Using the Countdown class in a for-loop
for number in countdown:
    print(number)
