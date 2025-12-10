import pandas as pd
from pathlib import Path

def main():
    # Adjust this path if you downloaded the sample somewhere else
    base_path = Path("data")

    # Note: Ensure you have the parquet files downloaded from Hugging Face
    # Typical path structure shown below
    patents_path = base_path / "patents" / "patents_2025-10.parquet"
    applications_path = base_path / "applications" / "applications_2025-10.parquet"

    # Only run if files exist locally
    if patents_path.exists() and applications_path.exists():
        patents = pd.read_parquet(patents_path)
        applications = pd.read_parquet(applications_path)

        print("Patents sample:")
        print(patents.head())

        print("\nApplications sample:")
        print(applications.head())
    else:
        print("Parquet files not found. Please download from Hugging Face first.")

if __name__ == "__main__":
    main()
