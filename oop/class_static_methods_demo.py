class Calculator:
    calculation_type = "Arithmetic Operations"
    def add(a, b):
        return a + b
    
    def multiply(cls,a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b