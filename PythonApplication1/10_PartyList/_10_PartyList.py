TITLE =  'Party List'
print("-"*40)
print("{:^40}\n".format(TITLE))
print("-"*40)

names = []
loop = True
while loop :
    name = input("Input guest name [blank to stop]: ")
    if (len(name)<=0) :
        break
    else :
        names.append(str(name))

names.sort() #inplace sort verses a copy of a sorted list sorted(names)
for currentName in names :
    print(currentName)
