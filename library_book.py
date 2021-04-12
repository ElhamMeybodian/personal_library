class Book:
    def __init__(self, title, author, publish_year, pages, book_language, price):
        """
        :param title:title of book(string)
        :param author:writer book(string)
        :param publish_year:(integer)
        :param pages:(integer)
        :param book_language:(string)
        :param price:$(integer)
        """
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.book_language = book_language
        self.price = price
        self.read_pages = 0
        self.progress = 0

    def read(self, pages):
        """
        :param pages:number pages read
        :return:print information number pages read and number pages not read
        """
        self.read_pages = self.read_pages + pages
        unread_page = self.pages - self.read_pages
        self.progress = round((self.read_pages / self.pages) * 100, 2)
        if self.pages >= self.read_pages >= 0:
            print(f'you have read {self.read_pages} more pages from {self.title}.There are {unread_page} pages left ')

    def get_status(self):
        """
        :return:status read:
        1- "unread" ( no pages has been read yet)
        2- "reading" ( reading the book)
        3- "finished" ( all pages has been read)

        """
        if self.read_pages == 0:
            return "unread"
        elif self.read_pages == self.pages:
            return "finished"
        else:
            return "reading"

    def __str__(self):
        return f'information:\ntitle --> {self.title}\nauthor --> {self.author}\npublish_year --> {self.publish_year}' \
               f'\npage --> {self.pages}\nlanguage --> {self.book_language}\nprice --> {self.price}\n' \
               f'progress --> {self.progress}%\nstatus --> {self.get_status()}'


def get_data(book_shelf):
    title_book = input(f'Enter title book : ')
    author_book = input(f'Enter author book {title_book}: ')
    publish_year_book = int(input(f'Enter publish year book {title_book}: '))
    pages_book = int(input(f'Enter pages book {title_book}: '))
    language_book = input(f'Enter language book {title_book}: ')
    price_book = int(input(f'Enter price book {title_book}: '))
    book_shelf.append(Book(title_book, author_book, publish_year_book, pages_book, language_book, price_book))


bookshelf = []
while True:
    print(f'{"-" * 115}\n'
          f'1- Add book\n'
          f'2- Read book\n'
          f'3- Get status book\n'
          f'4- Quit\n'
          f'{"-" * 115}')
    num_item = int(input(f'Please select above item --> '))
    if num_item == 1:
        get_data(bookshelf)
    elif num_item == 2:
        for i in range(len(bookshelf)):
            print(f'{i + 1}_ {bookshelf[i].title}')  # print title books for select read book
        print(f'{"-" * 115}')
        book_slc = int(input("Please select above a book for read -->"))
        print(f'{"-" * 115}')
        num_pages = int(input('Enter number page --> '))
        print(f'{"-" * 115}')
        bookshelf[book_slc - 1].read(num_pages)
    elif num_item == 3:
        for i in range(len(bookshelf)):
            print(f'{i + 1}_ {bookshelf[i].title}')  # print title books for select read book
        print(f'{"-" * 115}')
        book_slc = int(input("Please select above a book for status-->"))
        print(f'{"-" * 115}')
        print(f'status {bookshelf[book_slc-1].title} is {bookshelf[book_slc - 1].get_status()}')
    elif num_item == 4:
        break
    else:
        print('Please enter correct number')
