def achievemant_trucker() -> tuple:
    try:
        print("=== Achievement Tracker System ===\n")
        first = {
            "name": "alice",
            "achievemant": {'first_kill', 'level_10', 'treasure_hunter',
                            'speed_demon'}}
        seconde = {
            "name": "bob",
            "achievemant": {'first_kill', 'level_10', 'boss_slayer',
                            'collector'}}
        third = {"name": "charlie",
                 "achievemant": {'level_10', 'treasure_hunter', 'boss_slayer',
                                 'speed_demon', 'perfectionist'}}

        total = first, seconde, third

        for player in total:
            print("Player", player['name'],
                  "achievemants:", player['achievemant'])
        return total

    except (Exception) as e:
        print("Error:", e)


def achievemant_analytics(total: tuple) -> None:
    try:
        print("\n=== Achievement Analytics ===")

        all_unique = set().union(total[0]['achievemant'],
                                 total[1]['achievemant'],
                                 total[2]['achievemant'])

        print("All unique achievements:", all_unique)
        print("Total unique achievements:", len(all_unique))

        p_01 = total[0]['achievemant']
        p_02 = total[1]['achievemant']
        p_03 = total[2]['achievemant']

        common = p_01.intersection(p_02, p_03)

        rare_first = p_01.difference(p_02.union(p_03))
        rare_seconde = p_02.difference(p_01.union(p_03))
        rare_third = p_03.difference(p_01.union(p_02))

        rare = rare_first.union(rare_seconde, rare_third)

        print("\nCommon to all players:", common)
        print("Rare achievements (1 player):", rare)

        player_01 = total[0]['name']
        player_02 = total[1]['name']

        player_01_unique = p_01.difference(p_02)
        player_02_unique = p_02.difference(p_01)

        print(f"\n{player_01.capitalize()} vs {player_02.capitalize()} "
              f"common: {p_01.intersection(p_02)}")
        print(f"{player_01.capitalize()} unique: {player_01_unique}")
        print(f"{player_02.capitalize()} unique: {player_02_unique}")

    except (Exception) as e:
        print("Error during analytics:", e)


if __name__ == "__main__":
    total = achievemant_trucker()
    achievemant_analytics(total)
