import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {'user-agent': 'JLubey class example (jlubey@pratt.edu)'}
url = f"https://spinitron.com/WHCL"
r = requests.get(url, headers=headers)

# scrape main spinitron page
whcl = BeautifulSoup(r.text, features="html.parser")
pagetitle = whcl.title
print(pagetitle.text)

artist = whcl.find_all("span", "artist")
song = whcl.find_all("span", "song")
album = whcl.find_all("span", "release")

artists = [a.string for a in artist]
songs = [a.string for a in song]
albums = [a.string for a in album]

mydict = {'song':songs,
        'artist':artists,
        'album':albums
}

whcl_df = pd.DataFrame(mydict)


# get songs from recent playlists
recent = whcl.find("div", "recent-playlists")
recent_atags = recent.find_all("a")
whcl_url = [pl['href'] for pl in recent_atags if "/pl/" in pl['href']]

def whcl_spider(url):
    headers = {'user-agent': 'JLubey class example (jlubey@pratt.edu)'}
    r = requests.get(url, headers=headers)
    wbar = BeautifulSoup(r.text, features="html.parser")

    artist = whcl.find_all("span", "artist")
    song = whcl.find_all("span", "song")
    album = whcl.find_all("span", "release")

    artists = [a.string for a in artist]
    songs = [a.string for a in song]
    albums = [a.string for a in album]

    mydict = {'song':songs,
            'artist':artists,
            'album':albums
    }

    whcl_df = pd.DataFrame(mydict)

    return whcl_df

whcl2 = whcl_spider('https://spinitron.com/' + whcl_url[0])
whcl3 = whcl_spider('https://spinitron.com/' + whcl_url[1])
whcl4 = whcl_spider('https://spinitron.com/' + whcl_url[2])
whcl5 = whcl_spider('https://spinitron.com/' + whcl_url[3])

# dump to csv
whcl_df.to_csv("radio.csv", index=False, mode="a")
whcl2.to_csv("radio.csv", index=False, header=False, mode="a")
whcl3.to_csv("radio.csv", index=False, header=False, mode="a")
whcl4.to_csv("radio.csv", index=False, header=False, mode="a")
whcl5.to_csv("radio.csv", index=False, header=False, mode="a")

# make file without duplicates
file_name = "radio.csv"
file_name_output = "radio_no_dupes.csv"

df = pd.read_csv(file_name, sep=",")

df.drop_duplicates(subset=None, inplace=True)
df.to_csv(file_name_output, index=False)

csvfile = pd.read_csv('radio_no_dupes.csv')

# choose and print a playlist of random songs
#print(csvfile.sample(10))

csvfile.to_html("WHCL.htm")
html_file = csvfile.to_html()
