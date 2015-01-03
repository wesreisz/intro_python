#simple input and output
firstName = input("What's is your name? ")
lastName = input("What's your last name " + firstName + "? ")

print("Welcome " + firstName + " " + lastName)

message = "Hello World"
print(message.upper())
print(message.lower())
print(message.swapcase())

#parsing strings
message = "Hello World"
print(message.find('Hello')) #same as indexOf
print(message.count('o'))
print(message.capitalize())
print(message.replace('Hello','Hi'))
