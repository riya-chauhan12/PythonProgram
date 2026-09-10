
#using request method
# fake_useragent so it does not block the scraping

#using request method
# fake_useragent so it does not block the scraping
#proxy_auth='HhUWuCeRDDLdFmbWUuu1KkpVP5biGdUDPmogehmjkRUN'
#==================Basic request (send http Request)===================
'''
import request
url='https://www.geeksforgeeks.org/python/python-programming-language-tutorial/'

#Sends a GET request to the given URL.
res=requests.get(url)
#Returns the raw HTML of the page in bytes.
print(res.content)
#returns http status code
print(res.status_code)
with open("file.html","w") as f:
    f.write(res.text) '''

#===================Parsing with BeautifulSoup================
'''
import requests
from bs4 import BeautifulSoup
url='https://www.geeksforgeeks.org/python/python-programming-language-tutorial/'
res=requests.get(url)
#Converts HTML into a searchable object. 'html.parser' is the built-in parse
soup=BeautifulSoup(res.content,'html.parser')
#Formats the HTML nicely for easier reading
#print(soup.prettify())

with open("bs$.html","w" )as f:
    f.write(soup.prettify())
'''
#====================Extracting Content by Tag and Class========
import requests
from bs4 import BeautifulSoup
url='https://www.geeksforgeeks.org/python/python-programming-language-tutorial/'
res=requests.get(url)
soup=BeautifulSoup(res.content,'html.parser')
quotes=[]

#Find every <div> whose class is this particular class.
quote_box=soup.find_all('div',class_='col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top')

for box in quote_box:
    #Inside this quote box, find the <img> element.alt is atrribute of img tag
    quote_text=box.img['alt'].split("#")
    #creating one dictionary containing all the information about one quote.
    quote={
        #finds the <h5>.gets its text.removes unnecessary whitespace around it.
        'theme':box.h5.text.strip(),
        'image_url':box.img['src'],
        #so we split the data by ('#') now this gives the data in 1st index
        'lines':quote_text[0],
        #Because not every quote may necessarily contain:author
        'author':quote_text[1] if len(quote_text)> 1 else 'Unknown'

    }
    quotes.append(quote)
#diplay quotes
for q in quotes[:5]: #print only 5
    print(q)

'''
This entire <div> is one quote box.

The scraper takes this one box: and extract information

<html>
    <body>
        <div class="quote">
            ...
        </div>
    </body>
</html>

'''