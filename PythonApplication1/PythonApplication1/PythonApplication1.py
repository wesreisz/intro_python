import datetime

currentDate = datetime.date.today()
print(currentDate)
print("Month: " + str(currentDate.month))
print("Year: " + str(currentDate.year))
print("Day: " + str(currentDate.day))

print(currentDate.strftime('%d %b, %Y'))


userInput = input("Please input your birthdate (mm/dd/YYYY): ")
birthdate = datetime.datetime.strptime(userInput,"%m/%d/%Y").date()
print(birthdate)

days = birthdate - currentDate
print("Days: " + str(days))