books = []
q1 = "What is the title of the first book?"
q2 = "What is the title of the second book?"
q3 = "What is the title of the third book?"
Q = [q1, q2, q3,]

def get_book(user_book):
    user_book = user_book.capitalize()
    index = 0
    for book in books:
      if book[0] < user_book[0]:
        index = index + 1
    books.insert(index, user_book)

for i in Q:
    print(i)
    get_book(input())

print("Your alphabetical collection is...")
print(books)
