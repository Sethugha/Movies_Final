from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """Lists all movies in unordered manner."""
        pass


    @abstractmethod
    def get_movies(self):
        """Lists all movies in unordered manner."""
        pass


    @abstractmethod
    def save_movies(self, source):
        """writes the im-memory db into json file"""
        pass


    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """ Asks for Title, rating and publishing year of a movie,
        if not present in database, the new record will be added.
        """
        pass


    @abstractmethod
    def delete_movie(self, title):
        """Deletes given movie. Currently, no search involved
        thus the entered title has to match exactly the title to delete.
        If no match, nothing happens.
        """
        pass


    @abstractmethod
    def update_movie(self, title, rating):
        """Updates the rank of a given movie."""
        pass


    @abstractmethod
    def title_is_in_source(self, title, source):
        """Short check if the given movie title is in database.
        Search is case-insensitive.
        :returns: True or False, boolean
        """
        pass

if __name__ == '__main__':
    main()
