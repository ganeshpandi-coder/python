class animal:
    def eat (self):
        print("animal is eating")
class dog(animal):
    def bark(self):
        print("dog is barking")
a=dog()
a.eat()
a.bark()
