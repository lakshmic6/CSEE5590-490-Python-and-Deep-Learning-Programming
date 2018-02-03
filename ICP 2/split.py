i=open('words.txt','r')
for line in i.readlines():
    x=len(line.split(' '))
    print(line,x)