import random


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


def random_numbers(count, start, end):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(start, end))
    return numbers


def main():
    obj = MyClass(10, 20)
    print(f"Initial values: x = {obj.get_x()}, y = {obj.get_y()}")
    obj.set_x(30)
    obj.set_y(40)
    print(f"Updated values: x = {obj.get_x()}, y = {obj.get_y()}")

    random_count = 10
    random_start = 1
    random_end = 100
    print(
        f"Generating {random_count} random numbers between {random_start} and {random_end}:"
    )
    numbers = random_numbers(random_count, random_start, random_end)
    print(numbers)


if __name__ == "__main__":
    main()
