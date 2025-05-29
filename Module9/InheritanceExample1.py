# class Superclass:

# class Subclass(Superclass): # ketu subklasa trashegon prej superklases

class Animal:
    def eat(self):
        print("This animal eats")
    def sleep(self):
        print("It sleeps")

class Bird(Animal):
    def fly(self):
        print("It flyes in the sky")
    def sings(self):
        print("Its sings")

bilbili=Bird()
bilbili.sings()
bilbili.fly()

