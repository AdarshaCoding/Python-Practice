class Calculator:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


def main():
    c1 = Calculator(10, 5)
    c2 = Calculator(20, 10)

    print("Addition: " + str(c1.add()))
    print("Subtraction: " + str(c1.sub()))
    print("Multiply: " + str(c1.mul()))
    print("Division: " + str(c1.divide()))

    print("Addtion from Object2: " + str(c2.add()))


if __name__ == "__main__":
    main()
