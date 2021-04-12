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


class Magazine(Book):

    def __init__(self, title, author, publish_year, pages, book_language, price, issue):
        """
        :param title:(string)
        :param author:(string)
        :param publish_year:(int)
        :param pages:(int)
        :param book_language:(string)
        :param price:$(int)
        :param issue:(int)
        """
        Book.__init__(self, title, author, publish_year, pages, book_language, price)
        self.issue = issue

    def __str__(self):
        return f'information:\ntitle --> {self.title}\nauthor --> {self.author}\n' \
               f'publish_year -->{self.publish_year}\npage --> {self.pages}\n' \
               f'language --> {self.book_language}\nprice --> {self.price}\n' \
               f'issue --> {self.issue}\nprogress --> {self.progress}%\nstatus --> {self.get_status()}'


class PodcastEpisode:
    def __init__(self, title, speaker, publish_year, time, audio_language, price):
        """
        :param title:(string)
        :param speaker:name speaker(string)
        :param publish_year:(int)
        :param time:base minute(int)
        :param audio_language:(string)
        :param price:$(int)
        """
        self.title = title
        self.speaker = speaker
        self.publish_year = publish_year
        self.time = time
        self.audio_language = audio_language
        self.price = price
        self.time_spend = 0
        self.progress = 0

    def listen(self, time):
        """
        :param time:minutes(int)
        :return:print information time spend  and time remaining
        """
        self.time_spend = self.time_spend + time
        time_remaining = self.time - self.time_spend
        self.progress = round((self.time_spend / self.time) * 100, 2)
        if self.time >= self.time_spend >= 0:
            print(
                f'you have listen {self.time_spend} more min from {self.title}.There are {time_remaining}min left')

    def get_status(self):
        if self.time_spend == 0:
            return "not listen"
        elif self.time_spend == self.time:
            return "finished"
        else:
            return "listening"

    def __str__(self):
        return f'information:\ntitle --> {self.title}\nspeaker --> {self.speaker}\n' \
               f'publish_year --> {self.publish_year}\ntime --> {self.time}min\nlanguage --> {self.audio_language}\n' \
               f'price --> {self.price}\nprogress --> {self.progress}%\nstatus --> {self.get_status()}'


class Audiobook(Book, PodcastEpisode):
    def __init__(self, title, speaker, author, publish_year, pages, book_language, audio_language, time, price):
        Book.__init__(self, title, author, publish_year, pages, book_language, price)
        PodcastEpisode.__init__(self, title, speaker, publish_year, time, audio_language, price)

    def __str__(self):
        return f'information:\ntitle --> {self.title}\nspeaker --> {self.speaker}\nauthor --> {self.author}\n' \
               f'publish_year --> {self.publish_year}\npages --> {self.pages}\n' \
               f'book_language --> {self.book_language}\naudio_language --> {self.audio_language}\n' \
               f'time --> {self.time}min\nprice --> {self.price}\nprogress --> {self.progress}%\n' \
               f'status --> {PodcastEpisode.get_status(self)}'


