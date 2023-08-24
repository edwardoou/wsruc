from bs4 import BeautifulSoup

# Open File
with open('text.html', encoding="utf8") as f:
    soup = BeautifulSoup(f, 'html.parser')

tabla = soup.find_all('table')[0]
rows = tabla.find_all('td')

row = [i.text for i in rows]
print(row)