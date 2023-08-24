from bs4 import BeautifulSoup

# Open File
with open('text.html', encoding="utf8") as f:
    soup = BeautifulSoup(f, 'html.parser')
#lista_info = []
html_lista = soup.find_all(class_='list-group-item-text')

""" for elemento in html_lista:
    texto = elemento.get_text(strip=True) # strip=True para eliminar espacios en blanco
    lista_info.append(texto) """

lista_info = [' '.join(i.text.split()) for i in html_lista]

print(lista_info)

tabla = soup.find_all('table')[0]
rows = tabla.find_all('td')

row = [i.text for i in rows]
#print(row)