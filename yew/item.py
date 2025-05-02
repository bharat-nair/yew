from dataclasses import dataclass, field
import json
from datetime import datetime

import requests

# from yew.utils.api import fetch_item_prices
from yew.utils import get_friendly_unit
from yew import USER_AGENT, ITEMS_URL, ITEMS, PRICES_URL


@dataclass
class Trend:
    """Price trends for an Item."""

    current: float
    today: float
    day30: float
    day90: float
    day180: float


class ItemFetcher:

    @staticmethod
    def fetch_item_by_id(item_id: int):
        item_data = {}

        item_data = ITEMS.get(item_id, {})

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

    @staticmethod
    def fetch_item_by_name(name: str):
        item_data = {}

        for _id in ITEMS:
            if ITEMS[_id].get("name").lower() in name.lower():
                item_data = ITEMS[_id]
                item_id = _id
                break

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


class PriceFetcher:

    @staticmethod
    def fetch_item_price(item_id: int, interval: str):
        if interval == "latest":
            url = f"{PRICES_URL}/latest?id={item_id}"
        else:
            url = f"{PRICES_URL}/timeseries?timestep={interval}&id={item_id}"

        response = (
            requests.get(url, headers={"User-Agent": USER_AGENT}).json().get("data", {})
        )
        return response


@dataclass()
class Price:
    item_id: int
    high_price: int
    low_price: int
    high_price_time: datetime
    low_price_time: datetime
    since: datetime
    high_price_volume: int | None = None
    low_price_volume: int | None = None
    interval: str = "latest"
    friendly_units: bool = False

    def __init__(self, item_id: int, interval: str):
        if not item_id:
            raise RuntimeError("Item ID is not provided")

        self.item_id = item_id
        self.interval = interval

        price_data = PriceFetcher.fetch_item_price(self.item_id, self.interval)
        price_data = price_data.get(f"{item_id}")

        self.high_price = price_data.get("high", 0)
        self.low_price = price_data.get("low", 0)
        self.high_price_time = datetime.fromtimestamp(price_data.get("highTime", 0))
        self.low_price_time = datetime.fromtimestamp(price_data.get("lowTime", 0))
        self.since = (
            self.high_price_time
            if self.high_price_time > self.low_price_time
            else self.low_price_time
        )


@dataclass
class Item:
    """The Item class."""

    id: int
    name: str
    members: bool
    examine: str
    value: int
    highalch: int
    lowalch: int
    icon: str
    type_: str
    limit: int
    trend: Trend
    price: Price | None = field(init=False, default=None)

    @classmethod
    def from_id(cls, id: int):
        """Fetch an item using its ID."""

        if not isinstance(id, int):
            raise TypeError(f"Expected id to be of type int, got {type(id)}")

        item_data = ItemFetcher.fetch_item_by_id(id)

        return cls(
            id=id,
            name=item_data.get("name"),
            members=True if item_data.get("members") == "true" else False,
            examine=item_data.get("examine"),
            value=item_data.get("value"),
            highalch=item_data.get("highalch"),
            lowalch=item_data.get("lowalch"),
            icon=item_data.get("icon"),
            type_=item_data.get("type"),
            limit=item_data.get("limit"),
            trend=Trend(
                current=item_data.get("current"),
                today=item_data.get("today"),
                day30=item_data.get("day30"),
                day90=item_data.get("day90"),
                day180=item_data.get("day180"),
            ),
        )

    @classmethod
    def from_name(cls, name: str):
        """Fetch an item using its name."""

        if not isinstance(name, str):
            raise TypeError(f"Expected name to be of type str, got {type(name)}")

        item_data = ItemFetcher.fetch_item_by_name(name)

        return cls(
            id=item_data.get("item_id"),
            name=item_data.get("name"),
            members=item_data.get("members"),
            examine=item_data.get("examine"),
            value=item_data.get("value"),
            highalch=item_data.get("highalch"),
            lowalch=item_data.get("lowalch"),
            icon=item_data.get("icon"),
            type_=item_data.get("type"),
            limit=item_data.get("limit"),
            trend=Trend(
                current=item_data.get("current"),
                today=item_data.get("today"),
                day30=item_data.get("day30"),
                day90=item_data.get("day90"),
                day180=item_data.get("day180"),
            ),
        )

    def prices(self, interval: str):
        self.price = Price(self.id, interval)
        return self.price
