from mwparserfromhell.nodes.template import Template


def mw_safe_get(mw_template: Template, keys: list, ret_type=str):
    """Get value of any one key among keys from a MediaWiki template."""

    val = ret_type()
    for key in keys:
        if mw_template.has(key):
            val = ret_type(str(mw_template.get(key).value))
            break

    return val


def mw_safe_get_match(mw_template: Template, key, ret_type=str):
    """Get values of all matching keys from a MediaWiki template."""

    vals = list()
    print(mw_template.params)
    for param in mw_template.params:
        if key in param.name:
            vals.append(ret_type(param.value))

    return vals


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
