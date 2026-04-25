import argparse
import os
import shutil

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def _is_id_column(series):
    return series.nunique() == len(series)


def _is_discrete_column(series):
    if series.nunique() > 10:
        return False
    return pd.api.types.is_integer_dtype(series) or (series.dropna() % 1 == 0).all()


def generate_histograms(df):
    numeric_columns = [
        col for col in df.select_dtypes(include="number").columns
        if not _is_id_column(df[col]) and not _is_discrete_column(df[col])
    ]

    for column in numeric_columns:
        fig, ax = plt.subplots(figsize=(6, 4))

        ax.hist(df[column].dropna(), bins=20, edgecolor="white", color="steelblue")

        mean = df[column].mean()
        median = df[column].median()
        ax.axvline(mean, color="red", linestyle="--", linewidth=1.2, label=f"Mean: {mean:.2f}")
        ax.axvline(median, color="orange", linestyle="-", linewidth=1.2, label=f"Median: {median:.2f}")

        ax.set_title(f"{column} Distribution")
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        ax.legend()
        ax.grid(axis="y", alpha=0.4)

        fig.tight_layout()
        fig.savefig(f"output/{column}_histogram.png")
        plt.close(fig)


def _save_bar_chart(counts, column):
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(counts.index.astype(str), counts.values, color="steelblue", edgecolor="white")

    for bar, value in zip(bars, counts.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            str(value),
            ha="center", va="bottom", fontsize=9
        )

    ax.set_title(f"{column} Count")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    ax.grid(axis="y", alpha=0.4)
    plt.xticks(rotation=45, ha="right")

    fig.tight_layout()
    fig.savefig(f"output/{column}_bar.png")
    plt.close(fig)


def generate_bar_charts(df):
    # カテゴリ列
    for column in df.select_dtypes(include="str").columns:
        if df[column].nunique() <= 20:
            _save_bar_chart(df[column].value_counts(), column)

    # 離散数値列（0/1 や 1/2/3 など）
    for column in df.select_dtypes(include="number").columns:
        if not _is_id_column(df[col := column]) and _is_discrete_column(df[column]):
            _save_bar_chart(df[column].value_counts().sort_index(), column)


def generate_heatmap(df):
    numeric_df = df.select_dtypes(include="number").loc[
        :, [col for col in df.select_dtypes(include="number").columns
            if not _is_id_column(df[col])]
    ]

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        ax=ax
    )
    ax.set_title("Correlation Heatmap")

    fig.tight_layout()
    fig.savefig("output/correlation_heatmap.png")
    plt.close(fig)


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

    numeric_columns = [
        col for col in df.select_dtypes(include="number").columns
        if not _is_id_column(df[col])
    ]

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

    print("\n=== Generating Charts ===")
    if os.path.exists("output"):
        shutil.rmtree("output")
    os.makedirs("output")
    generate_histograms(df)
    generate_bar_charts(df)
    generate_heatmap(df)
    print("Charts saved to output/")


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
