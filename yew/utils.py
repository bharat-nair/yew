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
