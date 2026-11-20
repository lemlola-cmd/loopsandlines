names = []
name = input("Name (or done): ")
while name != "done":
    names.append(name)
    name = input("Name (or done): ")




correct = 0
searches = len(names)

search = input("Search (or done): ")
while search != "done":
    found = False
    
    for n in names:
        if n == search:
           found = True
           
    if found:
        print("Found")
        correct =+ 1
    else:
        print("Not Found")
        
    search = input("Search (or done): ")

print(correct, "out of",  searches, "Found." )
    

