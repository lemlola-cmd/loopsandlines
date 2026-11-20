
books = []
copies = []

for i in range(3):
    book = input("Title: ")
    books.append(book)
    copy = input("Copy: ")
    copies.append(copy)
    
def find():
    target = input("Search Title:")
    found = False
    
    for i in range(len(books)):
        if books[i] == target:
            print(target, "has", copies[i], "copies.")
            found = True
            
    if not found:
        print("Not in the Library")

        
find()


