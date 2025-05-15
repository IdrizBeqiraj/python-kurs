total = 0

for number in range(1,11):
    if number%2==0:
        total+=number
print("The sum of even numbers from 1 to 10 is ", total)

#this is definding a function. Keyword def - in python defines functions. greet - emri i funksionit
def greet():
    print("Hello World!")
#this is how we use the function
greet()

def greet_person(name):
    print("Hello", name)

greet_person("Idriz")

def shuma(x,y): #this type of function returns something in this case a number 
    z=x+y
    return z
rezultati=shuma(3,4)
print("3 + 4 = ",rezultati)


#local variable - variablat e deklaruara lokalishte per brenda nje funksioni
def greet(name):
    message=f"Hello,{name}!"
    print(message)
greet("Idriz")



#print(message) - this outputs an errror beacuse the message variable is defined only for the function

#argumentet dhe definimi tyre
def greet_person(name, greetting="Hello"):
    message=f"{greetting}, {name}"
    return message
default_greeting=greet_person("Idriz")
print(default_greeting)
custom_greeting=greet_person("Idriz","Good Morning!")
print(custom_greeting)

pershendetja="Hi"
def greet_people(name):
    global pershendetja
    return f"{pershendetja}, {name}"
variabla=greet_people("Idriz")
print(variabla)