import requests
import csv
from datetime import datetime

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
data = response.json()

price = data["bpi"]["USD"]["rate"]
time_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

file_name = "crypto_data.csv"

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)
    
    if file.tell() == 0:
        writer.writerow(["time", "price"])
    
    writer.writerow([time_updated, price])

print("Data updated successfully")
