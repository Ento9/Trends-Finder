from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import os

options = Options()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://trends.google.com/trends/embed/dailytrends?geo=FR")
driver.maximize_window()
driver.refresh()

time.sleep(1)

try:
    os.remove("FR/data-FR.txt")
except OSError as error:
    print(error)

links = driver.find_elements("xpath", "//a")


for link in links:
    data = link.get_attribute("innerHTML")
    with open("FR/data-FR.txt", 'a') as file:
        file.write(str(data))
    file.close()

x = datetime.datetime.now()

with open("FR/last-research-FR.txt", 'w') as file:
    file.write(str(x))

driver.close()