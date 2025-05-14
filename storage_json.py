import json
from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path


    def get_movies(self):
        """returns a lists of all movies in unordered manner."""
        with open(self.file_path, "r") as infile:
            movies = json.load(infile)
        return movies


    def save_movies(self, source):
        """Saves in-memory db into json file"""
        with open(self.file_path, "w") as outfile:
            json.dump(source, outfile, indent=4)
        return f"Saved to {self.file_path}."


    def list_movies(self):
        pass


    def add_movie(self, title, year, rating, poster):
        """ If not present in database, a new record will be added."""
        movies = self.get_movies()
        if not self.title_is_in_source(title, movies):
            movie = {"Title": title, "Year": year, "Rating": rating, "Poster": poster}
            movies.append(movie)
            self.save_movies(movies)
            return f"New movie {title} added."
        return f"Movie {title} already in database. No changes done."


    def delete_movie(self, title):
        """Deletes given movie. Currently, no search involved
        thus the entered title has to match exactly the title to delete.
        If no match, nothing happens.
        """
        with open(self.file_path, "r") as infile:
            movies = json.load(infile)
        for element in enumerate(movies):
            if element[1]['Title'] == title:
                removed_movie = movies.pop(element[0])['Title']
        with open(self.file_path, "w") as outfile:
            json.dump(movies, outfile, indent=4)
        return f" Removed movie {removed_movie}."


    def update_movie(self, title, rating):
        """Updates the rank of a given movie."""
        with open(self.file_path, 'r') as infile:
            movies = json.load(infile)
        for element in enumerate(movies):
            if element[1]['Title'] == title:
                element[1]['Rating'] = rating
        with open(self.file_path, 'w') as outfile:
            json.dump(movies, outfile, indent=4)
        return f"New Rating for {title}: {rating}."


    def title_is_in_source(self, title, source):
        """Short check if the given movie title is in database.
        Search is case-insensitive.
        :returns: True or False, boolean
        """
        for element in enumerate(source):
            if element[1]['Title'] == title:
                return True
        return False

def main():
    storage = StorageJson('data.json')
    print(storage.list_movies())
    storage.delete_movie('Ritter der Kokosnuss')


if __name__ == '__main__':
    main()
