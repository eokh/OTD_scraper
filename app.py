from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

# Unga bunga fetch from sacred digital scrolls

def scrape_wikipedia_on_this_day():
    today = datetime.today()
    month = today.strftime('%B')
    day = today.day
    url = f"https://en.wikipedia.org/wiki/Wikipedia:Selected_anniversaries/{month}_{day}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content_div = soup.find('div', {'id': 'mp-otd'})

    facts = []
    if content_div:
        for li in content_div.find_all('li'):
            text = li.get_text()
            if text and not text.startswith("Recently featured"):
                facts.append(text.strip())
    return facts[:5]

# Unga bunga home route. If POST, fetch wisdom. Else, show empty rock.
@app.route("/", methods=["GET", "POST"])
def index():
    facts = scrape_wikipedia_on_this_day() if request.method == "POST" else []
    return render_template("index.html", facts=facts)

