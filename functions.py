import os
import feedparser
import json 
import requests
from slugify import slugify

def createFolders(paths):
  for path in paths:
    if not os.path.exists(path):
      os.mkdir(path)

def getFeed():
  return feedparser.parse("https://anchor.fm/s/9630ffc/podcast/rss")


def downloadFile(url, fileName, name):
  if not fileExists(fileName):
    print("Baixando episódio: " + name)
    r = requests.get(url, allow_redirects=True)
    open(fileName, 'wb').write(r.content)
  else: 
    print("Arquivo já existe: " + fileName)

    
def fileExists(fileName):
    return os.path.isfile(fileName)

def downloadFeed(feed):
  for entry in feed.entries:
      # download image
    downloadFile(entry.image.href, "images/" + slugify(entry.title) + ".jpg", entry.title)
    downloadFile(entry.enclosures[0].href, "audio/" + slugify(entry.title) + ".mp3", entry.title)
  