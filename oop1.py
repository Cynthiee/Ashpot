class Human:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        
    def talk(self):
        print("Hello, World!","I'm",self.name, "I am", self.age, "years old", "and I am", self.color)

name = Human("Cynthia", 20, "dark")
age = Human()
name.talk()

# Read, understand and practice access specified in python
# Using oop, write a python program that has different
# methods to add, subtract, multiply and divide 2 numbers



# class Arithmetics:

#     def __init__(self, add_value, subtract_value, multiply_value, divide_value):
#         self.add_value = add_value
#         self.subtract_value = subtract_value
#         self.multiply_value = multiply_value
#         self.divide_value = divide_value

#     def add(self, num1, num2):
#         print("Addition:", num1 + num2)
#     def subtract(self, num1, num2):
#         print("Subtraction:", num1 - num2)
#     def multiply(self, num1, num2):
#         print("Multiplication:", num1 * num2)
#     def divide(self, num1, num2):
#         if num2 == 0:
#             print("Division by zero is not allowed.")
#         print("Division:", num1 / num2)
    
   
# solution = Arithmetics(17, 28, 93, 67)
# solution.add(78, 57)
# solution.subtract(72, 56)
# solution.multiply(52, 12)
# solution.divide(56, 8)


class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num

    def subtract(self, num):
        self.value -= num

    def multiply(self, num):
        self.value *= num

    def divide(self, num):
        if num != 0:
            self.value /= num
        else:
            raise ValueError("Division by zero is not allowed.")

    def get_result(self):
        return self.value

# Example usage:
calc = Calculator(10)
calc.add(5)
print("Result after addition:", calc.get_result())

calc.subtract(3)
print("Result after subtraction:", calc.get_result())

calc.multiply(4)
print("Result after multiplication:", calc.get_result())

calc.divide(2)
print("Result after division:", calc.get_result())
