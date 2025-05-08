my_set={1,53,53,4,8,9,1,2,3}
print(my_set)

my_set_1=set([1,2,3,4,5,4])
print(my_set_1) 

A={1,2,3}
B={3,4,6}

#find the union
unioni=A.union(B) # unioni A | B
print(unioni)

#intersection
prerja=A.intersection(B) # prerja=A & B
print(prerja)

#diferenca
diferenca=A.difference(B) #diferenca=A-B
print(diferenca)

#diferenca simetrike
d_simetrike=A.symmetric_difference(B) #d_simetrikeA ^ B
print(d_simetrike)

#add element
A.add(6)
print(A)

# remove element
A.remove(6)

#discard - remove an element withou error if it does not e  excits
A.discard(100)

#removes all elements
A.clear()

#find the numer of element of a set
print(len(A))


my_set_2=set([1,2,4])
print(my_set_2)

C=set(1,2,7)
print(C)

#idk
idriz=set('Idriz','Beqiraj','Beqiraj','ONE')
print(idriz)

D=(1,2,3,4)
numri=100
print(numri in D) #true ose false eshte pjese e bashkesise
print(numri not in D)