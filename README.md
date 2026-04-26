<div id="top"></div>

# csv-analyzer

## 使用技術

<p>
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
  <img src="https://img.shields.io/badge/-pandas-150458.svg?logo=pandas&style=for-the-badge&logoColor=white">
  <img src="https://img.shields.io/badge/-scikit--learn-F7931E.svg?logo=scikit-learn&style=for-the-badge&logoColor=white">
  <img src="https://img.shields.io/badge/-matplotlib-11557c.svg?logo=python&style=for-the-badge&logoColor=white">
  <img src="https://img.shields.io/badge/-seaborn-4c72b0.svg?logo=python&style=for-the-badge&logoColor=white">
</p>

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [機能](#機能)
3. [環境](#環境)
4. [セットアップ](#セットアップ)
5. [使用方法](#使用方法)
6. [出力例](#出力例)
7. [ディレクトリ構成](#ディレクトリ構成)
8. [ロードマップ](#ロードマップ)
9. [トラブルシューティング](#トラブルシューティング)

## プロジェクトについて

CSVファイルを渡すだけで、統計分析・グラフ生成・ML予測を自動で行うPython CLIツールです。

データ分析を始めるとき、毎回「pandas で読み込んで、matplotlib でグラフを書いて…」という準備を手書きする手間がかかります。このツールはその作業を 1 コマンドで自動化し、データの中身にすぐ集中できることを目指して作りました。

<p align="right">(<a href="#top">トップへ</a>)</p>

## 機能

- 📊 **基本統計量の出力** — 平均・中央値・最大・最小・欠損値を列ごとに表示
- 💬 **自動分析コメント** — 分布の偏り（右裾・左裾）や欠損率を日本語で説明
- 📈 **グラフ自動生成** — ヒストグラム・棒グラフ・相関ヒートマップを `output/` に保存
- 🤖 **ML予測** — `--predict` オプションで任意の列をターゲットにランダムフォレスト分類

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境

| ライブラリ      | バージョン |
| --------------- | ---------- |
| Python          | 3.13以上（3.13で動作確認済み）   |
| pandas          | 3.0.2      |
| matplotlib      | 3.10.9     |
| seaborn         | 0.13.2     |
| scikit-learn    | 1.8.0      |
| numpy           | 2.4.4      |

その他の依存パッケージは `requirements.txt` を参照してください。

<p align="right">(<a href="#top">トップへ</a>)</p>

## セットアップ

### 前提条件

- Python 3.13以上
- pip

### インストール手順

```bash
# 1. リポジトリをクローン
git clone https://github.com/a9307781-cpu/csv-analyzer.git
cd csv-analyzer

# 2. 仮想環境を作成・有効化
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 依存関係をインストール
pip install -r requirements.txt
```

<p align="right">(<a href="#top">トップへ</a>)</p>

## 使用方法

### 統計分析＋グラフ生成のみ

```bash
python analyzer.py <CSVファイルのパス>
```

```bash
# サンプルデータで試す
python analyzer.py sample_data/titanic.csv
```

### ML予測あり

```bash
python analyzer.py <CSVファイルのパス> --predict <ターゲット列名>
```

```bash
# Survivedを予測する例
python analyzer.py sample_data/titanic.csv --predict Survived
```

グラフは実行後に `output/` ディレクトリへ自動保存されます。

<p align="right">(<a href="#top">トップへ</a>)</p>

## 出力例

### ターミナル出力

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

=== ML Prediction: Survived ===

正答率 (Accuracy): 81.0%
学習データ: 712件 / テストデータ: 179件

特徴量の重要度 (Top 10):
  Sex_male                            0.113  ████
  Fare                                0.085  ███
  Age                                 0.077  ███
```

### ヒストグラム — 数値列の分布と平均・中央値

![Histogram](images/histogram.png)

### 棒グラフ — カテゴリ列の件数

![Bar Chart](images/bar_chart.png)

### 相関ヒートマップ — 列間の相関係数

![Heatmap](images/heatmap.png)

<p align="right">(<a href="#top">トップへ</a>)</p>

## ディレクトリ構成

```
csv-analyzer/
├── analyzer.py          ← メインスクリプト
├── requirements.txt     ← 依存ライブラリ
├── README.md
├── images/              ← README用デモ画像
│   ├── histogram.png
│   ├── bar_chart.png
│   └── heatmap.png
├── sample_data/
│   └── titanic.csv      ← サンプルデータ
└── output/              ← 実行時に自動生成されるグラフ（gitignore済み）
```

<p align="right">(<a href="#top">トップへ</a>)</p>

## ロードマップ

- [x] CSV 読み込み・基本統計量の出力
- [x] 自動分析コメント（日本語）
- [x] グラフ生成（ヒストグラム・棒グラフ・ヒートマップ）
- [x] ML 予測（`--predict` フラグ）
- [ ] 回帰予測への対応
- [ ] 複数 CSV の比較分析
- [ ] HTML レポートの出力

<p align="right">(<a href="#top">トップへ</a>)</p>

## トラブルシューティング

### `ModuleNotFoundError: No module named 'pandas'`

仮想環境が有効化されていません。以下を実行してください。

```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### `Error: '列名' 列が見つかりません。`

`--predict` で指定した列名がCSVに存在しない場合に発生します。列名のスペルとCSVのヘッダーを確認してください。

### グラフが生成されない

`output/` ディレクトリへの書き込み権限があるか確認してください。既存の `output/` は実行のたびに自動で削除・再作成されます。

<p align="right">(<a href="#top">トップへ</a>)</p>
