#kushtet dhe kontrolla e  flowit te programit
# == nese jane te barabarta dy variabla
# != nese nuk jane te barabarta
# < me e vogel
# > me e madhe
# <= dhe >= me e vogel ose me e madhe e barabarte
# operatoret logjik
# and or not

#shembull1;
age = int(input("Sa vjeq jeni?"))
if age >=15:
    print("je i pranuar ne shkollen digjitale advanced level!")
else:
    print("Code.org")

temperature=28
if temperature>30:
    print("Its hot today, stay inside")
elif 20<= temperature<=30:
    print("The weather is Nice")
else:
    print("Its cold")