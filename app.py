# app.py
from flask import Flask, render_template
from datetime import datetime
import requests
import requests_cache
from bs4 import BeautifulSoup

# Unga bunga summon app spirit
app = Flask(__name__)
# Unga bunga cache fire scrolls for 1 hour
requests_cache.install_cache("unga_bunga_cache", expire_after=3600)

@app.route("/")
def index():
    # Unga bunga enter Wikipedia cave
    url = "https://en.wikipedia.org/wiki/Main_Page"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; UngaBungaBot/1.0)'}
    response = None

    # Unga bunga knock 3 times
    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                break
        except requests.RequestException:
            pass

    # Cave stay silent. Unga bunga rage.
    if not response or response.status_code != 200:
        return "Cave say no story. Unga bunga smash rock in frustration.", 500

    # Unga bunga brew soup from wiki scroll
    soup = BeautifulSoup(response.text, "html.parser")
    on_this_day_section = soup.find("div", id="mp-otd")
    events = []

    # Unga bunga carve story list
    if on_this_day_section:
        ul = on_this_day_section.find("ul")
        if ul:
            for li in ul.find_all("li"):
                for sup in li.find_all("sup"):
                    sup.decompose()  # Smash little number glyphs
                text = li.get_text(strip=True)
                if text:
                    events.append(f"- {text}")

    # Unga bunga read sky and mark day
    today = datetime.now().strftime("%B %d")
    return render_template("index.html", today=today, events=events)

# Unga bunga lost in forest
@app.errorhandler(404)
def not_found(e):
    return "Unga bunga lost. Page no exist. Try different path.", 404

# templates/index.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>On This Day</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
  <main>
    <h1>On This Day – {{ today }}</h1>
    <button onclick="location.reload()" class="fire-button">Fetch Wisdom</button>
    <ul>
      {% for event in events %}
        <li>{{ event }}</li>
      {% endfor %}
    </ul>
    <div class="campfire"></div>
  </main>
</body>
</html>
"""

# static/style.css
"""
body {
  background-color: white;
  color: black;
  font-family: "Apple Garamond", "ITC Garamond", serif;
  font-size: 12pt;
  line-height: 1.6;
  margin: 3rem auto;
  max-width: 700px;
  text-align: center;
  padding: 0 1rem;
}

h1 {
  font-size: 16pt;
  font-weight: bold;
  margin-bottom: 2rem;
}

ul {
  list-style: none;
  padding-left: 0;
  margin: 0 auto;
}

li {
  margin-bottom: 1rem;
}

.fire-button {
  font-family: "Apple Garamond", "ITC Garamond", serif;
  font-size: 12pt;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: linear-gradient(45deg, #ff4500, #ff6b35, #ff8e53);
  color: white;
  margin-bottom: 1.5rem;
  box-shadow: 0 0 10px rgba(255, 69, 0, 0.6);
}

.fire-button:hover {
  opacity: 0.9;
}

.campfire {
  margin-top: 3rem;
  position: relative;
  width: 60px;
  height: 80px;
  margin-left: auto;
  margin-right: auto;
  background: radial-gradient(circle at 50% 80%, #ff4500, #ff6b35, #ff8e53);
  border-radius: 50% 50% 50% 50% / 70% 70% 30% 30%;
  animation: flicker 2s ease-in-out infinite alternate;
  box-shadow: 0 0 20px rgba(255, 69, 0, 0.6);
}

.campfire::before {
  content: '';
  position: absolute;
  top: 15px;
  left: 15px;
  width: 30px;
  height: 50px;
  background: radial-gradient(circle at 50% 80%, #ff8e53, #ffad7a, #ffcc99);
  border-radius: 50% 50% 50% 50% / 65% 65% 35% 35%;
  animation: flicker 1.8s ease-in-out infinite alternate-reverse;
  box-shadow: 0 0 15px rgba(255, 142, 83, 0.5);
}

.campfire::after {
  content: '';
  position: absolute;
  top: 25px;
  left: 25px;
  width: 15px;
  height: 30px;
  background: radial-gradient(circle at 50% 85%, #ffcc99, #ffe0b3, #fff8dc);
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  animation: flicker 1.5s ease-in-out infinite alternate;
  opacity: 0.9;
}

@keyframes flicker {
  0% { transform: scale(1) rotate(-1deg) skewX(1deg); filter: brightness(1) hue-rotate(0deg); }
  25% { transform: scale(1.05) rotate(1deg) skewX(-0.5deg); filter: brightness(1.1) hue-rotate(5deg); }
  50% { transform: scale(0.98) rotate(-0.5deg) skewX(0.8deg); filter: brightness(0.95) hue-rotate(-3deg); }
  75% { transform: scale(1.08) rotate(0.8deg) skewX(-1deg); filter: brightness(1.15) hue-rotate(8deg); }
  100% { transform: scale(1.02) rotate(-1.2deg) skewX(0.5deg); filter: brightness(1.05) hue-rotate(-2deg); }
}
"""

