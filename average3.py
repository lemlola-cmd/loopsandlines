names = []

for i in range(5):
    name = input("Name: ")
    names.append(name)
target = input("Look For: ")

found = False
for n in names:
    if n == target:
        found = True
if found:
    print(target, "is in the list")
else:
    print(target, "is not in the list")
