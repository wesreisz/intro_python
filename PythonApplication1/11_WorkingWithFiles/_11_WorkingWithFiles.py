TITLE =  'Party List to File'
print("-"*40)
print("{:^40}\n".format(TITLE))
print("-"*40)

#constants
FILENAME = "guestlist.csv"
MODE = "w"
OUTPUT_PATTERN="%s,%d\n"

#member varables
names = []
ages = []

while True :
    name = input("Input guest name [blank to stop]: ")
    if (len(name)<=0) :
        break
    else :
        age = input("Input guest age: ")
        names.append(str(name))
        ages.append(int(age))

myfile = open(FILENAME, mode=MODE)
print("\nGuest list:")
print("-"*40)
for position in range(len(names)):
    print(names[position])
    myfile.write(OUTPUT_PATTERN % (names[position],ages[position]))
myfile.close()
print("\n%s written" %(FILENAME))

