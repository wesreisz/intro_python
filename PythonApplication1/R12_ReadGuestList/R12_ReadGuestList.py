import csv

print('Printing Guest List')

with open("guestList.txt",mode="r") as myFile :
    allData = csv.reader(myFile)
    name = ""
    age = ""
    for row in allData :
        position = 0
        for item in row :
            position+=1
          
            if position==1 :
                name = item
            else :
                age = item
        print("{} ({})".format(name, age))

