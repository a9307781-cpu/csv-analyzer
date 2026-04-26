<div id="top"></div>

<div align="center">

# csv-analyzer

<table>
  <thead>
    <tr>
      <th align="center"><a href="README.md">English</a></th>
      <th align="center">日本語</th>
    </tr>
  </thead>
</table>

<p>
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
  <img src="https://img.shields.io/badge/-pandas-150458.svg?logo=pandas&style=for-the-badge&logoColor=white">
  <img src="https://img.shields.io/badge/-scikit--learn-F7931E.svg?logo=scikit-learn&style=for-the-badge&logoColor=white">
  <img src="https://img.shields.io/badge/-matplotlib-11557c.svg?logo=python&style=for-the-badge&logoColor=white">
  <img src="https://img.shields.io/badge/-seaborn-4c72b0.svg?logo=python&style=for-the-badge&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge">
</p>

**毎回書くボイラープレートをなくす。CSVを渡すだけで、統計・グラフ・ML予測を1コマンドで。**

[クイックスタート](#セットアップ) · [機能一覧](#機能) · [出力例](#出力例) · [ロードマップ](#ロードマップ)

<table>
  <tr>
    <td><img src="images/histogram.png" alt="Histogram" width="260"></td>
    <td><img src="images/bar_chart.png" alt="Bar Chart" width="260"></td>
    <td><img src="images/heatmap.png" alt="Heatmap" width="260"></td>
  </tr>
  <tr>
    <td align="center">ヒストグラム</td>
    <td align="center">棒グラフ</td>
    <td align="center">相関ヒートマップ</td>
  </tr>
</table>

</div>

---

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [機能](#機能)
3. [使用技術](#使用技術)
4. [セットアップ](#セットアップ)
5. [使用方法](#使用方法)
6. [出力例](#出力例)
7. [ディレクトリ構成](#ディレクトリ構成)
8. [ロードマップ](#ロードマップ)
9. [トラブルシューティング](#トラブルシューティング)
10. [貢献方法](#貢献方法)
11. [ライセンス](#ライセンス)
12. [著者](#著者)

---

## プロジェクトについて

> データ分析を始めるたびに、pandas で読み込んで、matplotlib でグラフを書いて…という同じセットアップコードを毎回書いていました。このツールはその手間を 1 コマンドで自動化し、データの中身にすぐ集中できることを目指して作りました。

csv-analyzer は CSV ファイルを渡すだけで **統計分析・グラフ生成・ML予測** を自動実行するPython CLIツールです。

<p align="right">(<a href="#top">トップへ</a>)</p>

---

## 機能

| 機能 | 説明 |
|------|------|
| 📊 基本統計量の出力 | 平均・中央値・最大・最小・欠損値を列ごとに表示 |
| 💬 自動分析コメント | 分布の偏り（右裾・左裾）や欠損率を日本語で説明 |
| 📈 グラフ自動生成 | ヒストグラム・棒グラフ・相関ヒートマップを `output/` に保存 |
| 🤖 ML予測 | `--predict` で任意の列をターゲットにランダムフォレスト分類 |

<p align="right">(<a href="#top">トップへ</a>)</p>

---

## 使用技術

| ライブラリ | バージョン |
| ---------- | ---------- |
| Python | 3.13以上（3.13で動作確認済み） |
| pandas | 3.0.2 |
| matplotlib | 3.10.9 |
| seaborn | 0.13.2 |
| scikit-learn | 1.8.0 |
| numpy | 2.4.4 |

その他の依存パッケージは `requirements.txt` を参照してください。

<p align="right">(<a href="#top">トップへ</a>)</p>

---

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

> [!NOTE]
> `ModuleNotFoundError` が出る場合は、仮想環境が有効化されていない可能性があります。`source venv/bin/activate` を先に実行してください。

<p align="right">(<a href="#top">トップへ</a>)</p>

---

## 使用方法

### 基本構文

```bash
python analyzer.py <csv_file> [--predict TARGET_COLUMN]
```

### オプション一覧

| 引数 | 必須 | 説明 |
|------|:----:|------|
| `csv_file` | ✅ | 分析対象のCSVファイルのパス |
| `--predict TARGET_COLUMN` | — | ML分類のターゲット列名 |

### 実行例

```bash
# 統計分析＋グラフ生成のみ
python analyzer.py sample_data/titanic.csv

# ML予測あり
python analyzer.py sample_data/titanic.csv --predict Survived
```

グラフは実行後に `output/` ディレクトリへ自動保存されます。

<p align="right">(<a href="#top">トップへ</a>)</p>

---

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

### グラフ

<table>
  <tr>
    <th>ヒストグラム</th>
    <th>棒グラフ</th>
  </tr>
  <tr>
    <td><img src="images/histogram.png" alt="Histogram" width="380"></td>
    <td><img src="images/bar_chart.png" alt="Bar Chart" width="380"></td>
  </tr>
  <tr>
    <th colspan="2">相関ヒートマップ</th>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="images/heatmap.png" alt="Heatmap" width="500"></td>
  </tr>
</table>

<p align="right">(<a href="#top">トップへ</a>)</p>

---

## ディレクトリ構成

```
csv-analyzer/
├── analyzer.py          ← メインスクリプト
├── requirements.txt     ← 依存ライブラリ
├── README.md            ← 英語版
├── README_ja.md         ← 日本語版
├── images/              ← README用デモ画像
│   ├── histogram.png
│   ├── bar_chart.png
│   └── heatmap.png
├── sample_data/
│   └── titanic.csv      ← サンプルデータ
└── output/              ← 実行時に自動生成されるグラフ（gitignore済み）
```

<p align="right">(<a href="#top">トップへ</a>)</p>

---

## ロードマップ

- [x] CSV 読み込み・基本統計量の出力
- [x] 自動分析コメント（日本語）
- [x] グラフ生成（ヒストグラム・棒グラフ・ヒートマップ）
- [x] ML 予測（`--predict` フラグ）
- [ ] 回帰予測への対応
- [ ] 複数 CSV の比較分析
- [ ] HTML レポートの出力

<p align="right">(<a href="#top">トップへ</a>)</p>

---

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

---

## 貢献方法

コントリビューション歓迎です！

1. このリポジトリをフォーク
2. ブランチを作成 (`git checkout -b feature/YourFeature`)
3. 変更をコミット (`git commit -m 'Add YourFeature'`)
4. ブランチをプッシュ (`git push origin feature/YourFeature`)
5. プルリクエストを作成

<p align="right">(<a href="#top">トップへ</a>)</p>

---

## ライセンス

[MIT](https://opensource.org/licenses/MIT)

<p align="right">(<a href="#top">トップへ</a>)</p>

---

## 著者

**a9307781-cpu**

- GitHub: [@a9307781-cpu](https://github.com/a9307781-cpu)

<p align="right">(<a href="#top">トップへ</a>)</p>