# function get information per media
def get_data(my_shelf, type_media):
    """
    :param my_shelf:dictionary that keys are type media and values are list object
    :param type_media:To specify the dictionary key ('book', 'magazine', 'podcast episode', 'audiobook')
    :return:No value is returned, only information taken from each media is added to the dictionary.
    """
    print(f'{"-" * 115}')
    if type_media == 'book':
        title = input(f'Enter title book : ')
        author = input(f'Enter author book {title}: ')
        publish_year = int(input(f'Enter publish year book {title}: '))
        pages = int(input(f'Enter pages book {title}: '))
        language = input(f'Enter language book {title}: ')
        price = int(input(f'Enter price book {title}: '))
        my_shelf[type_media].append(Book(title, author, publish_year, pages, language, price))
    elif type_media == 'magazine':
        title = input(f'Enter title magazine : ')
        author = input(f'Enter author magazine {title}: ')
        publish_year = int(input(f'Enter publish year magazine {title}: '))
        pages = int(input(f'Enter pages magazine {title}: '))
        language = input(f'Enter language magazine {title}: ')
        price = int(input(f'Enter price magazine {title}: '))
        issue = int(input(f'Enter issue magazine {title}: '))
        my_shelf[type_media].append(Magazine(title, author, publish_year, pages, language, price, issue))
    elif type_media == 'podcast episode':
        title = input(f'Enter title podcast : ')
        speaker = input(f'Enter speaker podcast {title}: ')
        publish_year = int(input(f'Enter publish year podcast {title}: '))
        time = int(input(f'Enter time(min) podcast {title}: '))
        language = input(f'Enter language podcast {title}: ')
        price = int(input(f'Enter price podcast {title}: '))
        my_shelf[type_media].append(PodcastEpisode(title, speaker, publish_year, time, language, price))
    else:
        title = input(f'Enter title audiobook : ')
        speaker = input(f'Enter speaker audiobook {title}: ')
        author = input(f'Enter author audiobook {title}: ')
        publish_year = int(input(f'Enter publish year audiobook {title}: '))
        pages = int(input(f'Enter pages audiobook {title}: '))
        audio_language = input(f'Enter language audiobook {title}: ')
        book_language = input(f'Enter language book {title}: ')
        time = int(input(f'Enter time(min) audiobook {title}: '))
        price = int(input(f'Enter price audiobook {title}: '))
        my_shelf[type_media].append(
            Audiobook(title, speaker, author, publish_year, pages, audio_language, book_language, time, price))


# function show bookshelf
def show_bookshelf(my_shelf):
    """
    :param my_shelf:dictionary that keys are type media and values are list object
    :return:Print the information of all media
    """
    print('Show my bookshelf')
    for type_media, list_obj in my_shelf.items():
        for obj in range(len(list_obj)):
            print(f'{"-" * 115}\ntype media:{type_media}\n{list_obj[obj].__str__()}')


def sort_item(my_shelf):
    """
    :param my_shelf:dictionary that keys are type media and values are list object
    :return:A sorted list of objects sorted by progress
    """
    list_obj = []
    for list_obj_item in my_shelf.values():
        for _ in list_obj_item:
            list_obj.append(_)
    return sorted(list_obj, key=lambda x: x.progress, reverse=True)


# main
# book_shelf is dictionary that keys are media and values are list of objects
book_shelf = {'book': [], 'magazine': [], 'podcast episode': [], 'audiobook': []}

# make instance of media
book_shelf['book'].append(Book('No Friend But the Mountains', 'Behrouz Boochani', 2018, 374, 'English', 10))
book_shelf['book'].append(Book('The Black Swan', 'Abbas Maroufi', 2007, 280, 'Persian', 20))
book_shelf['book'].append(Book('Symphony of the Dead', 'Behrouz Boochan', 2018, 374, 'English', 126))
book_shelf['magazine'].append(Magazine('Bukhara', 'Ali Dehbashi,Darioush Ashoori', 2020, 768, 'Persian', 55, 140))
book_shelf['podcast episode'].append(PodcastEpisode('Ravaaq', 'Farzin Ranjbar', 2020, 50, 'Persian', 0))
book_shelf['audiobook'].append(
    Audiobook('The Black Swan', 'Ali Bandari', 'Nassim Nicholas Taleb', 2020, 400, 'English', 'Persian', 62, 0))

