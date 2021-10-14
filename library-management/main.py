
class book:

    def __init__(self, booktitle, author) -> None:
        self.title  = booktitle
        self.author = author

    def __hash__(self) -> int:
        return hash(self.title)

    def __repr__(self) -> str:
        return f"{self.title} by {self.author}"

class library:

    def __init__(self) -> None:
        self.bookshelf = set()

    def add_book(self, book) -> bool:
        """return true if book is added, else false"""
        if book in self.bookshelf:
            return False

        self.bookshelf.add(book) 
        return True

    @property
    def book_shelf(self) -> None:
        for i, book in enumerate(self.bookshelf, start=1):
            print(f"{i:2d}> {book}")
        
    
if __name__ == "__main__":

    library_ = library()

    library_.add_book(book("alchemist", "pablo coehlo"))

    library_.add_book(book("harry potter", "j.k. rowling"))

    library_.book_shelf

    #  1> alchemist by pablo coehlo
    #  2> harry potter by j.k. rowling