import random, time, requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from random import randrange

Page_number = str(random.randrange(1, 1253))
url = "https://boardgamegeek.com/browse/boardgame/page/"+Page_number
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

Intermediatelist = ('')

for a in soup.find_all('a', href=True):
    Intermediatelist += a['href']+"å"

Final_list = Intermediatelist.split('å')
Final_list_2 = Final_list[13:313]
Final_list_3 = Final_list_2[0::3]

New_url = "https://boardgamegeek.com/"+(random.choice(Final_list_3))
#New_url = "https://boardgamegeek.com/boardgame/203504/stormcloud-attack-eldritch-beast"


print(Page_number)
print(New_url)

url= New_url
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
Webscrape = soup.find_all("meta")
Intermediatelist = ('')
for el in Webscrape:
                Intermediatelist += (str(el))

Final_list_usable = Intermediatelist.split("<")
Game_description_long = Final_list_usable[17]
Game_description_medium = Game_description_long[14:-22]
Game_description_short = Game_description_medium.split("\n")
Game_description_short_intermidate = Game_description_short[0].split(".")
Game_description_shortest = '.'.join(Game_description_short_intermidate[0:3])

print(len(Game_description_short[0]))

if len(Game_description_medium) <= 200:
    print(Game_description_medium)
elif len(Game_description_short[0]) <= 75:
    print(''.join(Game_description_short[0:3]))
elif len(Game_description_short[0]) >= 150:
    print(Game_description_shortest.replace("&amp;quot;",""))
else:
    print(Game_description_short[0])





#print(Game_description_medium)
#print(Game_description_short[0])
#print(len(Game_description_short[0]))
#print(soup.prettify())