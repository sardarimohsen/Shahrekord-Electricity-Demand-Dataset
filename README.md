# ParDeeB: A Graph Framework for Load Forecasting Based on Parallel DeepNet Branches

[![Paper](https://img.shields.io/badge/Paper-Scientia%20Iranica-blue)](https://doi.org/10.24200/sci.2021.56343.4673)
[![Python](https://img.shields.io/badge/Python-3.7+-green.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)

This repository hosts the official implementation and dataset for the **ParDeeB** framework introduced in the paper:  
**"ParDeeB: A Graph Framework for Load Forecasting Based on Parallel DeepNet Branches"**.

Read the full paper here: **[Scientia Iranica Publication](https://doi.org/10.24200/sci.2021.56343.4673)**.

---

## 📌 Abstract
Energy demand forecasting is at the heart of energy management. Due to its complex, non-linear nature and long-term historical dependency, standard deep network models are not always robust against different historical dependencies. To tackle this challenge, **ParDeeB** proposes a novel graph framework based on parallel DeepNet branches. It uses multiple parallel branches where different types of networks (e.g., RNNs, LSTMs, GRUs, or Dense networks) process individual determinants depending on their specific historical behavior. This directed acyclic graph structure leads to significantly higher accuracy and generalization over state-of-the-art models.

---

## 🗺 Framework Architecture

ParDeeB features an acyclic graph topology that accommodates diverse sequences of varying lengths:
- **Branch 1 (Sequence Recurrent):** Typically handles historical load demand using an **LSTM** layer. Designed for long sequence lengths (e.g., lookback = 168 hours, time-step $d = 1$) to capture long-term patterns perfectly.
- **Branch 2 (Exogenous Sequence Recurrent):** Models temporal sequences of exogenous climate/weather determinants via a **GRU** layer. Uses daily sampling (lookback = 7 days, time-step $d = 24$) to extract daily trends without overfitting.
- **Branch 3 (Non-Historical Dense):** Accepts non-temporal/calendar dummy determinants (e.g., holiday status, season metrics) using fully connected layers directly without any recurrent components.

All branches are integrated via a **concatenated layer** and passed through a final dense layer to output the forecasted peak load demand.

---

## 📊 Dataset Specifications
The benchmark data consists of hourly peak load demand and weather variables recorded in **Shahrekord, Iran**, from **March 3, 2015, to March 3, 2018**.

| Detail | Specification |
|:---|:---|
| **Timeline** | March 3, 2015 – March 3, 2018 |
| **Total Samples** | 30,768 records |
| **Target Variable** | Hourly Peak Load Demand |
| **Determinants** | 23 Input Determinants (Climate, Calendar, etc.) |

### 🛠 Train-Validation-Test Split
The timeline is split chronologically as follows:
- **Training and Validation (75%):** The first 3 years of sequential samples, containing **23,076 samples**.
- **Test Set (25%):** The remaining 1 year, consisting of **7,692 samples**.

---

## ⚙ Installation & Requirements

Ensure that you have `Python 3.7+` installed. You can install the required packages using the list below:

```bash
pip install tensorflow numpy pandas scikit-learn matplotlib
```

### Required Dependencies
- Python >= 3.7
- TensorFlow / Keras
- Pandas & NumPy
- Scikit-learn (for min-max and Z-score data scaling)

---

## 📂 Repository Structure

The suggested repository layout is organized as follows:

```text
├── data/
│   └── shahrekord_dataset.csv     # Preprocessed hourly case-study data
├── models/
│   └── pardeeb_model.py           # The multi-input parallel graph model definition
├── src/
│   ├── preprocess.py              # Normalization (Z-score) and sequence preparation
│   └── evaluate.py                # Calculations for RMSE and MAPE
├── requirements.txt               # Dependencies listing
├── README.md                      # Project documentation
└── main.py                        # Training and test execution pipeline
```

---

## 🔬 Running the Model

1. **Preprocess Data**: Standardizes variables with Z-score scaling and processes sequence tensors with individual time-steps $d$ and lookbacks $k$.
2. **Execute Training**:
   ```bash
   python main.py --train --model pardeeb
   ```

---

## 📄 Citation

If you use this model or dataset in your research, please cite our paper published in **Scientia Iranica**:

```bibtex
@article{neshat2021pardeeb,
  title={ParDeeB: A Graph Framework for Load Forecasting Based on Parallel DeepNet Branches},
  author={Neshat, Najmeh and Zarchi, Mohsen Sardari and Mahlooji, Hashem},
  journal={Scientia Iranica},
  volume={28},
  number={6},
  pages={3551-3567},
  year={2021},
  publisher={Sharif University of Technology},
  doi={10.24200/sci.2021.56343.4673}
}

@article{neshatapplication,
  title={Application of Deep Learning Models Based on Fully-Connected and Recurrent Neural Networks to Residual Peak Load Forecasting},
  author={Neshat, N and S‌a‌r‌d‌a‌r‌i‌z‌a‌r‌c‌h‌i, M and Mahlooji, H},
  journal={Sharif Journal of Industrial Engineering \& Management},
  volume={36},
  number={1.2},
  pages={103--111},
  year={2020}
}

```
