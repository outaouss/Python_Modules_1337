import sys


def command_quest():
    print("=== Command Quest ===")

    name = f"Program name: {sys.argv[0]}"
    i = 1
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(name)
    else:
        print(name)
        print("Argument received:", len(sys.argv) - 1)
        for _ in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print("Total arguments:", len(sys.argv))


if __name__ == "__main__":
    command_quest()
