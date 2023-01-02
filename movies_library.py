class Movies():
    def __init__(self, titel, year_of_publication, genre, plays_count):
        self.titel = titel
        self.year_of_publication = year_of_publication
        self.genre = genre
        self.plays_count = plays_count

        self.current_watch_count = 0
    
    def play(self,view = 1):
        self.current_watch_count += view

    def __str__(self):
        return f"{self.title} ({self.year})"
    

class TVseries():
    def __init__(self, titel, year_of_publication, genre, chapter_number, season_number, plays_count):
        self.titel = titel
        self.year_of_publication = year_of_publication
        self.genre = genre
        self.chapter_number = chapter_number
        self.season_number = season_number
        self.plays_count = plays_count

        self.current_watch_count = 0

    def play(self,view = 1):
        self.current_watch_count += view

    