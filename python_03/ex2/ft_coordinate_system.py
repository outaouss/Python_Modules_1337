import math


def create_tuple(pos_str: str = None) -> tuple | str:
    try:
        if pos_str is None:
            print("Error: Empty Parametre !!!")
            return
        pos_list = pos_str.split(',')
        num = []
        for pos in pos_list:
            clean_num = int(pos)
            num += [clean_num]
        return tuple(num)
    except (ValueError, AttributeError, TypeError):
        return "Error While Creating A Tuple"


def create_position(pos_str: str = None) -> None:
    try:
        if pos_str is None:
            print("oops, No Coordinates Given !")
            return
        pos_list = pos_str.split(',')
        num = [int(pos) for pos in pos_list]
        if len(num) != 3:
            if len(num) > 3:
                print("Error  : Coordinates Dimensions Cannot Be More Then "
                      "[ 3 ]\nExample: (x, y, z)")
            else:
                print("Error  : Coordinates Dimensions Cannot Be Less Than "
                      "[ 3 ]\nExample: (x, y, z)")
            return
        print("Position created:", tuple(num))

        x = num[0]
        y = num[1]
        z = num[2]

        distance = math.sqrt((x-0)**2 + (y-0)**2 + (z-0)**2)
        print(f"Distance between (0, 0, 0) and {num}: {distance:.2F}")
    except (ValueError, AttributeError, TypeError) as e:
        print("Error parsing coordinates:", e)
        print(f'Error details - Type: {type(e).__name__}, Args: ("{e}",)')
        return


def parsing_cordinates(pos_str: str = None) -> None:
    try:
        if pos_str is None:
            print("oops, No Coordinates Given !")
            return
        pos_list = pos_str.split(',')
        num = [int(pos) for pos in pos_list]
        if len(num) != 3:
            if len(num) > 3:
                print("Error  : Coordinates Dimensions Cannot Be More Then "
                      "[ 3 ]\nExample: (x, y, z)")
            else:
                print("Error  : Coordinates Dimensions Cannot Be Less Than "
                      "[ 3 ]\nExample: (x, y, z)")
            return
        x = num[0]
        y = num[1]
        z = num[2]
        print(f'Parsing coordinates: "{x},{y},{z}"')
        print('Parsed position:', tuple(num))

        distance = math.sqrt((x-0)**2 + (y-0)**2 + (z-0)**2)
        print(f"Distance between (0, 0, 0) and {tuple(num)}: {distance}")
    except (ValueError, AttributeError, TypeError) as e:
        print("Error parsing coordinates:", e)
        print(f'Error details - Type: {type(e).__name__}, Args: ("{e}",)')
        return


def unpacking(list_coordinates: tuple = None) -> None:
    x = list_coordinates[0]
    y = list_coordinates[1]
    z = list_coordinates[2]

    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===\n")

        invalid = "abc,def,ghi"
        valid_1 = "10,20,5"
        valid_2 = "3,4,0"

        create_position(valid_1)
        print()

        parsing_cordinates(valid_2)
        print()

        print(f'Parsing invalid coordinates: "{invalid}"')
        create_position(invalid)

        x = create_tuple(valid_2)
        unpacking(x)
    except Exception as e:
        print("Error: ", e)
