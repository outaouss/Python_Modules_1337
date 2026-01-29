def write_into_file():
    try:
        data = ("[ENTRY 001] New quantum algorithm discovered\n"
                "[ENTRY 002] Efficiency increased by 347%\n"
                "[ENTRY 003] Archived by Data Archivist trainee\n")
        file_name = "new_discovery.txt"
        file = open(file_name, 'w')
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
        print("Initializing new storage unit:", file_name)
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        file.write(data)
        print(data)
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
        file.close()
    except FileNotFoundError:
        print("Error: File Not Found")
    except Exception:
        print("- Error: Unexpected Error !!!")


if __name__ == "__main__":
    write_into_file()
