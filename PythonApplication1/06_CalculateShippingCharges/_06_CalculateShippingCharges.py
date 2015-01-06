TITLE =  'Let\'s Calculate Your Shipping'
print("-"*40)
print("{:^40}\n".format(TITLE))
print("-"*40)

purchaseAmount = float(input('What is the total purchase amount? '))
if purchaseAmount < 50.00 :
    purchaseAmount += 10.00

print("-"*40)
print("Your shipping amount is ${:.2f}".format(purchaseAmount))
print("-"*40)