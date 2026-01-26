    high_score = []
        player for player, score in player_table.items() if score > 2000]

    all_scores = list(player_table.values())
    doubled_scores = set()
    seen = set()

    for s in all_scores:
        if s in seen:
            doubled_scores.add(s)
        else:
            seen.add(s)

    active_players = [
        player for player, score in player_table.items() if score > 0]

    print("- High scorers ( >2000 ):", high_score)
    if doubled_scores:
        print("- Scores doubled :", list(doubled_scores))
    else:
        print("- Scores doubled : None")
    print("- Active players:", active_players)