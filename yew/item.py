from yew.utils.api import fetch_item, fetch_item_prices
from datetime import datetime
from yew.utils.format import get_friendly_unit
from dataclasses import dataclass, field

import requests

from yew import USER_AGENT, ITEMS_URL, ITEMS, PRICES_URL


@dataclass
class Trend:
    """Price trends for an Item."""

    current: float
    today: float
    day30: float
    day90: float
    day180: float


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

    def __init__(self, item_id: int):
        if not item_id:
            raise RuntimeError("Item ID is not provided")

        self.item_id = item_id

        if self.interval == "latest":
            url = f"{PRICES_URL}/latest?id={item_id}&timestep={self.interval}"
        else:
            url = f"{PRICES_URL}/timeseries?timestep={self.interval}&id={item_id}"

        response = (
            requests.get(url, headers={"User-Agent": USER_AGENT}).json().get("data", {})
        )
        price_data = response.get(f"{item_id}")

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
    _price: Price | None = field(init=False, repr=False, default=None)

    @classmethod
    def from_id(cls, id: int):
        """Fetch an item using its ID."""

        if not isinstance(id, int):
            raise TypeError(f"Expected id to be of type int, got {type(id)}")

        item_data = fetch_item(id)

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

        item_data = fetch_item(name=name)

        return cls(
            id=item_id,
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

    @property
    def price(self):
        if self._price is None:
            self._price = Price(self.id)

        return self._price
