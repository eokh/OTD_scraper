import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
from pathlib import Path

# Tribe speak story out loud? Unga bunga decide
PRINT_TO_CONSOLE = True

# Go to big fire cave, ask for story stone
url = "https://en.wikipedia.org/wiki/Main_Page"

# Unga bunga wear disguise so cave guards not suspicious
headers = {'User-Agent': 'Mozilla/5.0 (compatible; UngaBungaBot/1.0)'}

# Try to enter cave 3 times. Unga bunga chant helps.
response = None
for attempt in range(3):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            break
        else:
            print(f"Cave guard angry. Code {response.status_code}. Unga bunga try again.")
    except requests.RequestException as e:
        print(f"Cave spirits block path: {e}. Unga bunga persistent.")
    sleep(2)
else:
    # Cave no open. Unga bunga smash.
    if response:
        raise Exception(f"Page no work after 3 tries. Last code is {response.status_code}")
    else:
        raise Exception("Cave completely blocked. No response from spirits.")

# Brew soup from cave scroll
soup = BeautifulSoup(response.text, "html.parser")
on_this_day_section = soup.find("div", id="mp-otd")

# No story? Wiki hide. Unga bunga curse scroll.
if not on_this_day_section:
    raise Exception("No 'on this day' found. Wiki hide story.")

events_list = on_this_day_section.find("ul")
if not events_list:
    raise Exception("No list of events. History gone. Unga bunga mourn.")

# Carve sky time into stone
today = datetime.now().strftime("%B %d")
header = f"On this day – {today}:\n\n"

# Name the rock with sky number
filename = f"on_this_day_{datetime.now().strftime('%Y-%m-%d')}.txt"
filepath = Path(filename)

# Begin carving. Unga bunga focused now.
lines = [header]
if PRINT_TO_CONSOLE:
    print(header.strip() + "\n")

for li in events_list.find_all("li"):
    # Smash tiny bug glyphs
    for sup in li.find_all("sup"):
        sup.decompose()
    event = li.get_text(strip=True)
    if event:  # Unga bunga no write empty stones
        lines.append(f"- {event}\n")
        if PRINT_TO_CONSOLE:
            # Shout to sky. Unga bunga proud.
            print(f"- {event}")

# Final scratch on stone. Unga bunga done.
try:
    filepath.write_text("".join(lines), encoding="utf-8")
    print(f"\nUnga bunga carved story on stone: {filepath}")
except Exception as e:
    print(f"Stone too hard to carve: {e}. Unga bunga frustrated.")
