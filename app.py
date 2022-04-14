from functions import createFolders, getFeed, downloadFeed

# Create image and audio folders
createFolders(['./images',"./audio"])

# feed
feed = getFeed()

downloadFeed(feed)






# # print(json.dumps(f.entries[0].enclosure, sort_keys=True, indent=4))

# downloadFile(f.entries[0].enclosures[0].href, "audio/" + slugify(entry.title) + ".mp3")

