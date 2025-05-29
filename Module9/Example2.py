class Animal:
    def sound(self):
        print("Some generic animal song")

class Dog(Animal):
    def sound(self):
        print("Woof! woof!")

class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")

kafshe=Animal()

kafshe.sound()

rex=Dog()

rex.sound()

tom=Cat()
tom.sound()