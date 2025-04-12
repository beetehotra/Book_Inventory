### --- BOOK CLASS --- ###

class book:
    ### --- initialize --- ###
        
    # Name, Author, Language, Read?(Bool), Owned/Borrowed, if_Owned Lent?(Bool) to whom, if_Borrowed from whom

    def __init__(self, name, author, read, owned, lent, lent_to, borrowed_from):
        self.name = name
        self.author = author
        self.read = read
        self.owned = owned
        self.lent = lent
        self.lent_to = lent_to
        self.borrowed_from = borrowed_from

