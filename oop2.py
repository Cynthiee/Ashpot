# # Python Access Specifiers
# # Inheritance

# class Human:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
        
#     def talk(self):
#         print("Hello, World!","I'm",self.name, "I am", self.age, "years old.")

# # Inheritance
# class Africans(Human):
#     def __init__(self, name, age, height, size):
#         super().__init__(name, age)
#         self.height = height
#         self.size = size

#     def talk(self):
#         print("Hello")


# class Asians(Human):
#     def __init__(self, name, age, height, size):
#         super().__init__(name, age)
#         self.height = height
#         self.size = size



# # name = Human("Cynthia", 20)
# # name.talk()

# name = Africans("Adaobi", 20, '170cm', 'Large')
# name.talk()

# name = Asians("Jackie Chan", 60, '150cm', 'Medium')
# name.talk()




class Hidden:
    def __init__(self, data1, data2):
        self._data1 = data1
        self._data2 = data2

           
    def get_data1(self):
        print("I'm the", self._data1)

    def get_data2(self):
        print("This is the", self._data2)


data = Hidden('found it', 'simple' )
data.get_data1()
data.get_data2()


# Static variable
# Instance variable
# local variable
# differentiat with examples, instance method, class method and static method
# Decorators in python