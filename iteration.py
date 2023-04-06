import requests
import bs4

#cuando la url tiene varia paginas y queremos buscar en todas ellas
def url():
    """esta funcion es para obtener la url de la pagna a explorar
    como en esta page- cabia el numero esta se reempla por {} para hacer iteraciones
    """
    url_page = 'http://books.toscrape.com/catalogue/page-{}.html'
    return pags(url_page)


def pags(url_page):
    """ se usa la url de la pagina para crear unos links estos peticiones se transforman en formato 
    lxml para extraer el contenido de las etiquetas
    """
    #iterar paginas
    for pagina in range(1,51):
        #iterador de paginas
        url_pagina = url_page.format(pagina)
        resultado = requests.get(url_pagina)
        tag_pagina = bs4.BeautifulSoup(resultado.text, 'lxml')

        #seleccion de libros
        name_book = tag_pagina.select('.product_pod')
        libros(name_book)

# lista de titulos 4 0 5 estrellas deja de manera global
title_rating_high = []

def libros(name_book):
    """ cada url que obtiene tiene 20 articulos los cuales se van clasificando
    y agregando a la lista si cumplen
    """
    for libro in name_book:
        #check 4 o 5 star
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) !=0:
            #titulo variable
            title_book = libro.select('a')[1]['title']

            #add a la lista
            title_rating_high.append(title_book)


#ver libros
def show_books():
    for t in title_rating_high:
        print(t)

if __name__ == "__main__":
    url()
    show_books()
