# class Animal:
#     kind = 'herbivores' # class/static variable

#     def __init__(self, name, family):
#         Animal.kind = "carnivores"
#         self.name = name
#         self.family = family

#         # instance method
#     def speak(self):
#         sound = 'meo' # local  variable
#         return "I'm a", self.name,"and I can", sound, Animal.kind
    
#     #  class method
#     @classmethod
#     def get_class_var(cls):
#         cls.kind = "chicken"
#         print(cls.kind)


# #  static method
#     @staticmethod
#     def animal_age(x, y):
#         calc = x *return      print(calc)
    
# lion = Anial("simba", "cat")
# print(lion.speak())
# lion.get_class_var()

# Animal.animal_age(34, 56)
# lion.animal_age(20, 4)


class Animal:
    kind = 'herbivores' # class/static variable

    def __init__(self, name, family):
        self.name = name
        self.family = family

        # instance method
    def speak(self):
        return "Animal kingdom"
    
class Amphibian(Animal):
    def speak(self):
      return "Amphibians are a class of animal"

class Reptile(Animal):
    def speak(self):
        return  "Reptiles are a class of animal"
    
def animal_speak(talk):
    return talk.speak()


    # create object of the child classes
name = input("Name of animal:")
family = input("Animal family:")
lizard = Reptile(name, family)
frog = Amphibian(name, family)

print(animal_speak(lizard))
print(animal_speak(frog))


# Doctyping, method overloading, nested methods
