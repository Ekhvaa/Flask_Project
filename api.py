import requests
import json


class Film:
    api_key = "b39ede14"

    def __init__(self, film):
        self.film = film

    def request(self):
        # მეთოდი request-ის გასაკეთებლად.
        url = f"http://www.omdbapi.com/?apikey={Film.api_key}&t={self.film}&plot=full"
        r = requests.get(url)
        return r

    @property
    def response(self):
        # აბრუნებს JSON მონაცემებს რექუესთის შემდგომ.
        data = self.request().json()
        return data

    @property
    def rating(self):
        # აბრუნებს ფილმის IMDB რეიტინგს. თუ ფილმს არ აქვს რეიტინგი, მაშინ დააბრუნებს "N/A"-ს.
        rating = self.response["imdbRating"]
        return rating

    @property
    def title(self):
        # JSON მონაცემებიდან გამოაქვს მხოლოდ ფილმის დასახელება იმ შემთხვევაში, თუ ეს ფილმი არსებობს.
        title = self.response["Title"]
        return title

    @property
    def genres(self):
        genres = self.response["Genre"]
        return genres

    def plot(self):
        try:
            plot = self.response["Plot"]
            return plot
        except KeyError:
            print("The summary of the plot is not in the provided data.")


user_input = input("Enter a film: ")
movie = Film(user_input)
req = movie.request()

if movie.response["Response"] == "True":
    structured_data = json.dumps(movie.response, indent=4)
    print(structured_data)
    print(movie.genres)
    print(movie.title)
    print(movie.plot())
    print(movie.rating)
    print(req.status_code)
    print(req.headers)
elif movie.response["Response"] == "False":
    print("The film was not found.")