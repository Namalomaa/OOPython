import importlib


def compare_versions(lib_name: str, installed_version: str,
                     req_version: str, desc: str) -> bool:
    installed = tuple(int(x) for x in installed_version.split(".") if x.isdigit())
    required = tuple(int(x) for x in req_version.split(".") if x.isdigit())

    if installed >= required:
        print(f"[OK] {lib_name} ({installed_version}) - {desc} ready")
        return True
    else:
        print(f"[VERSION CONFLICT] {lib_name} ({installed_version}) is outdated")
        print(f"Need >= {req_version}")
        return False


def check_dependency() -> bool:
    dependencies = {
        'pandas': ('2.1.0', 'Data manipulation'),
        'numpy': ('1.25.0', 'Numerical computation'),
        'requests': ('2.31.0', 'Network access'),
        'matplotlib': ('3.7.2', 'Visualization')
    }
    required = {'pandas', 'numpy', 'matplotlib'}
    imported = set()
    print("Checking dependencies:")
    for lib, (req_version, desc) in dependencies.items():
        try:
            module = importlib.import_module(lib)
            installed_version = module.__version__

            if compare_versions(lib, installed_version, req_version, desc):
                if lib in required:
                    imported.add(lib)
        except ImportError:
            print(f"[MISSING] {lib} - {desc} unavailable")
    if imported == required:
        return True
    return False


def analyze_matrix() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    x = np.arange(1, 1001)
    y = np.random.uniform(0, 100, 1000)

    df = pd.DataFrame({
        'Time': x,
        'Value': y
    })
    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Time'], df['Value'])
    
    plt.title('Matrix Data Analysis')
    plt.xlabel('Time')
    plt.ylabel('Values')

    plt.savefig('matrix_analysis.png')
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    if not check_dependency():
        print("to install missing dependencies run:\n")
        print("using pip:")
        print("pip install -r requirements.txt")
        print("python3 loading.py\n")
        print("Or using poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        return
    analyze_matrix()


if __name__ == "__main__":
    main()
