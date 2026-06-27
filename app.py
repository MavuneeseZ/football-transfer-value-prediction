import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("Setting up the invisible browser...")

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')           
options.add_argument('--disable-dev-shm-usage') 
driver = webdriver.Chrome(options=options)
urls=['https://www.transfermarkt.com/spieler-statistik/wertvollstemannschaften/marktwertetop']
first=False
row_data=[]
count=0
print("Opening the website...")
for url in urls:
    count=count+1
    driver.get(url)
    print(f"Waiting 1 second for JavaScript to load webpage {count}...")


    print("Extracting data...\n")
    if first==False:
        rows=driver.find_elements(By.CSS_SELECTOR, "table.items > tbody > tr")
        for row in rows:
            cell = row.find_elements(By.TAG_NAME,"td")[1]
            link = cell.find_element(By.TAG_NAME, "a").get_attribute("href")
            print(link)
            urls.append(link)
        first=True
        continue
    rows = driver.find_elements(By.CSS_SELECTOR, "table.items > tbody > tr")
    links = driver.find_elements(By.CSS_SELECTOR, "thead th a")

    columns = [link.get_attribute("textContent").strip() for link in links]

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        cleaned_row = []
        second_cell=row.find_elements(By.TAG_NAME,"td")[1]
        player_link = second_cell.find_elements(By.TAG_NAME, "a")
        for cell in cells:
            text = " ".join(cell.get_attribute("textContent").split())
            if text: 
                cleaned_row.append(text)
        row_data.append(cleaned_row)
    
for row in row_data:
    del row[1]
columns[0] = 'Shirt No.'
columns.insert(2,'Position')
'''columns.append("Appearances")
columns.append("Goals")
columns.append("Assists")'''
df=pd.DataFrame(row_data,columns=columns)
print(df)
driver.quit()
print("Scraping complete!")

