"""Functions to keep track and alter inventory."""


def create_inventory(items: list[str]) -> dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    return {item: items.count(item) for item in items}


def add_items(inventory: dict, items: list[str]) -> dict:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    item_dict = create_inventory(items)
    if inventory == {}:
        return item_dict
    for key in item_dict:
        if inventory.get(key, 'not found') != 'not found':
            inventory[key] += item_dict[key]
            print(inventory[key])
        else:
            inventory[key] = item_dict[key]
            print(inventory[key])
    return inventory


def decrement_items(inventory: dict, items: list[str]) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if inventory.get(item, 'not found') != 'not found':
            if inventory[item] != 0:
                inventory[item] -= 1
    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if inventory.get(item, 'not found') != 'not found':
        inventory.pop(item)
    return inventory


def list_inventory(inventory: dict) -> list[tuple]:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(key, inventory[key]) for key in inventory if inventory[key] > 0]

