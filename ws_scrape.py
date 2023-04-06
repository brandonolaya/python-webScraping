import requests
import bs4

#cuando la url tiene varia paginas y queremos buscar en todas ellas
url_page = 'http://books.toscrape.com/catalogue/page-{}.html'

pagina = requests.get(url_page.format('1')) #para iterar entre paginas
tag_pagina = bs4.BeautifulSoup(pagina.text, 'lxml') #convertirlo en ese formato y usarg los tags

books = tag_pagina.select('.product_pod') #catidad de productos que ese encuentran
stars = books[0].select('.star-rating.Three')#candidad de estrella de un elemento
name = books[0].select('a')[1]['title'] #nombre del titulo del elemento
#primero toma la etiqueta con () y loq ue esta dentro de la etiqueta con []
amount_product_pag = len(tag_pagina.select('.product_pod')) #cantidad en solo una pagina

