import datetime

TITLE =  'How Long do ya Got?'
print("-"*40)
print("{:^40}\n".format(TITLE))
print("-"*40)

deadlineInput = input("Input project deadline (yyyy/mm/dd): ")
deadlineDate = datetime.datetime.strptime(deadlineInput, "%Y/%m/%d")
currentDate = datetime.datetime.today()

print("You have:")
delta = deadlineDate - currentDate
print("{} Days left".format(str(delta)))
#print overall hours
days_to_hours = delta.days * 24
diff_btw_two_times = (delta.seconds) / 3600
overall_hours = days_to_hours + diff_btw_two_times
print (str(overall_hours) + ' hours');
print("{} Seconds left".format(str(overall_hours * 60))) 
print("")
