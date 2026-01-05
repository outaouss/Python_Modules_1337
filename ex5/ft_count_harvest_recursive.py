# First Way Bla Recursion Jus Loop -->

def ft_count_harvest_recursive():
    Days = int(input("Days untill harvest: "))

    for count in range(1, Days + 1):
        print(f"Day {count}")
    print("Harvest time!")

# Secone Way B Recursion -->

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def counter(n):
        if n > 0:
            counter(n - 1)
            print(f"Day {n}")

    counter(days)
    print("Harvest time!")

# def main():
#     ft_count_harvest_recursive()

# main()
