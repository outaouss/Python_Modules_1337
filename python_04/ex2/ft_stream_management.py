import sys


def stream_managemant() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    val_1 = input("Input Stream active. Enter archivist ID: ")
    val_2 = input("Input Stream active. Enter status report: ")
    print()

    if val_1 == "" and val_2 == "":
        print("Error: No Archivis ID And No Status Report Provided")
        return
    if val_1 == "":
        print("Error No Archivist ID Provided !")
        return
    if val_2 == "":
        print("Error: No Status Report Provided !")
        return

    sys.stdout.write(f"[STANDARD] Archie status from {val_1}: {val_2}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication "
                     "channels verified\n")
    sys.stdout.write("[STANDARD] Data transimission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    stream_managemant()
