from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.getText())

all_movies = soup.find_all("h3", class_="title")
movie_titles = [movie_title.getText() for movie_title in all_movies]
movies = movie_titles[::-1]

# for n in range(len(movie_titles) - 1, -1, -1):
#     print(movie_titles[n])

with open("movies.txt", "a", errors="ignore") as file:
    for movie in movies:
        file.write(f"{movie}\n")

# PRACTICE CODE

# with open("website.html", errors="ignore") as file:
#     contents = file.read()

# hacker_url = "https://news.ycombinator.com/"
# response = requests.get(url=hacker_url)
# yc_webpage = response.text
# soup = BeautifulSoup(yc_webpage, "html.parser")
# article_tags = soup.find_all("a", class_="titlelink")
#
# article_texts = []
# article_links = []
#
# for tag in article_tags:
#     article_texts.append(tag.getText())
#     article_links.append(tag.get("href"))
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll("span", class_="score")]
# max_score = max(article_upvotes)
# index_of_max = article_upvotes.index(max_score)
#
# print(article_texts[index_of_max])
# print(article_links[index_of_max])
# print(article_upvotes[index_of_max])

# for anchor in all_anchors:
#     print(anchor.getText())

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.title.string)
# tags = soup.find_all(name="a")
#
# for tag in tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h3", class_="heading")
# print(heading.getText())
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
# company_url = soup.select(selector=".heading")
# print(company_url)
# company_url = soup.select_one(selector="#name")
# print(company_url.getText())
