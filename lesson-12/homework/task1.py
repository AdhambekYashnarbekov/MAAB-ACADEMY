from bs4 import BeautifulSoup


with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")


weather_data = []
for row in soup.find("tbody").find_all("tr"):
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    weather_data.append({"day": day, "temperature": temp, "condition": condition})


print("5-Day Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")


max_temp_day = max(weather_data, key=lambda x: x["temperature"])
print(f"\nHottest Day: {max_temp_day['day']} with {max_temp_day['temperature']}°C")


sunny_days = [entry["day"] for entry in weather_data if entry["condition"].lower() == "sunny"]
print(f"Sunny Days: {', '.join(sunny_days)}")


average_temp = sum(entry["temperature"] for entry in weather_data) / len(weather_data)
print(f"Average Temperature for the week: {average_temp:.2f}°C")
