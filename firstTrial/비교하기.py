#1번
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

print("******************************")
#2번
furry = False
large = False
if furry:
     if large:
             print("It's a yeti.")
     else:
             print("It's a cat!")
else:
     if large:
             print("It's a whale!")
     else:
             print("It's a human. Or a hairless cat.")

print("******************************")
#3번
color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)