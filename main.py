import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from twilio.rest import Client
from dotenv import load_dotenv
import os
import re

load_dotenv()

# Save on a file called comingSoon
fileImdb = open("comingSoonImdb.txt", "a")
fileImdb.write(str((datetime.now().replace(day=1) + timedelta(days=32)).strftime("%b %Y"))+"\n\n")

imdb = 'https://www.imdb.com/calendar'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', "Accept-Language": "en-US,en;q=0.5"}

pageImdb = requests.get(imdb, headers=headers)
soupImdb = BeautifulSoup(pageImdb.content, 'html.parser')

ComingSoonImdb = soupImdb.find_all(class_="sc-ed25d65a-1 fyabhQ")

# This gets all the dates
ComingSoonImdbDate = soupImdb.find_all(class_="ipc-title__text")
# print(ComingSoonImdbDate)

dateList = []
rePattern = r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{2}, \d{4}\b'
upcoming_month_date = datetime.now().replace(day=1) + timedelta(days=32)
upcoming_month = upcoming_month_date.strftime("%b")
upcoming_year = upcoming_month_date.strftime("%Y")

# This gets the all the dates from the upcoming month and puts them in a list, it uses the pattern created above
for dates in ComingSoonImdbDate:
    match = re.search(rePattern, dates.text.strip())
    if (match and str(match.group().split(" ")[0]) == upcoming_month and str(match.group().split(" ")[1] == upcoming_year)):
        dateList.append(match.group())
        # print(match.group())

moviesImdb = {}
moviesGenre = []

# Imdb get movie titles
for dayInfo in ComingSoonImdb:  # Starts in the class that contains the date and the movie details
    for dates in dayInfo.find_all(class_="ipc-title__text"):
        if dates.text.strip() in dateList:
            # print(dates.text.strip())
            for movie in dayInfo.find_all(class_="ipc-metadata-list-summary-item__tc"):  # class that has the movies titles and its genres
                for i in movie.find_all(class_="ipc-metadata-list-summary-item__t"):  # gets the movies title
                    # print(i)
                    for j in movie.find_all(class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__tl base"):  # Gets the genres
                        # print(j)
                        moviesImdb[i.text.strip()] = ', '.join([s for s in re.split('(?=[A-Z])', j.text.strip()) if s])
print(moviesImdb)

if moviesImdb:
    for i in moviesImdb:
        fileImdb.write("Title: " + str(i) + "\n")
        fileImdb.write("Genre: " + str(moviesImdb[i]) + "\n\n")
else:
    print("No movies for this Month")

fileImdb.write("-----------------------------------------------" + "\n" + "\n")

# Currently using twilio, buts its paid, so when i lose the trial money they ofered, gonna have to change
account_sid = os.getenv('ACC')
auth_token = os.getenv('TOKEN')
client = Client(account_sid, auth_token)

message = client.messages .create(
    body=str(moviesImdb) + '\n',
    from_='whatsapp:+14155238886',
    to='whatsapp:+351911111443'
)

print(message.sid)


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
