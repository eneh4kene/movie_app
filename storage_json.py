import json
import requests
from istorage import IStorage

URL = "http://www.omdbapi.com"
API_KEY = "3266dad0"

class StorageJson(IStorage):
    def __init__(self, file_path):
        self._file_path = file_path
        self.movies_data = self.load_data()

    def load_data(self):
        try:
            with open(self._file_path, "r") as fileobj:
                return json.load(fileobj)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return {}

    def save_data(self):
        with open(self._file_path, "w") as fileobj:
            json.dump(self.movies_data, fileobj, indent=4)

    def show_file_path(self):
        return self._file_path

    def list_movies(self):
        print(f"{len(self.movies_data)} in total")
        for key, value in self.movies_data.items():
            print(f"{key}: {value.get('rating')}")

    def add_movie(self):
        user_title = input("Enter new movie name: ")
        if self.movie_exists(self.movies_data, user_title):
            print(f"Movie '{user_title}' already exists in the database.")
            return

        try:
            params = {"apikey": API_KEY, "t": user_title}
            res = requests.get(URL, params=params)
            res.raise_for_status()
            movie_data = res.json()
            if "Error" in movie_data:
                print(f"Movie '{user_title}' doesn't exist in the OMDB API.")
                return

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch movie data from OMDB API: {e}")
            return

        self.movies_data[movie_data.get("Title")] = {
            "rating": movie_data.get("imdbRating", "N/A"),
            "year": movie_data.get("Year", "N/A"),
            "poster": movie_data.get("Poster", "N/A")
        }
        self.save_data()
        print(f"Movie {user_title} successfully added")

    def delete_movie(self):
        user_title = input("Enter movie name to delete: ")
        movie_to_delete = next((title for title in self.movies_data if title.lower() == user_title.lower().strip()), None)

        if movie_to_delete:
            del self.movies_data[movie_to_delete]
            self.save_data()
            print(f"Movie '{movie_to_delete}' successfully deleted.")
        else:
            print(f"Movie '{user_title}' doesn't exist in the database.")

    def update_movie(self):
        user_title = input("Enter movie name to update: ")
        if self.movie_exists(self.movies_data, user_title):
            new_year = input("Enter new year: ")
            new_rating = input("Enter new rating: ")
            new_poster = input("Enter new poster URL: ")

            movie_to_update = self.movies_data[user_title]
            movie_to_update['year'] = new_year
            movie_to_update['rating'] = new_rating
            movie_to_update['poster'] = new_poster
            self.save_data()
            print(f"Movie '{user_title}' successfully updated.")
        else:
            print(f"Movie '{user_title}' doesn't exist in the database.")

    def movie_exists(self, database_movies, user_title):
        return user_title.lower().strip() in map(str.lower, database_movies.keys())
