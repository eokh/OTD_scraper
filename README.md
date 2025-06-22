# On This Day Scraper – Unga Bunga Edition

## Why This Exists
Fire let early humans share warmth and light. Knowledge does the same for the present.  
This project treats a first Python script as that first spark – a handmade answer to the industrial glow of modern AI. By scraping Wikipedia’s **On This Day** list and carving it into a digital cave wall, it links the dawn of storytelling to today’s code. As the script matures it will grow from crude glyphs to cathedral-scale narrative, the way cave art once bloomed into the Sistine Chapel and now into personalized feeds.

## What Unga Bunga Do
A short, sharp script stalks the Wikipedia cave, grabs the daily historical embers, cleans away citation clutter, and presents the stories for humans to pass around the communal fire.

### Tribe-Approved Features
* **Story Hunter** – fetches “On This Day” events  
* **Glyph Smasher** – strips `[1]`, `[2]`, and similar debris  
* **Rock Carver** – writes to `on_this_day_YYYY-MM-DD.txt`  
* **Story Teller** – prints to terminal  
* **Spirit Resistant** – retries on network errors  
* **Disguise Master** – polite User-Agent so Wikipedia stays calm  
* **Cave Painting Display** – HTML page with flickering campfire

## File Map

OTD_scraper/
├── unga_bunga_scraper.py    Python hunter
├── index.html               Digital campfire display
├── README.md                This scroll
└── on_this_day_*.txt        Generated tablets

## Quick Start

### 1 – Install Magic Berries
```bash
pip3 install requests beautifulsoup4

2 – Traditional Cave Scrape

python3 unga_bunga_scraper.py

3 – Modern Cave Display
	1.	Run the scraper
	2.	Open index.html in a browser
	3.	Watch the campfire and read the events

How It Works
	1.	Enters Wikipedia quietly
	2.	Locates the “On This Day” section
	3.	Removes citation glyphs
	4.	Writes clean lines to a dated file
	5.	Optionally displays them in the HTML campfire

Evolution Roadmap

Stage	Symbol	Goal
Spark	Fire	Working CLI scraper
Canvas	Paint	Rich HTML layout, typography, and motion
Digital Fire	Screen	Interactive page with live parallax effects
Immersive Sky	Sky	Future VR-style experience where a virtual elder narrates events

Contributing

Fork the repo, open a pull request, and keep the style rough but readable.
All improvements – code, design, or storytelling – are welcome.

License

Public domain. Use it, remix it, pass it along the fire circle.

“The first spark of code and the first spark of fire serve the same end – keeping stories alive.”

