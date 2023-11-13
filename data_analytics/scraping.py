from bs4 import BeautifulSoup
import requests

page = requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")
soup = BeautifulSoup(page.text, "html")
table = soup.find_all('table')[1]

word_titles = table.find_all('th')
word_page_titles = [title.text.strip() for title in word_titles]

for row in table.find_all("tr")[1:]:
    row_data = row.find_all("td")
    individual_raw_data = [data.text.capitalize().strip() for data in row_data]

print(individual_raw_data)