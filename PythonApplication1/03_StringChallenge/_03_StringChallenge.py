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
girl = "Nan"
thing = "bucket"
letter = "e"

print(story.format(name,girl,thing,len(story),story.count(letter)))
