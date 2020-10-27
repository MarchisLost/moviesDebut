import requests
from bs4 import BeautifulSoup
from csv import writer
from datetime import date
from twilio.rest import Client
# response = requests.get('')

# Save on a file called comingSoon
file = open("E:\David\Google D\Code\Python\moviesDebut\comingSoon.txt", "a")
file.write(str(date.today())+"\n\n")

url = 'https://www.imdb.com/movies-coming-soon/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=b7da399c-a987-4453-bc16-f3ae0c58eee3&pf_rd_r=H2VMYJPWQRGHXGHSBBW1&pf_rd_s=right-8&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_cs_hd'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

ComingSoon = soup.find_all(class_="overview-top")

movies = []

for x in ComingSoon:
  title = x.find('a')["title"]
  #print(title)
  movies.append(title)
  file.write("Title: " + str(title) + "\n")
print(movies)

#file.write("-----------------------------------------------" + "\n" + "\n")

account_sid = 'AC1ba5d46dd2a26a4400fdaee2b761a410'
auth_token = '4549645935c9c070411686ccd4e76fdf'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=', '.join(movies),
                     from_='+16153921289',
                     to='+351911111443'
                 )

print(message.sid)