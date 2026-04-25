# csv-analyzer

CSVファイルを渡すだけで、統計分析・グラフ生成・ML予測を自動で行うPython CLIツールです。

A Python CLI tool that automatically analyzes CSV files — statistics, charts, and ML prediction.

---

## Features

- 基本統計量の出力（平均・中央値・最大・最小・欠損値）
- 自動分析コメント（分布の偏りや欠損値を日本語で説明）
- グラフ生成（ヒストグラム・棒グラフ・相関ヒートマップ）
- ML予測（`--predict` で任意の列をターゲットにランダムフォレスト分類）

## Technologies

- Python / pandas / matplotlib / seaborn / scikit-learn

## Setup

```bash
git clone git@github.com:a9307781-cpu/csv-analyzer.git
cd csv-analyzer

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

**分析のみ：**
```bash
python analyzer.py sample_data/titanic.csv
```

**ML予測あり：**
```bash
python analyzer.py sample_data/titanic.csv --predict Survived
```

## Example Output

```
=== Basic Statistics ===

Age
平均: 29.70
中央値: 28.00
最大: 80.0
最小: 0.42
欠損値: 177

📝 Analysis
平均値が中央値より大きいため、右裾が長い分布の可能性があります。
⚠️ 欠損値が 19.9% あります。

=== ML Prediction: Survived ===

正答率 (Accuracy): 81.0%
学習データ: 712件 / テストデータ: 179件

特徴量の重要度 (Top 10):
  Sex_male                            0.113  ████
  Fare                                0.085  ███
  Age                                 0.077  ███
```

## Demo Images

### Histogram — 数値列の分布と平均・中央値

![Histogram](images/histogram.png)

### Bar Chart — カテゴリ列の件数

![Bar Chart](images/bar_chart.png)

### Heatmap — 列間の相関

![Heatmap](images/heatmap.png)
