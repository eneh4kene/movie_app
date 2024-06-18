from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def show_file_path(self):
        pass

    @abstractmethod
    def list_movies(self):
        pass

    @abstractmethod
    def add_movie(self):
        pass

    @abstractmethod
    def delete_movie(self):
        pass

    @abstractmethod
    def update_movie(self):
        pass
