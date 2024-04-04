import json

import requests

GE_URL = "https://prices.runescape.wiki/api/v1/osrs/"
ITEMS_URL = "https://secure.runescape.com/m=itemdb_oldschool/api"
HISCORES_URL = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.json"
WIKI_URL = "https://oldschool.runescape.wiki/api.php"
USER_AGENT = "GE APY"


def fetch_item(item_id):

    with open("items.json", "r") as f:
        item_data = json.loads(f.read()).get(item_id, {})

    url = f"{ITEMS_URL}/catalogue/detail.json?item={item_id}"
    response = (
        requests.get(url, headers={"User-Agent": USER_AGENT}).json().get("item", {})
    )
    item_data["icon"] = response.get("icon")
    item_data["type"] = response.get("type")
    item_data["current"] = response.get("current")
    item_data["today"] = response.get("today")
    item_data["day30"] = response.get("day30")
    item_data["day90"] = response.get("day90")
    item_data["day180"] = response.get("day180")

    return item_data


def fetch_item_prices(item_id, interval="latest"):
    """interval: 5m, 1h, 6h, 24h"""

    if interval == "latest":
        url = f"{GE_URL}/latest?id={item_id}"
    else:
        url = f"{GE_URL}/timeseries?timestep={interval}&id={item_id}"

    response = (
        requests.get(url, headers={"User-Agent": USER_AGENT}).json().get("data", {})
    )
    return response


def fetch_player(name: str):

    url = f"{HISCORES_URL}?player={name}"

    response = requests.get(url, headers={"User-Agent": USER_AGENT}).json()

    player_skills = {}
    player_activities = {}
    for skill in response.get("skills", [{}]):
        player_skills[skill["name"]] = skill
    for activity in response.get("activities", [{}]):
        player_activities[activity["name"]] = activity

    return {"skills": player_skills, "activities": player_activities}


def fetch_wikicode(name: str):

    url = f"{WIKI_URL}?action=query&prop=revisions&titles={name}&rvslots=*&rvprop=content&formatversion=2&format=json"
    print(url)
    response = requests.get(url, headers={"User-Agent": USER_AGENT}).json()

    wikicode: str = (
        response.get("query", {})
        .get("pages", [{}])[0]
        .get("revisions", [{}])[0]
        .get("slots", {})
        .get("main", {})
        .get("content")
    )
    # print(wikicode)
    wikicode = wikicode.replace("\n", "")

    # templates = mwparserfromhell.parse(wikicode).filter_templates()
    # print(templates)
    # infobox_template = templates[1]
    # print(infobox_template.name)

    return wikicode
