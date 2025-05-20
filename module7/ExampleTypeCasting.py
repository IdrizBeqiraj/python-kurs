age=25
age_As_string=str(age)
print(age_As_string, " of type type", type(age_As_string))

print(bool(0))#eshte false sepese eshte 0
print(bool(42))# eshte true sepse vlera duhet te jete q e me lart

print(bool(""))
print(bool("Hello"))

#implicit TypeCasting
x=32
y=5.3
resultati=x+y
print(resultati, "of type", type(resultati))

a=5
b="3"
resultati=a*int(b)
print(resultati, "of type", type(resultati))

c=4
resultati2="Hello"*c
print(resultati2)

#get 2 numbers from user input and sum them up 
user=45
user2=70
Rez=user+user2
print(Rez)


#detyr
nr1=int(input)("Enter the First Number: ")
nr2=int(input)("Enter the Second Number: ")
reZZ=nr1+nr2
print(reZZ)
