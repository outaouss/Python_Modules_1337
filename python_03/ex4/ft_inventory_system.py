import sys


def parse_items() -> dict | str:
    argv = sys.argv

    if len(argv) == 1:
        return "Error: No Arguments Provided"
    else:
        items = {arg.split(':')[0]: arg.split(':')[1] for arg in argv[1:]}
        return items


if __name__ == "__main__":
    try:
        print(parse_items())
        print(len(parse_items().keys()))
    except (Exception) as e:
        print("Error:", e)
