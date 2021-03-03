import requests
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

r = requests.get(url, stream = True)

with open("python.txt","wb") as textfile:
   for chunk in r.iter_content(chunk_size=1024):

       if chunk:
           textfile.write(chunk)

file = open ("python.txt")
