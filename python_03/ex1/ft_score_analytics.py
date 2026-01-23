import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    argv = sys.argv
    scores = []

    if (len(argv) == 1):
        print(f"No scores provided. Usage: python3 "
              f"{argv[0]} <score1> <score2> ...")
    else:
        for i in range(1, len(argv)):
            try:
                scores += [int(argv[i])]
            except ValueError:
                print(f"oops, I typed '{argv[i]}' insted of a number !!!")
                return None

        print("Scores processed:", scores)
        print("Total players:", len(scores))

        total_score = sum(scores)
        range_list = max(scores) - min(scores)
        count = len(scores)

        print("Total score:", total_score)
        print("Average score:", total_score / count)
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", range_list)


if __name__ == "__main__":
    score_analytics()
