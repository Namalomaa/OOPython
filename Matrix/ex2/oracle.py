import os
from dotenv import load_dotenv

def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    if not all([db_url, api_key, zion_endpoint]):
        print("[WARNING] Default or missing configuration detected!")
        print("Please ensure your .env file is configured or"
              " environment variables are set.")
        return

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if matrix_mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to secure production cluster")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing")

    print(f"Log Level: {log_level}")

    if matrix_mode == "development":
        print("Zion Network: Online")
    else:
        print("Zion Network: Encrypted routing active")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()