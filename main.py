from bs4 import BeautifulSoup
import requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
html_website = response.text

soup = BeautifulSoup(html_website,"html.parser")
headings = soup.find_all(name="h3", class_="title")

print(headings)

titles = [title.getText() for title in headings]

movies = titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")