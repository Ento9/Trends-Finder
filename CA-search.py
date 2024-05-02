from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import os

options = Options()
options.add_argument("--headless")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://trends.google.com/trends/embed/dailytrends?geo=CA")

driver.refresh()

time.sleep(1)

try:
    os.remove("CA/data-CA.txt")
except OSError as error:
    print(error)

links = driver.find_elements("xpath", "//a")


for link in links:
    data = link.get_attribute("innerHTML")
    with open("CA/data-CA.txt", 'a') as file:
        file.write(str(data))
    file.close()

x = datetime.datetime.now()

with open("CA/last-research-CA.txt", 'w') as file:
    file.write(str(x))

driver.close()