from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV

storage = StorageCSV('movie_data_base/movies.csv')
movie_app = MovieApp(storage)
movie_app.run()