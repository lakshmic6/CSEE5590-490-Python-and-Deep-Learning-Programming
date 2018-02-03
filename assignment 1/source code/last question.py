#program to find the students in both of the classes and only enrolled in single classes in student list 1 and student list 2
#  List1 in which students list of python class are stored in:
stdlist1 = ['lakshmi', 'vaishu', 'bhargavi', 'akhila', 'deepthi', 'navya', 'mrudula', 'mrunalini','rekha']

# List2 in which students list of web development class are stored in:
stdlist2 = ['lakshmi', 'vaishu', 'bhargavi', 'akhila', 'deepthi', 'mrudula', 'mounika', 'navya', 'mrunalini', 'ganga']

# Comparing both the files to print common students in both the classes
print(" Comparing both the files starts:")
print('. . . . .  . . . .  \n ')

# Printing students who are common in both the classes
print("Students who are common in both python and web developement classes are: \n")
for s in stdlist1:
    if s in stdlist2:
        print(s)
print('\n')

# Printing Students who are not common in both classes that are python and web development
print("Students who have taken only one of web development or python are: \n")

# Picking out the odd one's out from  the first list of students
print("only in stdlist 1")
for s in stdlist1:
    if s not in stdlist2:
        print(s)

# Picking out the odd one's out from the second list of students
print("only in stdlist 2")
for s in stdlist2:
    if s not in stdlist1:
        print(s)