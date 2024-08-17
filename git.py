import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
scrape = input("what you want to scrape ? ")
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get(f"{scrape}")
repo = "https://github.com/Gokul4113"

# Collect repository links
ele = driver.find_elements(By.CLASS_NAME, "repo")
links = []

def raaa(second):
    driver.get(second)
    raw = driver.find_elements(By.CLASS_NAME,"Box-sc-g0xbh4-0 kkrdEu")
    html= driver.page_source
    html = f"{html}"
    if "out_files" in html:
        print(f"found {second}")
def loop(next_page):
    driver.get(next_page)
    time.sleep(5)  # Wait for the page to load completely
    ele2 = driver.find_elements(By.CLASS_NAME, "react-directory-truncate")
    for a in ele2:
        if "probes.py" in a.text:
            second = f"{next_page}/blob/main/{a.text}"
            raaa(second)

for i in ele:
    links.append(i.text)

for l in links:
    next_page = f"{repo}/{l}"
    loop(next_page)

driver.quit()
