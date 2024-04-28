def get_friendly_unit(n: int):
    """Get prices in units like 2.1b or 100k"""

    available_units = {1_000_000_000: "b", 1_000_000: "m", 1000: "k"}
    unit = ""
    place_value = 1000
    for value in available_units:
        if value <= n:
            unit = available_units[value]
            place_value = value
            break

    while n > place_value:
        n /= place_value

    return f"{format(n,'.1f')}{unit}"
