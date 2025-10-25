class Book:
    def __init__(self, title, authors, publication_year):
        self.title = title
        self.authors = authors
        self.publication_year = publication_year

    def __str__(self):
        auth = ' & '.join(self.authors)
        return f'{auth}: {self.title} ({self.publication_year})'

    def num_authors(self):
        return len(self.authors)

def get_num_authors(book): # It doesn't work to call a function in a class for the key=...; you need a normal function.
    return book.num_authors()

clrs = Book('Introduction to Algorithms (3rd ed.)',
            ['Cormen', 'Leiserson', 'Rivest', 'Stein'],
            2009)
fkww = Book('Mathematics Analysis and Approaches HL', 
            ['Fannon', 'Kadelburg', 'Woolley', 'Ward'], 
            2020)
t = Book('Physics for the IB Diploma', 
         ['Tsokos'], 
         2023)

books = [clrs, fkww, t]

books.sort(key=get_num_authors, reverse=True) # This will apply this function to every element then sort. Note, do not use () as this would try call it.

for book in books: # You cant just print(books) because there are objects stored inside. Print calls repr() not __str__().
    #print(repr(book)) # canonical string representation -> 'official' string representation. Most things will return same as print() but objetcs will return memory address.
    #print(repr('hello')) # This is normal
    print(book)