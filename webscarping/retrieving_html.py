
#using request method
# fake_useragent so it does not block the scraping
import requests
import time
from fake_useragent import UserAgent
url="https://www.flipkart.com/all/~cs-6ef68bc8d283b86730515a8f2c87ff23/pr?sid=0pm%2Cfcn%2C821%2Ca7x%2C2si&marketplace=FLIPKART&restrictLocale=true&BU=Mixed"

session=requests.Session()
headers={
    'User-Agent': UserAgent().random,
    'Accept-Language': 'en-Us,en;q=0.9',
    'Accept-Encoding':'gzip,deflate,br',
    'Connection':'keep-alive',
    'Referer' :'https://www.google.com'
}

proxy_auth='HhUWuCeRDDLdFmbWUuu1KkpVP5biGdUDPmogehmjkRUN'
proxies={
    'http': f'http://{proxy_auth}',
    'https':f'https://{proxy_auth}'
}

time.sleep(2)
r=session.get(url,proxies=proxies,headers=headers)
print(r.text)
with open("file.html","w") as f:
    f.write(r.text)