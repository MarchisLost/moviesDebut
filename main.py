import requests
from bs4 import BeautifulSoup
from datetime import date
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Save on a file called comingSoon
fileImdb = open("comingSoonImdb.txt", "a")
fileImdb.write(str(date.today())+"\n\n")

imdb = 'https://www.imdb.com/calendar'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

pageImdb = requests.get(imdb, headers=headers)
soupImdb = BeautifulSoup(pageImdb.content, 'html.parser')

ComingSoonImdb = soupImdb.find_all(class_="ipc-metadata-list-summary-item__tc")
# print(ComingSoonImdb)

moviesImdb = {}

# Imdb get movie titles
for movie in ComingSoonImdb:
    # Find movie title
    titlesRaw = movie.find_all(class_="ipc-metadata-list-summary-item__t")
    for title in titlesRaw:
        # print(title.text.strip())

        # Find genre
        genreRaw1 = movie.find_all(class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__tl base")
        for genreRaw2 in genreRaw1:
            genreRaw2 = movie.find_all(class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__tl base")
            for genre in genreRaw2:
                # print(genre.text.strip())
                moviesImdb[title.text.strip()] = genre.text.strip()
                fileImdb.write("Title: " + str(title.text.strip()) + "\n")
                fileImdb.write("Genre: " + str(genre.text.strip()) + "\n\n")
# print(moviesImdb)

fileImdb.write("-----------------------------------------------" + "\n" + "\n")

# ------ Cinema NOS -----

# fileNos = open("comingSoonNos.txt", "a")
# fileNos.write(str(date.today())+"\n\n")

# nos = 'https://www.cinemas.nos.pt/filmes'

# pageNos = requests.get(nos, headers=headers)

# soupNos = BeautifulSoup(pageNos.content, 'html.parser')

# Click on "Brevemente"
# ComingSoonNos = soupNos.find_all(class_="movies-filter__tab")
# print(ComingSoonNos)

# moviesNos = []

# NosCinemas stuff
# for x in ComingSoonNos:
#     title = x.find('span')["title"]
#     #print(title)
#     moviesNos.append(title)
#     fileNos.write("Title: " + str(title) + "\n")
# print(moviesNos)

# fileNos.write("-----------------------------------------------" + "\n" + "\n")

account_sid = os.getenv('ACC')
auth_token = os.getenv('TOKEN')
client = Client(account_sid, auth_token)

""" message = client.messages .create(
                     body='\nImdb:\n' + ',\n'.join(moviesImdb) + '\n' + '\nNos:\n' + ',\n'.join(moviesNos),
                     from_='+16153921289',
                     to='+351911111443'
                    )

print(message.sid) """
