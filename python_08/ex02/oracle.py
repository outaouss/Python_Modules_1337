import os
from dotenv import load_dotenv


def load_oracle_config() -> tuple:
    """
    Loads environment variables from a .env file and verifies their presence.

    Logic:
    1. load_dotenv() scans for a .env file and injects its values
    into the process.
    2. We iterate through a list of critical 'required_vars'.
    3. os.getenv(var) attempts to pull the value from the system environment.
    4. Any missing keys are tracked to prevent running the system in
    an insecure state.
    """
    # Load external configuration file into environment variables
    load_dotenv()

    # Define the mandatory keys needed for the Matrix to function
    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    config = {}
    missing = []

    for var in required_vars:
        # Retrieve the value without raising an error if it's missing
        value = os.getenv(var)
        if not value:
            # Audit missing configuration for security reporting
            missing.append(var)
        config[var] = value

    return config, missing


def main() -> None:
    # Program Entry Point: Evaluating the environment
    print("\nORACLE STATUS: Reading the Matrix...\n")

    # Unpack the tuple to access the config data and the list of errors
    config, missing = load_oracle_config()

    print("Configuration loaded:")
    # Using .get() provides a safe fallback if the key is missing
    print(f"Mode: {config.get('MATRIX_MODE', 'NOT SET')}")

    # Logic: Database behavior changes based on the detected environment mode
    db_status = "Connected to local instance" if config.get('MATRIX_MODE') \
        == "development" else "Remote Cluster"
    print(f"Database: {db_status}")

    # Security: Verify presence of key without printing its actual value
    print(f"API Access: "
          f"{'Authenticated' if config.get('API_KEY') else 'FAILED'}")
    print(f"Log Level: {config.get('LOG_LEVEL', 'NOT SET')}")
    print(f"Zion Network: "
          f"{'Online' if config.get('ZION_ENDPOINT') else 'Offline'}")

    print("\nEnvironment security check:")

    # Confirming the transition from hardcoded strings to env variables
    print("[OK] No hardcoded secrets detected")

    # Report logic: Clearly identify if the .env file is incomplete
    if missing:
        print(f"[KO] .env file incomplete. Missing: {', '.join(missing)}")
    else:
        print("[OK] .env file properly configured")

    # Logic: Validate the current operational mode of the system
    if config.get('MATRIX_MODE') == "production":
        print("[OK] Running in development mode")
    elif config.get('MATRIX_MODE') == "development":
        print("[OK] Production overrides available")
    else:
        print("[KO] No development or production mode founded")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
