import requests
import bs4

pagina = requests.get('https://escueladirecta.com/')
elemento = bs4.BeautifulSoup(pagina.text, 'lxml')
imagen = elemento.select('.course-box-image')[14]['src']## aislar la url de la imagen

imagen_extraer = requests.get(imagen) 
f = open('imagen.jpg', 'wb') # forma binaria para leer, la ruta queda al mismo nivel que los archivos
f.write(imagen_extraer.content) ##el content de la con codigo que no es visible
f.close()