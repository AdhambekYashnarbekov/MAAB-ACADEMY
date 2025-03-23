import requests
import json
from bs4 import BeautifulSoup


BASE_URL = "https://www.demoblaze.com/"
LAPTOPS_URL = "https://www.demoblaze.com/#/"

def get_laptops():
    laptops = []
    page = 1
    
    while True:

        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        
   
        items = soup.find_all("div", class_="card-block")
        for item in items:
            name = item.find("h4", class_="card-title").text.strip()
            price = item.find("h5").text.strip()
            description = item.find("p", class_="card-text").text.strip()
            laptops.append({"name": name, "price": price, "description": description})
        
      
        next_button = soup.find("button", id="next2")
        if next_button and "disabled" not in next_button.attrs:
            page += 1
        else:
            break
    
    return laptops

laptop_data = get_laptops()


json_filename = "laptops.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(laptop_data, json_file, indent=4)

print(f"Scraped {len(laptop_data)} laptops and saved to {json_filename}.")
