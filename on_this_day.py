import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Go get big wiki page
url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)

# If wiki not come back good, make loud angry
if response.status_code != 200:
    raise Exception(f"Page no work. Code is {response.status_code}")

# Use big soup magic to read page
soup = BeautifulSoup(response.text, "html.parser")
on_this_day_section = soup.find("div", id="mp-otd")

# If no "on this day", then no story. Bad.
if not on_this_day_section:
    raise Exception("No 'on this day' found. Wiki hide story.")

events_list = on_this_day_section.find("ul")
# If no list, then no event. Only sadness.
if not events_list:
    raise Exception("No list of events. History gone.")

# Mark today with sky symbols
today = datetime.now().strftime("%B %d")
print(f"📅 On this day – {today}:\n")

# Smash events into stone tablet (text file)
with open("on_this_day.txt", "w", encoding="utf-8") as file:
    file.write(f"On this day – {today}:\n\n")

    for li in events_list.find_all("li"):
        # Smash little footnote bug
        for sup in li.find_all("sup"):
            sup.decompose()
        event = li.get_text(strip=True)
        # Shout event to sky
        print("-", event)
        # Scratch event into tablet
        file.write("- " + event + "\n")
