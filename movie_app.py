import random

class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def user_menu_options(self):
        print("Menu:")
        menu_options = ["Exit", "List Movies", "Add movie", "Delete movie",
                        "Update Movie", "Stats", "Random Movie", "Search Movie",
                        "Movies Sorted by Rating", "Generate Website"]
        for i, option in enumerate(menu_options):
            print(f'{i}. {option}')

    def stats(self):
        ratings = []
        for movie in self._storage.movies_data.values():
            try:
                rating = float(movie.get("Rating", 0))
                ratings.append(rating)
            except ValueError:
                pass

        if not ratings:
            print("No numeric ratings found.")
            return

        total_ratings = sum(ratings)
        average_rating = total_ratings / len(ratings)
        print(f"Average rating: {average_rating}")

        ratings.sort()
        n = len(ratings)
        if n % 2 == 0:
            median_rating = (ratings[n // 2 - 1] + ratings[n // 2]) / 2
        else:
            median_rating = ratings[n // 2]
        print(f"Median rating: {median_rating}")

        best_rating = max(ratings)
        worst_rating = min(ratings)
        for title, value in self._storage.movies_data.items():
            if float(value.get("Rating", 0)) == best_rating:
                print(f"Best movie: {title}, {value.get('Rating')}")
            elif float(value.get("Rating", 0)) == worst_rating:
                print(f"Worst movie: {title}, {value.get('Rating')}")

    def random_movie(self):
        movie_at_random = random.choice(list(self._storage.movies_data.items()))
        print(f"Your movie for tonight: {movie_at_random[0]}, it's rated {movie_at_random[1].get('Rating')}")

    def search_movie(self):
        user_search = input("Enter part of movie name: ")
        for key, val in self._storage.movies_data.items():
            if user_search.lower().strip() in key.lower():
                print(f"{key}, {val['Rating']}")

    def movies_sorted_by_rating(self):
        sorted_movies = sorted(self._storage.movies_data.items(), key=lambda x: x[1]["Rating"], reverse=True)
        for movie_title, value in sorted_movies:
            print(f"{movie_title}: {value.get('Rating')}")

    def serialize_movies(self):
        movies_data_str = ""
        for movie, info in self._storage.movies_data.items():
            try:
                movie_title = movie
                movie_img = info["Poster"]
                movie_year = info["Year"]
                movies_data_str += '<li>'
                movies_data_str += (f"\n<div class='movie'>"
                                f"<img class='movie-poster' src='{movie_img}'>"
                                f"<div class='movie-title'>{movie_title}</div>"
                                f"<div class='movie-year'>{movie_year}</div>")
                movies_data_str += "</div>\n</li>\n\n"
            except Exception as e:
                print(f"An error occurred : {e}")
                continue
        return movies_data_str

    def read_movies_template(self, html_file_path):
        with open(html_file_path, "r") as movies_template_fileobj:
            return movies_template_fileobj.read()

    def generate_website(self):
        original_html_data = self.read_movies_template("movie_website/index_template.html")
        new_movies_info = self.serialize_movies()
        new_html_data = original_html_data.replace("__TEMPLATE_MOVIE_GRID__", new_movies_info)
        with open("movie_website/movies.html", "w") as fileobj:
            fileobj.write(new_html_data)
        print("Website successfully generated!")

    def user_menu_functions(self, user_input):
        menu_functions = {
            1: self._storage.list_movies,
            2: self._storage.add_movie,
            3: self._storage.delete_movie,
            4: self._storage.update_movie,
            5: self.stats,
            6: self.random_movie,
            7: self.search_movie,
            8: self.movies_sorted_by_rating,
            9: self.generate_website
        }
        return menu_functions[user_input]

    def run(self):
        while True:
            self.user_menu_options()
            user_input = input("Enter choice (0-9): ")
            if user_input.isdigit() and 0 <= int(user_input) <= 9:
                user_input = int(user_input)
                if user_input == 0:
                    print('Bye!')
                    break
                self.user_menu_functions(user_input)()
                print('\n')
                input("Press enter to continue")
            else:
                print("Invalid input. Please enter a number between 0 and 9.")


