from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = []
article_links = []
text = soup.find_all(name="span", class_="titleline")
print(text)

for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
# for article in soup.find_all(name="td", class_="subtext"):
#     if article.span.find(class_="score") is None:
#         article_upvotes.append(0)
#     else:
#         article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))
#
# max_points_index = article_upvotes.index(max(article_upvotes))
# print(
#     f"{article_titles[max_points_index]}, "
#     f"{article_upvotes[max_points_index]} points, "
#     f"available at: {article_links[max_points_index]}."
# )