from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
FILE_PATH = "Top 100 Movies.txt"


response = requests.get(url=URL)
soup = BeautifulSoup(response.text, 'html.parser')

title_elements = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
titles = [title_elements[0].getText().replace("100 ", "")] + [title.getText().split(")")[1][1:] for title in title_elements[1:]]

with open(FILE_PATH, 'w') as file:
    for title_index in range(99, -1, -1):
        file.write(titles[title_index] + "\n")

print("Titles Added!")
