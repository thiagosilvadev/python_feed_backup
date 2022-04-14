from functions import createFolders, getFeed, downloadFeed

# Create image and audio folders
createFolders(['./images',"./audio"])

# feed
feed = getFeed()

downloadFeed(feed)