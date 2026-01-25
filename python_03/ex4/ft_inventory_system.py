import sys


def parse_items() -> dict | str:
    if len(sys.argv) == 1:
        print("Error: No Input Provided !")
    argv = sys.argv[1:]

    if not argv:
        return "Error: No Arguments Provided"
    items = {}
    for arg in argv:
        parts = arg.split(":")

        if len(parts) == 2:
            key, value = parts
            if key and value:
                items.update({key: value})
    if items:
        return items
    example = "|--> Example of usage: ( [Key]:[Value] ) <--|"
    return f"Error: All provided arguments were invalid\n{example}"


def calculate_values(items_dict: dict) -> int:
    calcule = list(items_dict.values())
    cal = 0
    i = 0

    for _ in calcule:
        cal += int(calcule[i])
        i += 1
    return cal


def calculate_keys(items_dict: dict) -> int:
    return len(list(items_dict))


def current_inventory(items_dict: dict) -> None:
    total = int(calculate_values(items_dict))
    for item_name in items_dict.keys():
        if int(items_dict.get(item_name, 0)) > 1:
            print(f"{item_name}: {items_dict.get(item_name, 0)} units "
                  f"({(int(items_dict.get(item_name, 0)) / total) * 100:.1f})")
        else:
            print(f"{item_name}: {items_dict.get(item_name, 0)} unit "
                  f"({(int(items_dict.get(item_name, 0)) / total) * 100:.1f})")


def inventory_statistics(items_dict: dict) -> None:
    min_val = calculate_values(items_dict)
    max_val = 0
    max_name = ""
    min_name = ""

    for name, quantity in items_dict.items():
        current_q = int(quantity)
        if current_q > max_val:
            max_val = current_q
            max_name = name
        if current_q < min_val:
            min_val = current_q
            min_name = name
    if max_val > 1:
        print(f"Most abundant: {max_name} ({max_val} units)")
    else:
        print(f"Most abundant: {max_name} ({max_val} unit)")
    if min_val > 1:
        print(f"Least abundant: {min_name} ({min_val} units)")
    else:
        print(f"Least abundant: {min_name} ({min_val} unit)")


def inventory_categorie(items_dict: dict) -> None:
    moderate_items = {}
    scarce_items = {}

    for name, quantity in items_dict.items():
        current_q = int(quantity)
        if current_q > 3:
            moderate_items.update({name: quantity})
        else:
            scarce_items.update({name: quantity})
    print(f"Moderate: {moderate_items}")
    print(f"Scarce: {scarce_items}")


def suggestions(items_dict: dict) -> None:
    needed = []

    for name, quantity in items_dict.items():
        current_q = int(quantity)
        if current_q <= 1:
            needed += [name]
    if not needed:
        return
    else:
        print("\n=== Management Suggestions ===")
        print("Restock needed:", needed)


def dict_properties(items_dict: dict) -> None:
    dict_keys = []
    dictotalues = []

    for key in items_dict.keys():
        dict_keys += [key]
    for value in items_dict.values():
        dictotalues += [int(value)]

    print("Dictionary keys:", dict_keys)
    print("Dictionary keys:", dictotalues)


def key_checker(items_dict: dict, key: str | int) -> bool:
    return items_dict.get(key) is not None


if __name__ == "__main__":
    try:
        print("=== Inventory System Analysis ===")
        items = parse_items()
        print("Total items in inventory:", calculate_values(items))
        print("Unique item types:", calculate_keys(items))
        print("\n=== Current Inventory ===")
        current_inventory(items)
        print("\n=== Inventory Statistics ===")
        inventory_statistics(items)
        print("\n=== Item Categories ===")
        inventory_categorie(items)
        suggestions(items)
        print("\n=== Dictionary Properties Demo ===")
        dict_properties(items)
        key_name = "sword"
        print(f"Sample lookup - '{key_name}' in inventory: "
              f"{key_checker(items, key_name)}")
    except (Exception) as e:
        print("Error:", e)
