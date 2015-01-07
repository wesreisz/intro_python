import os

TITLE =  'Let\'s Calculate Your Shipping'
print("-"*40)
print("{:^40}\n".format(TITLE))
print("-"*40)


total = float(input("What is the total sale amount? "))
country = input("What is the Country? ").upper()
province = ""


if "CANADA" == country :
    province = input("What is the Province? ").upper()
    if "ALBERTA" == province :
        total = total * 1.05
    elif "ONTARIO" == province or "NEW BRUNSWICK" == province or "NOVA_SCOTIA" == province :
        total = total * 1.13
    else :
        inital = total
        total = inital * 1.06 + initial * 1.05 
elif "US" == country :
    province = input("What is your state? ").upper()
else :
    print("Sorry, we don't ship to {0}".format(country))
    input("Press enter to exit")
    os._exit(1)

print("Thank you for shipping your order with us")
print("Your order will cost ${0:.2f} and will be shipped to {1} {2}".format(total,province,country))






