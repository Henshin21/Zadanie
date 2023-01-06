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

class Library:
    def __init__(self, movies, tv_series):
        self.movies = movies
        self.tv_series = tv_series
        self.media = movies + tv_series

    def get_movies(self):
        return sorted([video for video in self.media if isinstance(video, Movie)], key=lambda x: x.title)
    
    def get_tv_series(self):
        return sorted([video for video in self.media if isinstance(video, TVSeries)], key=lambda x: x.title)

    def search(self, title):
        for movie in self.movies:
            if movie.title == title:
                return movie
        for tv_series in self.tv_series:
            if tv_series.title == title:
                return tv_series
        return None

    def generate_views(self):
        all_media = self.movies + self.tv_series
        random_media = random.choice(all_media)
        random_views = random.randint(1, 100)
        random_media.play(random_views)

    def top_titles(self, amount=10, content_type=None):
        if content_type == "movies":
            movies = sorted(self.movies, key=lambda x: x.plays_count, reverse=True)[:amount]
            return movies
        elif content_type == "tv_series":
            tv_series = sorted(self.tv_series, key=lambda x: x.plays_count,reverse=True)[:amount]
            return tv_series
        else:
            all_content = self.movies + self.tv_series
            sorted_content = sorted(all_content, key=lambda x: x.plays_count, reverse=True)[:amount]
            return sorted_content    
    
#test 
movie1 = Movie("Och, Karol", 1985, "Dramat", 0)
movie2 = Movie("Nie zadzieraj z fryzjerem", 2008, "Komedia", 0)
tv_series1 = TVSeries("Big Mouth", 2017, "Komedia", 1, 1, 0)
tv_series2 = TVSeries("Niesamowity świat Gumball'a", 2011, "Bajka", 2, 1, 0)

movies = [movie1, movie2]
tv_series = [tv_series1, tv_series2]

library = Library(movies, tv_series)
top_movies = library.top_titles(amount=5, content_type="movies")
top_tv_series = library.top_titles(amount=5, content_type="tv_series")
top_all = library.top_titles(amount=10)