#Error handling Try, Except, Finally
#Try - writting of the needed code
#Except - what happend if an error happends in the try part
#Finally - Part of code that is always run
from module6.mypackage import resultati

#This is dedicated  for errors that programmers do not predict

#Shembulli i par
try:
    print("Pjesto dy numra")
    nr1=int(input("Shkruani nr1:"))
    nr2=int(input("Shkruani nr2:"))
    resultatii=nr1/nr2
    print("Rezultati:",resultatii)
    resultatii=10/0
except ZeroDivisionError:
    print("ke gabu per shkak qe je duke pjestuar me 0")


#Shembulli i dyte
fruits={
    "Apples":5,
    "Banana":6,
    "Orange":7
}
try:
    print(fruits["cherry"])
except KeyError:
    print("The key does not exist in the dictionary")

text="This is not a number"
#Third example
try:
    text_to_int=int(text)
except Exception as e:
    print("An error ocurred while parsing the data:", e)

#forth example
try:
    resultatii=10/2
except ZeroDivisionError:
    print("Division by zero error occorred")
else:
    print("Division succeful, Result",resultatii)


#fifth example
try:
    resultatii=10/5
except ZeroDivisionError:
    print("Division by zero error occored")
finally:
    print("This part of code always runs")