def vault_security() -> None:
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")

        print("SECURE EXTRACTION:")
        with open("classified_data.txt", 'r') as file:
            data = file.read()
            print(data)

        print("\nSECURE PRESERVATION:")
        with open("classified_data.txt", 'a') as file:
            data_1 = "[CLASSIFIED] New security protocols archived"
            file.write("\n" + data_1)
            print(data_1)
        print("Vault automatically sealed upon completion\n")

        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("File Not Found !")
    except Exception:
        print("Error: Unexcpected Error")


if __name__ == "__main__":
    vault_security()
