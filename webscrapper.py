"""
Initial webscrapping of One Piece characters

At first, it only prints the name and wiki links of all characters
"""

import sys
import requests
from bs4 import BeautifulSoup

#try:
result = requests.get(url="https://onepiece.fandom.com/wiki/List_of_Canon_Characters")

# If the status code isn't 200, the page isn't accessible:
if result.status_code != 200:
    raise ConnectionError("It wasn't possible to connect to the website.\nStatus code:", result.status_code)

src = result.content
soup = BeautifulSoup(src, 'lxml')
"""
links = soup.find_all("a")

links = list(map(str, links))

characters_anchors = []

for link in links:
    #link = str(link)
    if (link.startswith("<a href=\"/wiki/") and "/wiki/Chapter" not in link and "/wiki/Episode" not in link and
        "/wiki/One_Piece_" not in link and "/wiki/SBS" not in link and "/wiki/Vivre_Card" not in link):
        if "Groups of known numbers" in link:
            break
        characters_anchors.append(link)


# The first 3 links is not in the characters list
del characters_anchors[0]
del characters_anchors[0]
del characters_anchors[0]


for link in characters_anchors:
    character_link = "https://onepiece.fandom.com/wiki/"
    index_after_wiki = 14
    link_end_index = link.find("\"", index_after_wiki)
    character_link += link[index_after_wiki+1:link_end_index]
    character_name_start_index = link.find(">")
    character_name_end_index = link.find("<", character_name_start_index)
    character_name = link[character_name_start_index+1:character_name_end_index]
    print(character_name, "-", character_link)
"""

characters_anchors = []

tables = soup.find_all("table")
del tables[2]


lines = tables[0].find_all("tr")
del lines[0]

lines2 = tables[1].find_all("tr")
del lines2[0]

lines += lines2


for line in lines:
    tds = line.find_all("td")
    anchor = tds[1].find("a")
    #print(anchor)
    characters_anchors.append(anchor)

characters_anchors = list(map(str, characters_anchors))

print("bbb")

for link in characters_anchors:
    #print(link)
    character_link = "https://onepiece.fandom.com/wiki/"

    if link.startswith("<a class=\"mw-redirect\""):
        index_after_wiki = 35
    else:
        index_after_wiki = 14
    
    link_end_index = link.find("\"", index_after_wiki)
    character_link += link[index_after_wiki+1:link_end_index]
    character_name_start_index = link.find(">")
    character_name_end_index = link.find("<", character_name_start_index)
    character_name = link[character_name_start_index+1:character_name_end_index]
    print(character_name, "-", character_link)


#except:
#    sys.exit("Error during connection, exiting the program...")
