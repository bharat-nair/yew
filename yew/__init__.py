import json

import requests

USER_AGENT = "YEW - https://github.com/bharat-nair/yew"

ETAG = ""
ITEMS = {}

ITEMS_URL = "https://secure.runescape.com/m=itemdb_oldschool/api"
PRICES_URL = "https://prices.runescape.wiki/api/v1/osrs"


request = requests.get(
    f"{PRICES_URL}/mapping",
    headers={"User-Agent": USER_AGENT, "If-None-Match": ETAG},
)
if request.status_code == 200:
    ETAG = request.headers.get("ETag", "")
    items = request.json()

    with open("items.json", "w") as f:
        for item in items:
            ITEMS[int(item["id"])] = item
        f.write(json.dumps(ITEMS))
