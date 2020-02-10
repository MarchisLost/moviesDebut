import requests
from bs4 import BeautifulSoup
from csv import writer
from datetime import date

#Save on a file called comingSoon
""" file= open("moviesDebut/comingSoon.txt","a")
file.write(str(date.today())+"\n\n") """

url = 'https://cinemas.nos.pt/'
headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

ComingSoon = soup.find_all(class_="movie-item")

for x in ComingSoon:
  title = x.find('span')
  print (title.text)
"""   file.write("Title: "+ str(title) + "\n")

file.write("-----------------------------------------------" + "\n" + "\n") """
