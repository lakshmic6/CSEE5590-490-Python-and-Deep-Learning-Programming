i = input("Please type a sentence: ")

if i.count('a')>=1 or i.count('e')>=1 or i.count('i')>=1 or i.count('o')>=1 or i.count('u')>=1:
    print("frequency of a is",i.count('a'))
    print( "frequency of e is",i.count('e'))
    print("frequency of i is",i.count('i'))
    print("frequency of o is",i.count('o'))
    print("frequency of u is",i.count('u'))
else:
    print("there are no vowels")