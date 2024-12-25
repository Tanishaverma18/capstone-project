from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Scrape the links, addresses and prices of the rental properties
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Use our Zillow-Clone website (instead of Zillow.com)
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# Create a list of all the links on the page 
all_link_element = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_element]
print(f"There are {len(all_links)} links to individual listings in total: \n")
# print(all_links)

# Create a list of all the links on the page
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | " , " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look loke this: \n")
# print(all_addresses)

# Create a list of all the price on the page
all_price_element = soup.select(".StyledPropertyCardDataWrapper span")
all_prices = [price.get_text().replace("/mo" , "").split("+")[0] for price in all_price_element]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
# print(all_prices)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    # Add fill in the link to your own google Form
    driver.get(GOOGLE_FORM)
    time.sleep(2)

    # Fill your Xpath of your google form
    address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH, value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()