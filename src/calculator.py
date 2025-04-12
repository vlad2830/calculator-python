from src.operations import add, subtract, multiply, divide

class Calculator:
    def __init__(self):
        self.last_result = None

    def add(self, a: float, b: float) -> float:
        self.last_result = add(a, b)
        return self.last_result

    def subtract(self, a: float, b: float) -> float:
        self.last_result = subtract(a, b)
        return self.last_result

    def multiply(self, a: float, b: float) -> float:
        self.last_result = multiply(a, b)
        return self.last_result

    def divide(self, a: float, b: float) -> float:
        self.last_result = divide(a, b)
        return self.last_result

    def get_last_result(self) -> float:
        return self.last_result