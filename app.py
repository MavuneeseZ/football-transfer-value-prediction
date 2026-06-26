import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("Setting up the invisible browser...")

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')             # Bypass OS security model
options.add_argument('--disable-dev-shm-usage')  # Prevent memory crashes

# Step 1: Initialize the browser (Selenium handles the driver automatically now!)
driver = webdriver.Chrome(options=options)

# Step 2: Navigate to the dynamic website
print("Opening the website...")
driver.get("https://www.transfermarkt.com/liverpool-fc/kader/verein/31/saison_id/2025/plus/1")

# Step 3: Wait for the JavaScript to "build" the page
print("Waiting 3 seconds for JavaScript to load the data...")
time.sleep(3) 

# Step 4: Locate the data we want to scrape
print("Extracting data...\n")
quotes = driver.find_elements(By.CSS_SELECTOR, "td")

# Step 5: Clean and display the data
for quote in quotes:
    print(quote.text)

# Step 6: Close the browser to free up memory
driver.quit()
print("Scraping complete!")
