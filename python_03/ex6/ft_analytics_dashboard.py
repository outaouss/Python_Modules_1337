def data_base() -> dict:
    infos = {
        'players': [
            {
                'name': 'alice',
                'achi': {'first_kill', 'level_10', 'treasure_hunter',
                         'speed_demon'
                         },
                'score': 2300,
                'region': 'north',
                'status': 'active'
            },
            {
                'name': 'bob',
                'achi': {'first_kill', 'level_10', 'boss_slayer', 'collector'},
                'score': 1800,
                'region': 'east',
                'status': 'active'
            },
            {
                'name': 'charlie',
                'achi': {
                        'level_10', 'treasure_hunter', 'boss_slayer',
                        'speed_demon',
                        'perfectionist'
                        },
                'score': 2150,
                'region': 'central',
                'status': 'active'
            },
            {
                'name': 'diana',
                'achi': {
                        'level_10', 'treasure_hunter',
                        'speed_demon',
                        'perfectionist'
                        },
                'score': 2050,
                'region': 'central',
                'status': 'inactive'
            },
        ],
    }
    return infos


def list_comprehension(player_table: dict) -> None:
    print("=== List Comprehension Examples ===")
    high_score = [
        player['name'] for player in player_table['players']
        if player['score'] > 2000]
    score_doubled = [
        player['score'] * 2 for player
        in player_table['players']]
    active_players = [
        player['name'] for player in player_table['players']
        if player['status'] == 'active']

    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {score_doubled}")
    print(f"Active players: {active_players}")


def dict_comprhension(player_table: dict) -> None:
    print("\n=== Dict Comprehension Examples ===")

    player_scores = {
        player['name']: player['score']
        for player in player_table['players']
        if player['status'] == 'active'
    }

    scores_categories = {
        'high': len([player for player in player_table['players']
                     if player['score'] > 2000]),
        'medium': len([player for player in player_table['players']
                       if 1900 <= player['score'] <= 2000]),
        'low': len([player for player in player_table['players'] if
                    player['score'] < 1900])
    }

    achiv_counts = {
        player['name']: len(player['achi'])
        for player in player_table['players']
    }
    print("Player scores:", player_scores)
    print("Score categories:", scores_categories)
    print("Achievement counts:", achiv_counts)


def set_comprehension(player_table: dict) -> None:
    print("\n=== Set Comprehension Examples ===")

    unique_player = set(player['name'] for player in player_table['players'])
    unique_achiv = set(one for player in player_table['players']
                       for one in player['achi'])
    active_regions = set(player['region'] for player in player_table['players'])

    print("Unique players:", unique_player)
    print("Unique achievemants:", unique_achiv)
    print("Active regions:", active_regions)


def combined_analys(player_table: dict) -> None:
    print("\n=== Combined Analysis ===")

    total_players = [player['name'] for player in player_table['players']]
    unique_achive = set([one for player in player_table['players']
                         for one in player['achi']])
    average_score = [sum(player['score'] for player
                         in player_table['players']) / len(total_players)]

    top_score = [max(player['score'] for player in player_table['players'])]
    best_player = [player for player in player_table['players']
                   if player['score'] == top_score[0]]

    print("Total players:", len(total_players))
    print("Total unique achievemants:", len(unique_achive))
    print("Average score:", average_score[0])
    print(f"Top performer: {best_player[0]['name']} "
          f"({best_player[0]['score']} points, "
          f"{len(best_player[0]['achi'])} achievements)")


if __name__ == "__main__":
    try:
        print("=== Game Analytics Dashboard ===\n")
        data = data_base()
        list_comprehension(data)
        dict_comprhension(data)
        set_comprehension(data)
        combined_analys(data)
    except Exception as e:
        print(e)
