from typing import Callable, Tuple, Any, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    if not callable(spell1) or not callable(spell2):
        raise TypeError("The Both Inputs Must Be Callable Functions !")

    def combined_spell(target: str) -> Tuple[Any, Any]:
        res1 = spell1(target)
        res2 = spell2(target)
        return (res1, res2)

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    if not isinstance(multiplier, int) or not callable(base_spell):
        raise ValueError("The Base Spell Must "
                         "Be Callable And The Multiplier Must Be int")

    def amplified_spell(item: dict) -> int:
        base_result = base_spell(item)

        return base_result * multiplier

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    if not callable(condition) or not callable(spell):
        raise ValueError("The Both Inputs Must Be Callable Functions !")

    def wrapper(target: Any) -> Any:

        if condition(target):
            return spell(target)

        return "Spell fizzled"

    return wrapper


def spell_sequence(spells: list[Callable]) -> Callable:

    if not isinstance(spells, list):
        raise ValueError("Input Must Be A List of Callable !")

    def sequence_wrapper(target: Any) -> List[Any]:

        result = []

        for spell in spells:
            result = spell(target)
            result.append(result)

        return result

    return sequence_wrapper


def main() -> None:

    def fireball(target: str):
        return (f"Fireball hits {target}")

    def heal(target: str):
        return (f"Heals {target}")

    combined = spell_combiner(fireball, heal)
    results = combined("Dragon")
    print("\nTesting spell combiner...")
    print(f"Combined spell result: {results[0]}, {results[1]}")

    print("\nTesting power amplifier...")
    dragon = {'name': 'Dragon', "power": 10}

    def fireball(card: dict):
        if isinstance(card, dict):
            return card['power']
        else:
            raise ValueError(f"The {card} is not a dict")

    mega_fireball = power_amplifier(fireball, 3)
    result = mega_fireball(dragon)
    print(f"Original: {fireball(dragon)}, Amplified: {result}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
