from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup



''' setup for chrome browser options to be configured
these setting allow headlessmode( runwithout visible window) ,
disable gpu usage (cause browser use gpu for rendering )
and custom user agent string to mimic real user
(A User-Agent(UA) is information that the browser sends to website for indetifying the browser/client)'''
chrome_options=Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0(Windows NT 10.0; win64;X64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)" 
    "Chrome/131.0.6778.265 Safari/537.36" )



#initializes the Chrome WebDriver using webdriver-manager package.
# It automatically downloads and configures the correct version of ChromeDriver
#avoiding manual setup. 
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,
options=chrome_options)

url="https://www.naukrigulf.com/top-jobs-by-designation"
driver.get(url)

# this step wait command to pause until those elemnts are ready
WebDriverWait(driver,30).until(
    EC.presence_of_element_located((By.CLASS_NAME,"soft-link"))
)

html=driver.page_source
soup=BeautifulSoup(html,"html.parser")

job_profiles_section=soup.find_all('a',class_='soft-link darker')
print("top Job Profiles")
for i, job in enumerate(job_profiles_section[:10],start=1):
    print(f"{i}.{job.text.strip()}")
driver.quit()