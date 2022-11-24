from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    text = file.read()
soup = BeautifulSoup(text, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.getText())
# for tags in soup.findAll("a"):
#     print(tags.getText())
#     print(tags.get("href"))
# heading = soup.find(name="h1", id="name")
# print(heading)
# section=soup.find(name="h3",class_="heading")
# print(section)
print(soup.select_one("#name").getText())
print(f"\n\033[32mCreated Playlist  Billboard 100\033[0m")
print("err_msg = '\n\033[31mInvalid year.\033[0m\nPlease enter a valid year.\ne.g 1990\n'")