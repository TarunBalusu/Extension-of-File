from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import urllib.request
import urllib.parse
import urllib.error

import json
import ssl
import ast
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input(‘Enter Genius song lyrics Url- ‘)

req = Request(url, headers = { ‘User-Agent’ : ‘Mozilla/5.0’ })
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, ‘html.parser’)
html = soup.prettify(‘utf-8’)

song_json = {}
song_json[“Lyrics”] = [];
song_json[“Comments”] = [];

for title in soup.findAll(‘title’):
	song_json[“Title”] = title.text.strip()

for span in soup.findAll(‘span’, attrs = {‘class’: ‘metadata_unit-info metadata_unit-info–text_only’}):
	song_json[“Release date”] = span.text.strip()

for div in soup.findAll(‘div’, attrs = {‘class’: ‘rich_text_formatting’}):
comments = div.text.strip().split(“\n”)
for comment in comments:
if comment!=””:
song_json[“Comments”].append(comment);

for div in soup.findAll(‘div’, attrs = {‘class’: ‘lyrics’}):
song_json[“Lyrics”].append(div.text.strip().split(“\n”));

with open(song_json[“Title”] + ‘.json’, ‘w’) as outfile:
json.dump(song_json, outfile, indent = 4, ensure_ascii = False)

with open(song_json[“Title”] + ‘.html’, ‘wb’) as file:
file.write(html)

print(‘———-Extraction of data is complete. Check json file.———-‘)
