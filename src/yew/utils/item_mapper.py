import json
import os
import requests

USER_AGENT = "osrs-wrapper"


def fetch_mapping(force_update=False):
    if not os.path.exists("./items.json") or force_update:

        items = requests.get(
            "https://prices.runescape.wiki/api/v1/osrs/mapping",
            headers={"User-Agent": USER_AGENT},
        ).json()

        with open("items.json", "w") as f:
            items_mapped = {}
            for item in items:
                items_mapped[item["id"]] = item
            f.write(json.dumps(items_mapped))


fetch_mapping()
