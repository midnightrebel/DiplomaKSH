from bs4 import BeautifulSoup
import requests

url = str(input("Вставьте ссылку на ресурс vtcloud: "))
responce = requests.get(url)
soup = BeautifulSoup(responce.text,'lxml')
quotes = soup.find_all('option')
for quote in quotes:
    if(quote.text.__contains__("КШ")):
        print(quote.text[9:])