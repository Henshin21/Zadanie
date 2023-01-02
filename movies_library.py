import random

class Media:
    def __init__(self, title, year_of_publication, genre, plays_count):
        self.title = title
        self.year_of_publication = year_of_publication
        self.genre = genre
        self.plays_count = plays_count

    def play(self, view=1):
        self.plays_count += view

    def __repr__(self):
        return f"{self.title} ({self.year_of_publication})"


class Movie(Media):
    def __init__(self, title, year_of_publication, genre, plays_count):
        super().__init__(title, year_of_publication, genre, plays_count)


class TVSeries(Media):
    def __init__(self, title, year_of_publication, genre, chapter_number, season_number, plays_count):
        super().__init__(title, year_of_publication, genre, plays_count)
        self.chapter_number = chapter_number
        self.season_number = season_number

    def __repr__(self):
        return f"{self.title} S{self.season_number:02d}E{self.chapter_number:02d}"