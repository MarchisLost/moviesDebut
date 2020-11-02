import requests
from bs4 import BeautifulSoup
from datetime import date
from twilio.rest import Client
from dotenv import load_dotenv
import os
# response = requests.get('')

load_dotenv()

# Save on a file called comingSoon
fileImdb = open("comingSoonImdb.txt", "a")
fileImdb.write(str(date.today())+"\n\n")

fileNos = open("comingSoonNos.txt", "a")
fileNos.write(str(date.today())+"\n\n")

imdb = 'https://www.imdb.com/movies-coming-soon/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=b7da399c-a987-4453-bc16-f3ae0c58eee3&pf_rd_r=H2VMYJPWQRGHXGHSBBW1&pf_rd_s=right-8&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_cs_hd'

nos = 'https://cinemas.nos.pt/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

pageImdb = requests.get(imdb, headers=headers)
pageNos = requests.get(nos, headers=headers)

soupImdb = BeautifulSoup(pageImdb.content, 'html.parser')
soupNos = BeautifulSoup(pageNos.content, 'html.parser')

ComingSoonImdb = soupImdb.find_all(class_="overview-top")
ComingSoonNos = soupNos.find_all(class_="list-item__name flex__center")

moviesImdb = []
moviesNos = []

#Imdb stuff
for x in ComingSoonImdb:
    title = x.find('a')["title"]
    #print(title)
    moviesImdb.append(title)
    fileImdb.write("Title: " + str(title) + "\n")
print(moviesImdb)

#NosCinemas stuff
for x in ComingSoonNos:
    title = x.find('span')["title"]
    #print(title)
    moviesNos.append(title)
    fileNos.write("Title: " + str(title) + "\n")
print(moviesNos)

fileImdb.write("-----------------------------------------------" + "\n" + "\n")
fileNos.write("-----------------------------------------------" + "\n" + "\n")

account_sid = os.getenv('ACC')
auth_token = os.getenv('TOKEN')
client = Client(account_sid, auth_token)

message = client.messages .create(
                     body='\nImdb:\n' + ',\n'.join(moviesImdb) + '\n' + '\nNos:\n' + ',\n'.join(moviesNos),
                     from_='+16153921289',
                     to='+351911111443'
                    )

print(message.sid)
