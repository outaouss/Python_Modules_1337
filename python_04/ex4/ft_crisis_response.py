def crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        file_name = "lost_archive.txt"
        with open(file_name, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    
    try:
        file_name = "classified_data.txt"
        with open(file_name, 'r') as file:
            data = file.read()
            print(data, "\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    
    try:
        file_name = "standard_archive.txt"
        with open(file_name, 'r') as file:
            data = file.read()
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        print(f"SUCCESS: Archive recovered - ``{data}''")
        print("STATUS: Normal operations resumed\n")
    except Exception as e:
        print(e)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()