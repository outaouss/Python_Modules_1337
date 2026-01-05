def ft_count_harvest_iterative():
    Days = int(input("Days untill harvest: "))

    for count in range(1, Days + 1):
        print(f"Day {count}")
    print("Harvest time!")

def main():
    ft_count_harvest_iterative()

main()
