#polymorphism
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(make_animal_speak(dog))  # Outputs: Woof!
print(make_animal_speak(cat))  # Outputs: Meow!
