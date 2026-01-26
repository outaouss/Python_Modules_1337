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
    high_score = []
    score_doubled = []
    active_players = []

    for player in player_table['players']:
        if player['score'] > 2000:
            high_score += [player['name']]
        if player['status'] == 'active':
            active_players += [player['name']]
        score_doubled += [player['score'] * 2]
    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {score_doubled}")
    print(f"Active players: {active_players}")


def dict_comprhension(player_table: dict):
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
        ''
    }
    print("Player scores:", player_scores)
    print("Score categories:", scores_categories)
    print("Achievement counts:", achiv_counts)


if __name__ == "__main__":
    try:
        print("=== Game Analytics Dashboard ===\n")
        data = data_base()
        list_comprehension(data)
        dict_comprhension(data)
    except Exception as e:
        print(e)
