import requests 
from zipfile import ZipFile


global setupDone
setupDone = False

    
download_link = 'http://www.bio-bigdata.center/AVM/download/All%20mutations%20and%20clinical%20information%20for%20the%20nine%20viruses.zip'
r = requests.get(download_link,allow_redirects=True)
open('data.zip','wb').write(r.content)
setupDone = True
