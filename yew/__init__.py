import json

import requests

ITEMS_URL = "https://secure.runescape.com/m=itemdb_oldschool/api"
PRICES_URL = "https://prices.runescape.wiki/api/v1/osrs"
HISCORES_URL = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.json"
WIKI_URL = "https://oldschool.runescape.wiki/api.php"
USER_AGENT = "YEW - https://github.com/bharat-nair/yew"

ETAG = ""
ITEMS = {}

# Fetch item mapping (ID-Item) from prices.runescape.com
# Save mapping in a local JSON file as a cache
# Check ETag value for future requests to reduce network load
response = requests.get(
    f"{PRICES_URL}/mapping",
    headers={"User-Agent": USER_AGENT, "If-None-Match": ETAG},
)
if response.status_code == 200:
    ETAG = response.headers.get("ETag", "")
    items = response.json()

    with open("items.json", "w") as f:
        for item in items:
            ITEMS[int(item["id"])] = item
