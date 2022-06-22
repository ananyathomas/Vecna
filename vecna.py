# Implementing Last.fm API

API_KEY = # add your API key
API_SECRET = # add you API key secret
USER_AGENT = 'Dataquest'
import requests
headers = {
    'user-agent': USER_AGENT
}
payload = {
    'api_key': API_KEY,
    'method': 'tag.gettoptracks',
    'format': 'json',
    "tracks": 
    {
        "track": [
                  {...},{...}
                 ],
        "@attr": 
        {
            "page": "1",
            "perPage": "5",
            "totalPages": "1",
            "total": "2"
        }
    }
}

def lastfm_get(url,payload):
    response = requests.get(url,headers=headers,params=payload)
    return response

# Using Text Blob

import random
import json
from textblob import TextBlob
emo =[]

sentence = random.sample(["Hey has your day been?","Hola! How's the day been so far","Ahh friend how has life been treating you this fine day",
                       "Yo what's up"],1)
print(sentence)

reply = input()
blob = TextBlob(reply)

if blob.polarity > 0:
  sentence = random.sample(["That's good to hear","NICEE good for you","Look at you living the life"],1)
  print(sentence)
  emo.append("P")
else:
  sentence = random.sample(["I'm sorry to hear that","Hopefully everything will get better","You'll get through this"],1)
  print(sentence)
  emo.append("N")

sentence = random.sample(["How are you feeling?", "What about you how are you?","You good my bro?"],1)
print(sentence) 
reply = input()
blob = TextBlob(reply)

if blob.polarity > 0:
  sentence = random.sample(["That's great to know!!","SOOO happy for you!!","That's the good stuff"],1)
  print(sentence)
  emo.append("P")
else:
  sentence = random.sample(["Oh no I hope you feel better","I'm here for you","The bad stuff will eventually fade"],1)
  print(sentence)
  emo.append("N")

sentence = random.sample(["What do you think about life?", "What is your opinion on the world?","What are your thoughts on love?"],1)
print(sentence) 
reply = input()
blob = TextBlob(reply)

if blob.polarity > 0:
  sentence = random.sample(["Ohh interesting","Ahh I think the same!!","Woww that's deep"],1)
  print(sentence)
  emo.append("P")
else:
  sentence = random.sample(["Really? that's a unique thought","Wow never thought about it that way!!","Hmm that's an interesting opinion"],1)
  print(sentence)
  emo.append("N")

sentence = random.sample(["What do you think about me?", "What's your opinion on me?"],1)
print(sentence) 
reply = input()
blob = TextBlob(reply)

if blob.polarity > 0:
  sentence = random.sample(["Hehehe thankss xD","OMG THANKSS!!","You're making me blush!!"],1)
  print(sentence)
  emo.append("P")
else:
  sentence = random.sample(["Don't take that tone with me young being","UGGGGHH MOOOMMM","Same sis same"],1)
  print(sentence)
  emo.append("N")

print("How about some music to suit your mood?  Y/N")
a = input()
c = max(emo,key=emo.count)
check= []
# Recommending Songs

if a =="Y" or a=="y":
  if c == "P":
    url = 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=happy&api_key=' + API_KEY + '&format=json'
    r = lastfm_get(url,{'method': 'tag.gettoptracks'})
    print(r.status_code)
    res = r.json()
    for i in range(10):
      j = random.choice(range(0, 50))
      for k in range(0,len(check)):
        if (check[k]==j):
          j = random.choice(range(0, 50))
          k = 0
      check.append(j)
      print(res['tracks']['track'][j]['name'],res['tracks']['track'][j]['url'],res['tracks']['track'][j]['artist']['name'])
  else:
    url = 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=sad&api_key=' + API_KEY + '&format=json'
    r = lastfm_get(url,{'method': 'tag.gettoptracks' })
    print(r.status_code)
    res = r.json()
    for i in range(10):
      j = random.choice(range(0, 50))
      for k in range(0,len(check)):
        if (check[k]==j):
          j = random.choice(range(0, 50))
          k = 0
      check.append(j)
      print(res['tracks']['track'][j]['name'],res['tracks']['track'][j]['url'],res['tracks']['track'][j]['artist']['name'])

# Recommending Movies

def getImage(image):
    try:
        return image.get('loadlate')
    except:
        return 'NA'
def getsynopsys(movie):
    try:
        return movie.find_all("p", {"class":  "text-muted"})[1].getText()
    except:
        return 'NA'
def getMovieTitle(header):
    try:
        return header[0].find("a").getText()
    except:
        return 'NA'

from bs4 import BeautifulSoup as SOUP
import requests as HTTP

movie_title_arr = []
movie_synopsis_arr =[]
image_url_arr  = []

def main(emotion):
  if(emotion == "sad"):
    urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter&format=json, asc'
  else:
    urlhere = 'http://www.imdb.com/search/title?genres=comedy&title_type=feature&sort=moviemeter&format=json, asc'
  response = HTTP.get(urlhere)
  data = response.text
  soup = SOUP(data, "html.parser")
  movies_list  = soup.find_all("div", {"class": "lister-item mode-advanced"})
  for movie in movies_list:
    muted_text = movie.find_all("p", {"class":  "text-muted"})
    header = movie.find_all("h3", {"class":  "lister-item-header"})
    imageDiv =  movie.find("div", {"class": "lister-item-image float-left"})
    image = imageDiv.find("img", "loadlate")
    movie_title =  getMovieTitle(header)
    movie_title_arr.append(movie_title)
    synopsis = getsynopsys(movie)
    movie_synopsis_arr.append(synopsis)
    img_url = getImage(image)
    image_url_arr.append(img_url)

print("How about some movies? Y/N")
b = input()
check =[]
if b =="Y" or b=="y":
  if c == "P":
    main("happy")
  else:
    main("sad")
  for i in range(5):
    j = random.choice(range(0, 10))
    for k in range(0,len(check)):
      if (check[k]==j):
        j = random.choice(range(0, 50))  
        k = 0
    check.append(j)
    print(movie_title_arr[j])
    print(movie_synopsis_arr[j])
    print(image_url_arr[j],"\n")
print("Okayy byee! Hope I helped :)")
