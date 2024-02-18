class Book:
    def __init__(self, title, author, release_year, number_of_pages):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.number_of_pages = number_of_pages
        #print("Book Created")
    def __del__(self):
        #print("Book destroyed")
        pass


    def toString(self):
        return ",".join([
                str(self.title),
                str(self.author),
                str(self.release_year),
                str(self.number_of_pages)
            ])