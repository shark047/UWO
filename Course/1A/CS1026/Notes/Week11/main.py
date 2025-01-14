
class Book:

    def __init__(self, title, author, num_pages):
        self._title = title
        self._author = author
        self._num_pages = num_pages

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_num_pages(self):
        return self._num_pages

    def set_title(self, title):
        self._title = title

    def set_num_pages(self, np):
        self._num_pages = np

    def __str__(self):
        return self._title + " by " + self._author + " (" + str(self._num_pages) + ")"

    def __eq__(self, other):
        if isinstance(other, Book) == False:
            raise TypeError("other is not a Book!")

        if self._title.lower() == other._title.lower() and self._author.lower == other._author.lower:
            return True

        return False


b1 = Book("Lord of the Rings", "Tolkien", 15240)
print(b1)

b2 = Book("The Hobbit", "Tolkien", 3856)
b2.set_title("Lord of the rings")
print(b2)
print(b1 == b2)

b3 = "Harry Potter"
#print(b1 == b3)