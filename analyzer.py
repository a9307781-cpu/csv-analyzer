import argparse
import pandas as pd


def generate_comment(df, column):
    mean = df[column].mean()
    median = df[column].median()

    missing_ratio = (
        df[column].isnull().sum() / len(df)
    ) * 100

    comments = []

    if mean > median:
        comments.append(
            "平均値が中央値より大きいため、右裾が長い分布の可能性があります。"
        )
    elif mean < median:
        comments.append(
            "中央値が平均値より大きいため、左裾が長い分布の可能性があります。"
        )
    else:
        comments.append(
            "平均値と中央値が近く、対称的な分布の可能性があります。"
        )

    if missing_ratio > 20:
        comments.append(
            f"⚠️ 欠損値が {missing_ratio:.1f}% あります。"
        )

    return comments


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

        comments = generate_comment(df, column)

        print("\n📝 Analysis")

        for comment in comments:
            print(comment)


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
