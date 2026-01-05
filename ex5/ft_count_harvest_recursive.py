def ft_count_harvest_recursive():
    Days = int(input("Days untill harvest: "))

    for count in range(1, Days + 1):
        print(f"Day {count}")
    print("Harvest time!")

def main():
    ft_count_harvest_recursive()

main()

# def ft_count_harvest_recursive(n):
#     if n > 0:
#         ft_count_harvest_recursive(n - 1)
#         print(f"Day {n}")

# def main():
#     n = int(input("Enter: "))
#     ft_count_harvest_recursive(n)

# main()