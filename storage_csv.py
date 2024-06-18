import csv
import requests
from istorage import IStorage

URL = "http://www.omdbapi.com"
API_KEY = "3266dad0"

class StorageCSV(IStorage):
    def __init__(self, file_path):
        self._file_path = file_path
        self.ensure_csv_headers()
        self.movies_data = self.load_data()

    def ensure_csv_headers(self):
        with open(self._file_path, 'a+', newline='') as file:
            file.seek(0)
            if not file.read(1):
                writer = csv.DictWriter(file, fieldnames=['Title', 'Year', 'Rating', 'Poster'])
                writer.writeheader()

    def load_data(self):
        try:
            with open(self._file_path, "r", newline='') as fileobj:
                reader = csv.DictReader(fileobj)
                return {row['Title']: {'Year': row['Year'], 'Rating': row['Rating'], 'Poster': row['Poster']} for row in reader}
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self._file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Title', 'Year', 'Rating', 'Poster'])
            writer.writeheader()
            for title, data in self.movies_data.items():
                row = {'Title': title, 'Year': data['Year'], 'Rating': data['Rating'], 'Poster': data['Poster']}
                writer.writerow(row)

    def show_file_path(self):
        return self._file_path

    def list_movies(self):
        print(f"{len(self.movies_data)} in total")
        for key, value in self.movies_data.items():
            print(f"{key}: {value.get('Rating')}")

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
            'Year': movie_data.get('Year', 'N/A'),
            'Rating': movie_data.get('imdbRating', 'N/A'),
            'Poster': movie_data.get('Poster', 'N/A')
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
            movie_to_update['Year'] = new_year
            movie_to_update['Rating'] = new_rating
            movie_to_update['Poster'] = new_poster
            self.save_data()
            print(f"Movie '{user_title}' successfully updated.")
        else:
            print(f"Movie '{user_title}' doesn't exist in the database.")

    def movie_exists(self, database_movies, user_title):
        return user_title.lower().strip() in map(str.lower, database_movies.keys())
