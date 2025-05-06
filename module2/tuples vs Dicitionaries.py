grades={
    ("John","Math"):5,
    ("Alice","Biology"):4,
    ("Bob","Physics"):3.5,
    ("Eve","Music"):5,
    ("John","English"):4
}
#John's grades in math
print(grades[("John","Math")])

#add a grade to Bob in math
grades[("Bob","Math")]=3
print(grades)

#how to get all the students names
keys=list(grades.keys())
print(keys)

student, subject=keys[0]
print(student)
