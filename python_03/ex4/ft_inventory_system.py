import sys


def parse_items() -> dict | str:
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
    total_values = calculate_values(items_dict)

    for item_name in items_dict.keys():
        if int(items_dict.get(item_name, 0)) > 1:
            print(f"{item_name}: {items_dict.get(item_name, 0)} units "
                  f"({(int(items_dict.get(item_name, 0))
                       / int(total_values)) * 100:.1f})")
        else:
            print(f"{item_name}: {items_dict.get(item_name, 0)} unit "
                  f"({(int(items_dict.get(item_name, 0))
                       / int(total_values)) * 100:.1f})")


def inventory_statistics(items_dict: dict):
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
    print(f"Most abundant: {max_name} ({max_val} units)")
    print(f"Least abundant: {min_name} ({min_val} unit)")


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
    except (Exception) as e:
        print("Error:", e)
