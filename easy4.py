names = []
entry = input("Name (or done): ")
x = 0
while entry != "done":
    x = x + 1
    names.append(entry)
    entry = input("Name (or done): ")
print(names)

print(x, "names saved.")
