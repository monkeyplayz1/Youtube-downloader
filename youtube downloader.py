from pytube import YouTube
import os



os.system('pip install pytube')
os.system('pip install os')

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
print("videos keywords:",yt.keywords)
print("this video was made on",yt.publish_date)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
print("credit to monkeyplayz1 and towardsdatascience website")
