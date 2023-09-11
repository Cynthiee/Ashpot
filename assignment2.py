# Static variable
# Instance variable
# local variable
# differentiat with examples, instance method, class method and static method
# Decorations in python

class Instances:

    def __init__(self): # Instance method
        # self.name = name
        return "Instance method", self
    
    @classmethod # Decorator
    def summer(cls):  # Class method
        return "Class method", cls
    
    @staticmethod # Decorator
    def unique(): # Static method
        return "Static method"
    
kind = Instances("Ins")
kind.summer()
kind.unique()
print(kind.summer, kind.unique)