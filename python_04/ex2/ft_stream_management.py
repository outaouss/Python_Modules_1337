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
    print(f"[STANDARD] Archie status from {val_1}: {val_2}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication "
          "channels verified", file=sys.stderr)
    print("[STANDARD] Data transimission complete", file=sys.stdout)
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    stream_managemant()
