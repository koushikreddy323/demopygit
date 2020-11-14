import requests
import bs4
base_url='http://books.toscrape.com/catalogue/page-{}.html'
res=requests.get(base_url.format(1))
soup=bs4.BeautifulSoup(res.text,'lxml')
products=soup.select('.product_pod')
example=products[0]
example.select('.star-rating.Three')  #place dot instead of spaces
two_star_rating_books=[]
for x in range(1,51):
    scraped_url=base_url.format(x)
    res=requests.get(scraped_url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    books=soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Two'))!=0:
            book_title=book.select('a')[1]['title']
            two_star_rating_books.append(book_title)
i=0
for x in two_star_rating_books:
    print(i,'.',x)
    i+=1
