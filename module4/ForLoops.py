names=["Alma","Blerta","Dhurata","Shpati"]
for name in names:
    print(name)

#shembulli 2

sentence_shembulli="Hello, World5"
for char in sentence_shembulli:
    if char.isalpha(): #boolean true or false 
        print(char)  #veq shkronjat i implementon


#shembulli 3 me range function
for numri in range(1, 6): #range (x,y) x- ku fillon y- ku mbaron nuk e perfshin y
    print(numri)


#find max numbers ne nje list
numrat=[33,45,45,55,23,12,94,100,101] 
max=numrat[0]
for num in numrat:
    if num>max:
        max=num
print("The max value of the list is ",max) #i krahason cila e ka vleren mat madhe 
