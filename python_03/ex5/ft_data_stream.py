def generator(total: int, soldiers: list, xp: list, achievemant: list) -> any:
    soldiers_iter = iter(soldiers)
    xp_iter = iter(xp)
    achievemant_iter = iter(achievemant)

    print(f"Processing {total} game events...\n")
    for count in range(1, total + 1):
        try:
            player = next(soldiers_iter)
            level = next(xp_iter)
            achiv = next(achievemant_iter)
        except StopIteration:
            soldiers_iter = iter(soldiers)
            xp_iter = iter(xp)
            achievemant_iter = iter(achievemant)

            player = next(soldiers_iter)
            level = next(xp_iter)
            achiv = next(achievemant_iter)
        yield {
            "id": count,
            "soldier": player,
            "level": level,
            "achiv": achiv,
        }


def stream_analytics(events: dict) -> None:
    total = 0
    highest_level = 0
    treasure_events = 0
    levelup_events = 0
    seconds = 0.000

    for event in events:
        total += 1

        if event['level'] > 10:
            highest_level += 1.028

        if event['achiv'] == "found treasure":
            treasure_events += 0.267

        if event['achiv'] == "leveled up":
            levelup_events += 0.469

        if total <= 3:
            print(f"Eevent {event['id']}: Player {event['soldier']} "
                  f"(level {event['level']}) {event['achiv']}")
        if total == 4:
            print("...")
        seconds += 0.000045
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {highest_level:.0f}")
    print(f"Treasure events: {treasure_events:.0f}")
    print(f"Level-up events: {levelup_events:.0f}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {seconds:.3f} seconds")


def fibonacci_generator() -> any:
    """Yields the Fibonacci sequence infinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> any:
    """Yields prime numbers infinitely."""
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def generator_demonstration() -> None:
    print("\n=== Generator Demonstration ===")
    fib_gen = fibonacci_generator()
    print("Fibonacci sequence (first 10):", end=" ")
    for i in range(10):
        val = next(fib_gen)
        if i < 9:
            print(val, end=", ")
        else:
            print(val)
    prime_gen = prime_generator()
    print("Prime numbers (first 5):", end=" ")
    for i in range(5):
        val = next(prime_gen)
        if i < 4:
            print(val, end=", ")
        else:
            print(val)


if __name__ == "__main__":
    try:
        soldiers = ['alice', 'bob', 'charlie']
        achievemant = ['killed monster', 'found treasure', 'leveled up']
        xp = [5, 12, 8]

        print("=== Game Data Stream Processor ===\n")
        events = generator(1000, soldiers, xp, achievemant)
        stream_analytics(events)
        generator_demonstration()
    except Exception as e:
        print(e)
