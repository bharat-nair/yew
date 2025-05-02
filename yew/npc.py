from dataclasses import dataclass
import re
from typing import TypedDict

import mwparserfromhell as mw
import requests

from yew import WIKI_URL, USER_AGENT
from yew.utils import mw_safe_get, mw_safe_get_match


class NpcFetcher:
    @staticmethod
    def fetch_wikicode(name: str) -> str | None:

        url = f"{WIKI_URL}?action=query&prop=revisions&titles={name}&rvslots=*&rvprop=content&formatversion=2&format=json"
        try:
            response = requests.get(url, headers={"User-Agent": USER_AGENT}).json()

            wikicode: str = (
                response.get("query", {})
                .get("pages", [{}])[0]
                .get("revisions", [{}])[0]
                .get("slots", {})
                .get("main", {})
                .get("content")
            )
            wikicode = wikicode.replace("\n", "")

            return wikicode

        except Exception as e:
            raise e


class NpcParser:

    @staticmethod
    def parse(wikicode: str | None) -> dict[str, str | bool | int | None]:

        npc = {}
        infobox: mw.nodes.template.Template = None

        regex = re.compile(r"[^a-zA-Z0-9 \-\,]")
        regex_keep_space = re.compile(r"[^a-zA-Z0-9\-\,]")

        templates = mw.parse(wikicode).filter_templates()

        for template in templates:
            if "Infobox NPC" in template.name:
                infobox = template

        npc["name"] = mw_safe_get(infobox, ["name", "name1"]).strip()

        members = mw_safe_get(infobox, ["members", "members1"])
        npc["members"] = True if "Yes" in members else False

        npc["race"] = regex.sub("", mw_safe_get(infobox, ["race", "race1"])).strip()

        npc["examine"] = regex.sub(
            "", mw_safe_get(infobox, ["examine", "examine1"])
        ).strip()

        npc["image"] = f"""https://oldschool.runescape.wiki/images/{npc["name"]}.png"""
        npc["level"] = mw_safe_get(infobox, ["level", "level1"], ret_type=int)

        npc["gender"] = regex.sub("", mw_safe_get(infobox, ["gender"])).strip()

        locations = mw_safe_get_match(infobox, "location")
        locations = [regex.sub("", location).strip() for location in locations]
        npc["locations"] = locations

        return npc


@dataclass
class Npc:
    name: str | None
    members: bool | None
    race: str
    examine: str
    image: str
    level: int
    gender: str
    locations: list[str]

    @classmethod
    def from_wiki(cls, name: str):
        wikicode = NpcFetcher.fetch_wikicode(name)
        npc = NpcParser.parse(wikicode)

        return cls(
            name=npc.get("name"),
            members=npc.get("members"),
            race=npc.get("race"),
            examine=npc.get("examine"),
            image=npc.get("image"),
            level=npc.get("level"),
            gender=npc.get("gender"),
            locations=npc.get("locations"),
        )
