from yew.utils.api import fetch_item, fetch_item_prices
from datetime import datetime
from yew.utils.format import get_friendly_unit


class Item:
    def __init__(self, search_term: int | str) -> None:
        super().__init__()

        self.high_price = None
        self.low_price = None
        self.high_price_time = None
        self.low_price_time = None

        if isinstance(search_term, int):
            item_data = fetch_item(item_id=search_term)
        elif isinstance(search_term, str):
            item_data = fetch_item(name=search_term)

        self.examine = item_data.get("examine", "")
        self.id = item_data.get("id")
        self.members = item_data.get("members", False)
        self.lowalch = item_data.get("lowalch", 0)
        self.limit = item_data.get("limit", 0)
        self.value = item_data.get("value", 0)
        self.highalch = item_data.get("highalch", 0)
        self.icon = item_data.get("icon", "")
        self.name = item_data.get("name", "")
        self.icon = item_data.get("icon")
        self.type = item_data.get("type")
        self.trends = {
            "current": item_data.get("current", {}).get("price", "0.0"),
            "today": item_data.get("today", {}).get("price", "0.0"),
            "day30": item_data.get("day30", {}).get("price", "0.0"),
            "day90": item_data.get("day90", {}).get("price", "0.0"),
            "day180": item_data.get("day180", {}).get("price", "0.0"),
        }

    def prices(self, interval="latest", friendly_units=False):
        return Prices(self.id, interval=interval, friendly_units=friendly_units)


class Prices:
    def __init__(self, item_id, interval="latest", friendly_units=False) -> None:
        self.interval = interval
        self.friendly_units = friendly_units
        self.item_id = item_id

        self.high_price = 0
        self.low_price = 0
        self.high_price_time = None
        self.low_price_time = None
        self.high_price_volume = 0
        self.low_price_volume = 0
        self.since = None

        prices_data = fetch_item_prices(self.item_id, self.interval)

        if self.interval == "latest":
            prices_data = prices_data.get(self.item_id, {})

            if self.friendly_units:
                self.high_price = get_friendly_unit(prices_data.get("high", 0))
                self.low_price = get_friendly_unit(prices_data.get("low", 0))
            else:
                self.high_price = prices_data.get("high", 0)
                self.low_price = prices_data.get("low", 0)

            self.high_price_time = datetime.fromtimestamp(
                prices_data.get("highTime", 0)
            )
            self.low_price_time = datetime.fromtimestamp(prices_data.get("lowTime", 0))

            self.since = (
                self.high_price_time
                if self.high_price_time > self.low_price_time
                else self.low_price_time
            )

        else:
            price_data = prices_data[0]
            if friendly_units:
                self.high_price = get_friendly_unit(price_data.get("avgHighPrice", 0))
                self.low_price = get_friendly_unit(price_data.get("avgLowPrice", 0))
            else:
                self.high_price = price_data.get("avgHighPrice", 0)
                self.low_price = price_data.get("avgLowPrice", 0)

            self.high_price_volume = price_data.get("highPriceVolume", 0)
            self.low_price_volume = price_data.get("lowPriceVolume", 0)
