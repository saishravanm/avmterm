import requests 
from zipfile import ZipFile
import os

global setupDone
setupDone = False

    
download_link = 'http://www.bio-bigdata.center/AVM/download/All%20mutations%20and%20clinical%20information%20for%20the%20nine%20viruses.zip'
r = requests.get(download_link,allow_redirects=True)
if not os.path.exists("./data/"):
    os.mkdir("./data/")
if not os.path.exists("./output/"):
    os.mkdir("./output/")    
else:
    open('./data/data.zip','wb').write(r.content)
    with ZipFile("./data/data.zip", 'r') as zObject: 
        zObject.extractall(path="./data/")
    zObject.close()
    os.remove("./data/data.zip")
    setupDone = True