print(f'{50 * "*"} Welcome :) {50 * "*"}')
while True:
    # print main menu
    print(f'{"-" * 115}\n'
          f'Menu main\n'
          f'1_ Add media\n'
          f'2_ Show bookshelf\n'
          f'3_ Read or listen media\n'
          f'4_ Sort my bookshelf\n'
          f'5_ ًQuit\n'
          f'{"-" * 115}')
    num_item = int(input(f'Please select above item --> '))
    if num_item == 1:
        while True:
            # print menu for add media
            print(f'{"-" * 115}\n'
                  f'Menu Add media\n'
                  f'1_ Add book\n'
                  f'2_ Add magazine\n'
                  f'3_ Add podcastEpisode\n'
                  f'4- Add audiobook\n'
                  f'5_ Back\n'
                  f'{"-" * 115}')
            num_slc = int(input("Please select above item --> "))
            if num_slc == 1:
                get_data(book_shelf, 'book')
            elif num_slc == 2:
                get_data(book_shelf, 'magazine')
            elif num_slc == 3:
                get_data(book_shelf, 'podcast episode')
            elif num_slc == 4:
                get_data(book_shelf, 'audiobook')
            elif num_slc == 5:
                break
            else:
                print('Please enter correct number')
    elif num_item == 2:
        # print bookshelf
        show_bookshelf(book_shelf)
    elif num_item == 3:
        while True:
            # print read or listen media
            print(f'{"-" * 115}\n'
                  f'Menu Read or listen media\n'
                  f'1_ read book\n'
                  f'2_ read magazine\n'
                  f'3_ listen to podcast episode\n'
                  f'4_ listen to audiobook\n'
                  f'5_ back\n'
                  f'{"-" * 115}')
            num_slc = int(input("Please select above item -->"))
            print(f'{"-" * 115}')
            if num_slc == 1:
                obj_book = book_shelf['book']
                for i in range(len(obj_book)):
                    print(f'{i + 1}_ {obj_book[i].title}')  # print title books for select read book
                print(f'{"-" * 115}')
                book_slc = int(input("Please select above a book for read -->"))
                print(f'{"-" * 115}')
                num_pages = int(input('Enter number page --> '))
                print(f'{"-" * 115}')
                obj_book[book_slc - 1].read(num_pages)
            elif num_slc == 2:
                obj_magazine = book_shelf['magazine']
                for i in range(len(obj_magazine)):
                    print(f'{i + 1}_ {obj_magazine[i].title}')  # print title books for select read magazine
                print(f'{"-" * 115}')
                magazine_slc = int(input("Please select above a magazine for read -->"))
                print(f'{"-" * 115}')
                num_pages = int(input('Enter number page --> '))
                print(f'{"-" * 115}')
                obj_magazine[magazine_slc - 1].read(num_pages)
            elif num_slc == 3:
                obj_podcast = book_shelf['podcast episode']
                for i in range(len(obj_podcast)):
                    print(f'{i + 1}_ {obj_podcast[i].title}')  # print title books for select read podcast
                print(f'{"-" * 115}')
                podcast_slc = int(input("Please select above a podcast episode for listen -->"))
                print(f'{"-" * 115}')
                time_spend = int(input('Enter time --> '))
                print(f'{"-" * 115}')
                obj_podcast[podcast_slc - 1].listen(time_spend)
            elif num_slc == 4:
                obj_audiobook = book_shelf['audiobook']
                for i in range(len(obj_audiobook)):
                    print(f'{i + 1}_ {obj_audiobook[i].title}')  # print title books for select read audiobook
                print(f'{"-" * 115}')
                podcast_slc = int(input("Please select above an audiobook for listen -->"))
                print(f'{"-" * 115}')
                time_spend = int(input('Enter time --> '))
                print(f'{"-" * 115}')
                obj_audiobook[podcast_slc - 1].listen(time_spend)
            elif num_slc == 5:
                break
            else:
                print('Please enter correct number')
    elif num_item == 4:
        while True:
            print(f'Menu Sort my bookshelf\n'
                  f'1_ Sort all item\n'
                  f'2_ Sort on base progress\n'
                  f'3_ Back\n'
                  f'{"-" * 115}')
            num_slc = int(input("Please select above item -->"))
            print(f'{"-" * 115}')
            sort_shelf = sort_item(book_shelf)
            if num_slc == 1:
                [print(f'media_type:{i.__class__.__name__}\n{i.__str__()}\n{"-" * 115}') for i in sort_shelf]
            elif num_slc == 2:
                [print(f'media_type:{i.__class__.__name__}\ntitle:{i.title}\nprogress:{i.progress}%\n{"-" * 115}') for i
                 in
                 sort_shelf]
            elif num_slc == 3:
                break
            else:
                print('Please enter correct number')
    elif num_item == 5:
        print(f'{"*" * 50} Good Bay:) {"*" * 50}')
        break
    else:
        print('Please enter correct number')
