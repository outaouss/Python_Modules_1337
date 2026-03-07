from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any, Dict, List


def spell_reducer(spells: List[int], operation: str) -> int:

    if not isinstance(spells, List) or not isinstance(operation, str):
        raise ValueError("Error: Input Must Be, List And str")

    ops = {
        'add': add,
        'multiply': mul,
        'max': max,
        'min': min
    }

    if operation not in ops:
        raise ValueError(f"Operation '{operation}' is not supported")

    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> Dict[str, Callable]:
    if not callable(base_enchantment):
        raise ValueError(f"{base_enchantment} is not callable !")

    return {
            'fire_enchant': partial(base_enchantment, 50, 'fire'),
            'ice_enchant': partial(base_enchantment, 50, 'ice'),
            'lightning_enchant': partial(base_enchantment, 50, 'lightning')
        }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if n <= 1:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:

    @singledispatch
    def cast_spell(spell: Any) -> str:
        return f"Unknown spell type: {type(spell).__name__}"

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Casting a damage spell with {spell} power!"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Applying the '{spell}' enchantment!"

    @cast_spell.register(list)
    def _(spell: list) -> str:
        return f"Multi-casting sequence: {', '.join(map(str, spell))}"

    return cast_spell
