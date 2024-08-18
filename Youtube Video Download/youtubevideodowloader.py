import pytube 
 

link = input('Paste the url here : ')
 
video = pytube.YouTube(link)
video.streams.first().download()
 
#promt to make sure that the download is complete
print("Downloaded Successfully, ",link)
