# constants
TITLE =  'Loan Payment Calculator'
PADDING_PATTERN = "{0:>20}: "
OUTPUT_PATTERN = "{0:>20}: {1:.2f}"

print("-"*40)
print("{:^40}\n".format(TITLE))
print("-"*40)

#grab some input
amount = float(input(PADDING_PATTERN.format("Loan Amount")))
duration = int(input(PADDING_PATTERN.format("Number of Months")))
interestRate = float(input(PADDING_PATTERN.format("Interest Rate")))

#calculate the result
monthlyPayment = (amount * (1.0 + interestRate))/duration

#display
print("-"*40)
print(OUTPUT_PATTERN.format("Monthly Payment", monthlyPayment)) 
print("")

