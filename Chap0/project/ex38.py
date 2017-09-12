ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

# split(ten_things, ' ')
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop(more_stuff)
    next_one = more_stuff.pop()
    print ("Adding:", next_one)
    # append(stuff, next_one)
    stuff.append(next_one)
    print ("There's %d items now." % len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
# pop(stuff)
print(stuff.pop())
# join(' ', stuff)
print(' '.join(stuff)) # what? cool!
# join('#', stuff)
print('#'.join(stuff[3:5])) # super stellar!
