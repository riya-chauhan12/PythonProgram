#========Basic ============
'''from selenium import webdriver
#This creates a micorsoft edge browser controlled by Selenium.
#driver is simply the Python object through which you control that browser.
#driver represents the browser session you're controlling.
driver =webdriver.Edge()
#Navigate the browser to the specified URL.
driver.get("https://duckduckgo.com/?q=geeksforgeeks")
input("press enter to close")
#close the browser session
driver.quit() '''

# =============finding element ================
# thee tutorial uses a test e-commerce website containing laptop products and extracts:
#Title Price Description Rating

#webdriver to create/control the browser
from selenium import webdriver

#by =used to depcify how we want to locate an element.ther are several ways:(class_name)
#By.ID,By.TAG_NAME,By.CSS_SELECTOR,By.XPATH,By.NAME
from selenium.webdriver.common.by import By

#Service is used to configure/provide the ChromeDriver service that Selenium uses to communicate with Chrome
from selenium.webdriver.chrome.service import Service

#useses it automatically download/set up to the appropriate chromeDriver(ChromeDriverManager().install())
#So instead of manually finding the ChromeDriver executable, we can use:

from webdriver_manager.chrome import ChromeDriverManager


#The browser may need some time to load the page before we try to extract elements.
import time


element_list=[]
#create palce weere we can specify option for chrome (cause normally selenium opens a visible browser window )
#With headless mode:You don't see the browser window.
options=webdriver.ChromeOptions()

options.add_argument("--headless")
#--no-sandbox  browser runtime option in certian env(ex linux) 
#for basic window we do not need tis
options.add_argument("--no-sandbox")

#This is another runtime option commonly used in restricted/container environments.
options.add_argument("--disable-dev-shm-usage")

#create chrome drivier servicemService(...)
#This gets/sets up the ChromeDriver.

service=Service(ChromeDriverManager().install())
for page in range(1,3): 
    driver=webdriver.Chrome(service=service,options=options)
    #Why {page} cuasse F string so page value will change form loop
    url=f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"
    driver.get(url)
    #wait 2 sec This gives the page time to load.
    time.sleep(2)
    price=driver.find_elements(By.CLASS_NAME,"price")
    #Find all elements whose class name is "title".
    titles=driver.find_elements(By.CLASS_NAME,"title")

    description=driver.find_elements(By.CLASS_NAME,"description")
    ratings=driver.find_elements(By.CLASS_NAME,"ratings")
    for i in range(len(titles)):
        element_list.append([
            titles[i].text,
            price[i].text,
            description[i].text,
            ratings[i].text
        ])
    driver.quit()
for row in element_list:
    print(row)