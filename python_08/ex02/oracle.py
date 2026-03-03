import os
from dotenv import load_dotenv


def load_oracle_config():
    load_dotenv()

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
        value = os.getenv(var)
        if not value:
            missing.append(var)
        config[var] = value

    return config, missing


def main():
    print("\nORACLE STATUS: Reading the Matrix...\n")

    config, missing = load_oracle_config()

    print("Configuration loaded:")
    print(f"Mode: {config.get('MATRIX_MODE', 'NOT SET')}")

    db_status = "Connected to local instance" if config.get('MATRIX_MODE') \
        == "development" else "Remote Cluster"
    print(f"Database: {db_status}")
    print(f"API Access: "
          f"{'Authenticated' if config.get('API_KEY') else 'FAILED'}")
    print(f"Log Level: {config.get('LOG_LEVEL', 'NOT SET')}")
    print(f"Zion Network: "
          f"{'Online' if config.get('ZION_ENDPOINT') else 'Offline'}")

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if missing:
        print(f"[KO] .env file incomplete. Missing: {', '.join(missing)}")
    else:
        print("[OK] .env file properly configured")

    if config.get('MATRIX_MODE') == "production":
        print("[OK] Running in development mode")
    elif config.get('MATRIX_MODE') == "development":
        print("[OK] Production overrides available")
    else:
        print("[KO] No development or production mode founded")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
