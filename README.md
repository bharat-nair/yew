# ![yew-logs](https://oldschool.runescape.wiki/images/thumb/Yew_logs_detail.png/32px-Yew_logs_detail.png) yew

`yew` is an OldSchool RuneScape API wrapper for Python. It lets you invoke entities of OSRS as Python objects.

## Installation

Install from PyPi:

```
pip install yew
```

You can also install the development version from the repository as:

```
pip install git+https://github.com/bharat-nair/yew.git@development
```

## Usage

Fetch an item:

```
from yew.item import Item

rune_scimmy = Item(id="1333")
rune_scimmy.examine     # "A vicious, curved sword."
rune_scimmy.highalch    # 15360
```

Fetch the latest prices:

```
prices = rune_scimmy.prices(interval="latest")
prices.high_price		# '15.1k'
str(prices.high_price_time)		# '2024-04-04 12:12:12'
```

Fetch a player:

```
from yew.player import Player

lynx_titan = Player("Lynx Titan")
lynx_titan.cooking.level	# 99
lynx_titan.cooking.xp		# 200000000
```

## Contributing

All contributions are welcome! If you would like to propose a new feature or raise a bug you have encountered, please create a new Github issue. Make sure to provide a concise title and a descriptive description, going over the aspects of your feature or bug.

If you would like to contribute to the development of `yew`, all relevant PRs are welcome.
To get started:

- Fork this repository.
- Install dependencies by running:
  ```
  pip install -r requirements.txt
  ```
  Note that it might be beneficial to create a Python virtual environment to keep your local dependencies clean.
- Raise a PR to the `development` branch, once you have made your changes and pushed them.
