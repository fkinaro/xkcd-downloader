import os
import threading
import requests
import bs4


os.makedirs('xkcd')

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # find the url of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # save the image
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
                imageFIle.close()


# create and start threads
downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target = downloadXkcd, args =(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()


# wait for all threads
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done!')
