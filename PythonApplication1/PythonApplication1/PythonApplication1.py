title = 'Workspvae for 03 Storing Numbers'

exp = 5 ** 2
print("Value is: %d" % exp)

area = 0
height = 10
width = 20

area = width * height / 2

print("Old Way")
print("The area of the rectangle is %.2f" % area)
print("justified it is: %6d" % 42)
print("justified and padded it is: %06d" % 42)

print("New Way")
print("The area of the rectangle is {:f}".format(area))
print("The area of the rectangle is {0:d}".format(42))

