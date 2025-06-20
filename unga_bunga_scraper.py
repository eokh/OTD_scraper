# Tribe speak story out loud? Unga bunga decide
PRINT_TO_CONSOLE = True

# Go to big fire cave, ask for story stone
url = "https://en.wikipedia.org/wiki/Main_Page"

# Try to enter cave 3 times. Unga bunga chant helps.
for attempt in range(3):
    response = requests.get(url)
    if response.status_code == 200:
        break
    sleep(2)
else:
    # Cave no open. Unga bunga smash.
    raise Exception(f"Page no work. Code is {response.status_code}")

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
    lines.append(f"- {event}\n")
    if PRINT_TO_CONSOLE:
        # Shout to sky. Unga bunga proud.
        print(f"- {event}")

# Final scratch on stone. Unga bunga done.
filepath.write_text("".join(lines), encoding="utf-8")

