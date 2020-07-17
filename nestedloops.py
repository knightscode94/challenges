count = 0

while count < 5:
    name = str(input("Give me a name: "))
    print(name, "is awesome")
    if name == "Chris":
        print(name, "Is not awesome")
        count += 1
    else:
        count += 1

print("for loop")
for i in range(10, 21, 2):
    print(i)

print("Planets:", planets)
print("planets:")

planets = ["mercury", "venus", "earth",
           "mars", "pluto", "jupiter", "saturn",
           "uranus", "neptune"]
           
for planets in planets:
    if planets == "pluto":
        continue
    print(planets)
