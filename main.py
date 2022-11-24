from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
response.raise_for_status()
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

article_text = [titles.find("a").getText() for titles in soup.select(".titleline")]
article_link = [titles.find("a").get("href") for titles in soup.select(".titleline")]
article_upvote = [int(scores.getText().split()[0]) for scores in soup.select(".score")]
index=article_upvote.index(max(article_upvote))
print(article_text[index])
print(article_link[index])
print(article_upvote[index])
