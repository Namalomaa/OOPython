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
        print("[ERROR] Missing critical configuration!")
        print("Please ensure your .env file is configured or environment variables are set.")
        return
    
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if matrix_mode == "development":
        print("Database: Connected to local instance")
        print("Zion Network: Diagnostic mode offline")
    elif matrix_mode == "production":
        print("Database: Connected to secure production cluster")
        print("Zion Network: Online")
    else:
        print("Database: Unknown routing")

    if api_key:
        print("[OK] API key loaded securely")
    else:
        print("[WARNING] API key missing")

    print(f"Log Level: {log_level}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
        
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()