from osrs.utils.item_mapper import fetch_mapping
import os

if not os.path.exists("items.json"):
    fetch_mapping()
