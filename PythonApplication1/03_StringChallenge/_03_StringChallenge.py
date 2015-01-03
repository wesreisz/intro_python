title = 'Challenge 3: Write a Simple Story'
print("{:^50}\n".format(title))

#write a simple story
story = """There once was a man from {0}
Who kept all his cash in a {2}.
But his daughter, named {1},
Ran away with a man
And as for the {2}, {0}. \n 
length: {3:d}
number of e's: {4:d}\n"""

name = "Nantucket"
name = input("Enter a location that ends with tucket [{}]: ".format(name)) or name
location = "Nan"
location = input("Enter the first part of the location minux the tucket [{}]: ".format(location)) or location
thing = "bucket"
thing = input("Enter something that rythms with tucket [{}]: ".format(thing)) or thing
letter = "e"
letter = input("What letter would you like to count [{}]: ".format(letter)) or letter

print(story.format(name,location.title(),thing,len(story),story.count(letter)))
