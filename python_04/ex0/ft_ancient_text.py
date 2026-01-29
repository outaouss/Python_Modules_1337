def read_file():

    try:
        file = "ancient_fragment.txt"
        read_file = open(file, 'r')
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print("Accessing Storage Vault:", file)
        print("Connection established...\n")
        print("RECOVRED DATA:")
        print(read_file.read())
        print("\nData recovery complete. Storage unit disconnected.")
        read_file.close()
    except FileNotFoundError:
        print("- Error: File Not Found !!!")
    except Exception:
        print("- Error: Unexpected Error !!!")


if __name__ == "__main__":
    read_file()
