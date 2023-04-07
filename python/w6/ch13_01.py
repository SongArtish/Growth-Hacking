# Calculator

class Calculator:
    def __init__(self, n1, n2):
        print('\n===__init--() START ===')
        self.num1 = n1
        self.num2 = n2

    def add(self):
        print('\n=== add() START ===')
        print(f'num1 + num2 = {self.num1 + self.num2}')

    def subtract(self):
        print('\n=== substract() START ===')
        print(f'num1 - num2 = {self.num1 - self.num2}')