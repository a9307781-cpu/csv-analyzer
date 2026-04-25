import argparse
import pandas as pd


def analyze_csv(file_path):
    # CSV読み込み
    df = pd.read_csv(file_path)

    print("\n=== Basic Statistics ===")

    # 数値列だけ取得
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        print(f"\n{column}")

        print(f"平均: {df[column].mean():.2f}")
        print(f"中央値: {df[column].median():.2f}")
        print(f"最大: {df[column].max()}")
        print(f"最小: {df[column].min()}")
        print(f"欠損値: {df[column].isnull().sum()}")


def main():
    parser = argparse.ArgumentParser(
        description="CSV Analyzer"
    )

    parser.add_argument(
        "csv_file",
        help="Path to CSV file"
    )

    args = parser.parse_args()

    analyze_csv(args.csv_file)


if __name__ == "__main__":
    main()
