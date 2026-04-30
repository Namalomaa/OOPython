def check_dependency() -> None:
    try:
        import pandas
        print("[OK] pandas (2.1.0) - Data manipulation ready")
    except ImportError:
        print("[MISSING] pandas (2.1.0) - Data manipulation ready")
    try:
        import numpy
        print("[OK] numpy (1.25.0) - Numerical computation ready")
    except ImportError:
        print("[MISSING] numpy (1.25.0) - Numerical computation ready")
    try:
        import requests
        print("OK] requests (2.31.0) - Network access ready")
    except ImportError:
        print("[MISSING]] requests (2.31.0) - Network access ready")