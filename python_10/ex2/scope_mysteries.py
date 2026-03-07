from typing import Dict, Any


def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:

    if not isinstance(initial_power, int):
        raise ValueError("The Input Must Be A Valid int !")

    total_power = initial_power

    def accumulator(ammount: int) -> int:

        if not isinstance(ammount, int):
            raise ValueError("The Input Must Be A Valid int !")
        nonlocal total_power
        total_power += ammount
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:

    if not isinstance(enchantment_type, str):
        raise ValueError("The Input Must Be A Valid string !")

    def enchant(item_name: str) -> str:

        if not isinstance(item_name, str):
            raise ValueError("The Input Must Be A Valid string !")
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> Dict[str, callable]:
    storage = {}

    def store(key: Any, value: Any) -> None:
        storage[key] = value

    def recall(key: Any) -> Any:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    my_counter = mage_counter()

    print("\nTesting mage counter...")
    print("Call 1:", my_counter())
    print("Call 2:", my_counter())
    print("Call 3:", my_counter())

    flaming = enchantment_factory("Flaming")
    sword = flaming("Sword")

    frozen = enchantment_factory("Frozen")
    shield = frozen("Shield")

    print("\nTesting enchantment factory...")
    print(sword)
    print(shield)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
