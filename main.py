import requests
from bs4 import BeautifulSoup
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv
import os
import re

load_dotenv()

# Save on a file called comingSoon
fileImdb = open("comingSoonImdb.txt", "a")
fileImdb.write(str(datetime.now().strftime("%d-%m-%Y"))+"\n\n")
rePattern = r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{2}, \d{4}\b'

imdb = 'https://www.imdb.com/calendar'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', "Accept-Language": "en-US,en;q=0.5"}

pageImdb = requests.get(imdb, headers=headers)
soupImdb = BeautifulSoup(pageImdb.content, 'html.parser')

ComingSoonImdb = soupImdb.find_all(class_="sc-ed25d65a-1 fyabhQ")

# This gets all the dates, but is no longer needed ----------------
# ComingSoonImdbDate = soupImdb.find_all(class_="ipc-title__text")
# print(ComingSoonImdbDate)

# dateList = []
# for date in ComingSoonImdbDate:
#     match = re.search(rePattern, date.text.strip())
#     if match:
#         dateList.append(match.group())
#         # print(match.group())

# ----------------------------------------------------------------

moviesImdb = {}
moviesGenre = []

for movie in ComingSoonImdb[0].find_all(class_="ipc-metadata-list-summary-item__tc"):
    # print(movie.text.strip())
    for i in movie.find_all(class_="ipc-metadata-list-summary-item__t"):
        for j in movie.find_all(class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__tl base"):
            moviesImdb[i.text.strip()] = ','.join([s for s in re.split('(?=[A-Z])', j.text.strip()) if s])

print(moviesImdb)
# Imdb get movie titles
# for data in ComingSoonImdb:
    # Find movie title
        # Find genre
        # genreRaw1 = movie.find_all(class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__tl base")
        # for genreRaw2 in genreRaw1:
        #     genreRaw2 = movie.find_all(class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__tl base")
        #     for genre in genreRaw2:
        #         # print(genre.text.strip())
        #         moviesImdb[title.text.strip()] = genre.text.strip()
        #         fileImdb.write("Title: " + str(title.text.strip()) + "\n")
        #         fileImdb.write("Genre: " + str(genre.text.strip()) + "\n\n")
# print(moviesImdb)

# fileImdb.write("-----------------------------------------------" + "\n" + "\n")
# # ------ Cinema NOS -----

# # fileNos = open("comingSoonNos.txt", "a")
# # fileNos.write(str(date.today())+"\n\n")

# # nos = 'https://www.cinemas.nos.pt/filmes'

# # pageNos = requests.get(nos, headers=headers)

# # soupNos = BeautifulSoup(pageNos.content, 'html.parser')

# # Click on "Brevemente"
# # ComingSoonNos = soupNos.find_all(class_="movies-filter__tab")
# # print(ComingSoonNos)

# # moviesNos = []

# # NosCinemas stuff
# # for x in ComingSoonNos:
# #     title = x.find('span')["title"]
# #     #print(title)
# #     moviesNos.append(title)
# #     fileNos.write("Title: " + str(title) + "\n")
# # print(moviesNos)

# # fileNos.write("-----------------------------------------------" + "\n" + "\n")

# account_sid = os.getenv('ACC')
# auth_token = os.getenv('TOKEN')
# client = Client(account_sid, auth_token)

# """ message = client.messages .create(
#                      body='\nImdb:\n' + ',\n'.join(moviesImdb) + '\n' + '\nNos:\n' + ',\n'.join(moviesNos),
#                      from_='+16153921289',
#                      to='+351911111443'
#                     )

# print(message.sid) """
