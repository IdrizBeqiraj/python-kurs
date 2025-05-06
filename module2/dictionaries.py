#collection of items, mutable, not indexable, works on a pair key:value

contact_into={
    "Alma":"049123456",
    "Erin":"049654321"
}


print(contact_into)

alma_into=contact_into["Alma"]
print(alma_into)
contact_into["Orkidea"]="049000123"
contact_into["Orkidea"]="0490001233"
del contact_into["orkidea"]
print(contact_into)

keys=contact_into.keys()
pritn(keys)

values=contact_into.values()
print(values)

items=contact_into.items()
print(items) #print out the key value pair as a lists