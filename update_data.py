import json, requests, datetime

def fetch_game(url):
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        return r.json()
    return []

games = {
    "northstar_cash.json": "https://www.mnlottery.com/api/v1/draw-games/northstar-cash/draws",
    "gopher_5.json": "https://www.mnlottery.com/api/v1/draw-games/gopher-5/draws",
    "powerball.json": "https://www.mnlottery.com/api/v1/draw-games/powerball/draws"
}

for fname, url in games.items():
    data = fetch_game(url)
    with open(fname, "w") as f:
        json.dump(data, f, indent=2)
print("✅ MN Lottery JSON files updated:", datetime.datetime.now())
