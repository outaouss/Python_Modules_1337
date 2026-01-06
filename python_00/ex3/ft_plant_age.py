def ft_plant_age():
    Days = int(input("Enter plant age in daye: "))

    if Days > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")

def main():
    ft_plant_age()

main()