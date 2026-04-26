<div id="top"></div>

<div align="center">

# csv-analyzer

<table>
  <thead>
    <tr>
      <th align="center">English</th>
      <th align="center"><a href="README_ja.md">日本語</a></th>
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

**Stop writing boilerplate. Just pass a CSV — and get statistics, charts, and ML predictions in one command.**

[Quick Start](#setup) · [Features](#features) · [Examples](#output-examples) · [Roadmap](#roadmap)

<table>
  <tr>
    <td><img src="images/histogram.png" alt="Histogram" width="260"></td>
    <td><img src="images/bar_chart.png" alt="Bar Chart" width="260"></td>
    <td><img src="images/heatmap.png" alt="Heatmap" width="260"></td>
  </tr>
  <tr>
    <td align="center">Histogram</td>
    <td align="center">Bar Chart</td>
    <td align="center">Heatmap</td>
  </tr>
</table>

</div>

---

## Table of Contents

1. [About](#about)
2. [Features](#features)
3. [Built With](#built-with)
4. [Setup](#setup)
5. [Usage](#usage)
6. [Output Examples](#output-examples)
7. [Directory Structure](#directory-structure)
8. [Roadmap](#roadmap)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [License](#license)
12. [Author](#author)

---

## About

> Every time I started a data analysis project, I found myself writing the same setup code over and over — loading CSVs with pandas, drawing histograms with matplotlib, wiring up sklearn... This tool automates all of that with one command, so I can focus on what the data actually says.

csv-analyzer is a Python CLI tool that automatically runs **statistical analysis**, **chart generation**, and **ML prediction** from any CSV file.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Features

| Feature | Description |
|---------|-------------|
| 📊 Basic Statistics | Mean, median, max, min, and missing value count per column |
| 💬 Auto Analysis Comments | Detects skewness (right/left tail) and high missing rates in plain language |
| 📈 Chart Generation | Histograms, bar charts, and a correlation heatmap saved to `output/` |
| 🤖 ML Prediction | Random Forest classification on any target column via `--predict` |

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Built With

| Library | Version |
| ------- | ------- |
| Python | 3.13+ (tested on 3.13) |
| pandas | 3.0.2 |
| matplotlib | 3.10.9 |
| seaborn | 0.13.2 |
| scikit-learn | 1.8.0 |
| numpy | 2.4.4 |

See `requirements.txt` for the full list of dependencies.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Setup

### Prerequisites

- Python 3.13+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/a9307781-cpu/csv-analyzer.git
cd csv-analyzer

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

> [!NOTE]
> If you see `ModuleNotFoundError`, the virtual environment is likely not activated. Run `source venv/bin/activate` first.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Usage

### Basic syntax

```bash
python analyzer.py <csv_file> [--predict TARGET_COLUMN]
```

### Options

| Argument | Required | Description |
|----------|:--------:|-------------|
| `csv_file` | ✅ | Path to the CSV file to analyze |
| `--predict TARGET_COLUMN` | — | Target column name for Random Forest classification |

### Examples

```bash
# Statistics + charts only
python analyzer.py sample_data/titanic.csv

# With ML prediction
python analyzer.py sample_data/titanic.csv --predict Survived
```

Charts are automatically saved to `output/` after each run.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Output Examples

### Terminal Output

```
=== Basic Statistics ===

Age
Mean:    29.70
Median:  28.00
Max:     80.0
Min:     0.42
Missing: 177

📝 Analysis
Mean is greater than median — the distribution may have a right-skewed tail.

=== ML Prediction: Survived ===

Accuracy: 81.0%
Train: 712 samples / Test: 179 samples

Feature Importances (Top 10):
  Sex_male                            0.113  ████
  Fare                                0.085  ███
  Age                                 0.077  ███
```

### Charts

<table>
  <tr>
    <th>Histogram</th>
    <th>Bar Chart</th>
  </tr>
  <tr>
    <td><img src="images/histogram.png" alt="Histogram" width="380"></td>
    <td><img src="images/bar_chart.png" alt="Bar Chart" width="380"></td>
  </tr>
  <tr>
    <th colspan="2">Correlation Heatmap</th>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="images/heatmap.png" alt="Heatmap" width="500"></td>
  </tr>
</table>

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Directory Structure

```
csv-analyzer/
├── analyzer.py          ← Main script
├── requirements.txt     ← Dependencies
├── README.md            ← English
├── README_ja.md         ← Japanese
├── images/              ← Demo images for README
│   ├── histogram.png
│   ├── bar_chart.png
│   └── heatmap.png
├── sample_data/
│   └── titanic.csv      ← Sample dataset
└── output/              ← Auto-generated charts on each run (gitignored)
```

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Roadmap

- [x] CSV loading and basic statistics
- [x] Auto analysis comments
- [x] Chart generation (histogram, bar chart, heatmap)
- [x] ML prediction (`--predict` flag)
- [ ] Regression prediction support
- [ ] Multi-CSV comparison analysis
- [ ] HTML report export

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'pandas'`

Your virtual environment is not activated. Run:

```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### `Error: Column '<name>' not found.`

The column name passed to `--predict` does not exist in the CSV. Check the spelling against the CSV headers.

### Charts are not generated

Make sure the `output/` directory is writable. Note that `output/` is automatically deleted and recreated on every run.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Contributing

Contributions are welcome!

1. Fork this repository
2. Create your branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

---

## License

[MIT](https://opensource.org/licenses/MIT)

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Author

**a9307781-cpu**

- GitHub: [@a9307781-cpu](https://github.com/a9307781-cpu)

<p align="right">(<a href="#top">back to top</a>)</p>
