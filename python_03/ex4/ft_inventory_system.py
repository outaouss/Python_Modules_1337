import sys


def parse_items() -> dict | str | None:
    if len(sys.argv) == 1:
        print("Error: No Input Provided !")
        return
    argv = sys.argv[1:]
    example_err = "Example of usage: ( [Key (any)]:[Value (int)] )"

    if not argv:
        return "Error: No Arguments Provided"
    items = {}
    for arg in argv:
        parts = arg.split(":")
        try:
            value = int(parts[1])
            if len(parts) == 2 and parts[0] and parts[1] and value >= 0:
                key, value = parts
                if key and value:
                    items.update({key: value})
            elif len(parts) == 2 and parts[0] and parts[1] and value < 0:
                print(f"Error: The Value of '{parts[0]}'"
                      f"is Negative ({parts[1]})")
                return
            else:
                print(example_err)
                return
        except Exception:
            print(example_err)
            return
    if items:
        return items
    return f"Error: All provided arguments were invalid\n{example_err}"


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
    print("\n=== Current Inventory ===")
    total = int(calculate_values(items_dict))
    try:
        for item_name in items_dict.keys():
            v_1 = f"({(int(items_dict.get(item_name, 0)) / total) * 100:.1f}%)"
            v_2 = f"({(int(items_dict.get(item_name, 0)) / total) * 100:.1f}%)"
            f"({(int(items_dict.get(item_name, 0)) / total) * 100:.1f}%)"
            if int(items_dict.get(item_name, 0)) > 1:
                print(f"{item_name}: {items_dict.get(item_name, 0)} "
                      f"units {v_1}")
            else:
                print(f"{item_name}: {items_dict.get(item_name, 0)} unit "
                      f"{v_2}")
    except Exception:
        print("Error occured while calculating the inventory !")


def inventory_statistics(items_dict: dict) -> None:
    min_val = calculate_values(items_dict)
    max_val = 0
    max_name = None
    min_name = None

    for name, quantity in items_dict.items():
        current_q = int(quantity)
        if current_q > max_val:
            max_val = current_q
            max_name = name
        if current_q < min_val:
            min_val = current_q
            min_name = name
    if max_name or min_name:
        print("\n=== Inventory Statistics ===")
    if max_name:
        if max_val > 1:
            print(f"Most abundant: {max_name} ({max_val} units)")
        else:
            print(f"Most abundant: {max_name} ({max_val} unit)")
    if min_name:
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
    if moderate_items or scarce_items:
        print("\n=== Item Categories ===")
    if moderate_items:
        print(f"Moderate: {moderate_items}")
    if scarce_items:
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

    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys:", dict_keys)
    print("Dictionary keys:", dictotalues)


def key_checker(items_dict: dict, key: str | int) -> bool:
    return items_dict.get(key) is not None


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    items = parse_items()
    if items:
        print("Total items in inventory:", calculate_values(items))
        print("Unique item types:", calculate_keys(items))
        current_inventory(items)
        inventory_statistics(items)
        inventory_categorie(items)
        suggestions(items)
        dict_properties(items)
        key_name = "sword"
        print(f"Sample lookup - '{key_name}' in inventory: "
              f"{key_checker(items, key_name)}")
