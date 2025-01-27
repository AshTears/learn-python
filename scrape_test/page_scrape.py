from bs4 import BeautifulSoup

# Scraping a local webpage
with open('recipes.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'html.parser')
    div_tags = soup.find_all('div', class_='recipe')
    description = soup.find_all('p', class_='description')
    for div, desc in zip(div_tags, description):
        print(div.h2.text + ": " + desc.text)

    html_file.close()


 