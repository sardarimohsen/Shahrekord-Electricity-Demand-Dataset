# The Shahrekord Electricity Demand Dataset
---
[![Scientia Iranica](https://img.shields.io/badge/Paper-Scientia%20Iranica-blue)](https://doi.org/10.24200/sci.2021.56343.4673)


## 📊 The Shahrekord Electricity Demand Dataset

The core contribution of this repository is the open release of the **The Shahrekord Electricity Demand Dataset**, a high-dimensional, fine-grained benchmark designed for short-term load forecasting (STLF). 

### **Dataset Overview**
* **Location:** Shahrekord, Iran.
* **Duration:** 4 Full Years (March 3, 2015 – March 3, 2019).
* **Temporal Resolution:** 1-hour intervals (recorded hourly).
* **Total Samples:** 30,768 unique hourly observations.
* **Dimensionality:** 23 distinct determinants + 1 target variable (actual load value).

### **Data Breakdown and Determinants**
The dataset decouples electricity usage dynamics from exogenous determinants across 23 input variables:

#### 1. Meteorological Variables (19 determinant sequences)
The meteorological variables capture the continuous physical and environmental dependencies of electricity consumption:
* **Temperature:** Minimum, Maximum, and Mean hourly readings (°C).
* **Humidity:** Minimum, Maximum, and Mean relative values (%).
* **Precipitation:** Rainfall, Total Rainfall, Snowfall, and Snow Height.
* **Wind Profiles:** Dynamic wind speed and direction recorded at specific intervals (03:00, 09:00, 15:00) alongside daily maximum gusts.

#### 2. Temporal & Categorical Variables (6 dummy determinants)
To eliminate the need for complex data clustering, categorical temporal features are embedded directly as dummy variables:
* **Holiday Status:** Binary classification (Holiday vs. Regular day) to capture human behavior shifts.
* **Weekly Periodicity:** Day of the week classified into 7 discrete steps.
* **Daily Periodicity:** 24 hours of the day modeled by a dummy variable with 3 classes (low, moderate, and high load type).
* **Seasonal Periodicity:** Month number and day of the month to capture continuous intra-year trends.

#### 3. Target Output
* **Hourly Load Demand (MW):** Precise real-time electricity load consumption.

### **Benchmark Splitting Strategy**
To maintain strict experimental validity, the dataset is pre-divided chronologically:
* **Training & Validation Set:** The first 75% of samples (Years 1, 2, and 3), totaling **23,076 samples**.
* **Test Set:** The remaining 25% (Year 4), totaling **7,692 samples**.

---

## 📚 Publications

This dataset serves as the experimental baseline for the following two research papers:

### 1. ParDeeB: A Graph Framework for Load Forecasting Based on Parallel DeepNet Branches
* **Journal:** *Scientia Iranica*, 2021.
* **Authors:** Najmeh Neshat, Mohsen Sardari Zarchi, Hashem Mahlooji.
* **Core Idea:** Introduces **ParDeeB**, an acyclic graph deep learning framework. It handles the multimodal nature of the Shahrekord dataset by directing temporal sequences through parallel subnetwork branches (LSTM for long-term historical dependencies, GRU for meteorological sequences, and Dense layers for static/categorical data) before merging via a concatenated layer.

### 2. Application of Deep Learning Models Based on Fully-Connected and Recurrent Neural Networks to Residual Peak Load Forecasting
* **Journal:** *Sharif Journal of Industrial Engineering & Management*, 2020.
* **Authors:** N. Neshat, M. Sardari Zarchi, H. Mahlooji.
* **Core Idea:** Investigates the direct application of standard and stacked Fully-Connected (Dense) and Recurrent Neural Network architectures to forecast the underlying residual and peak load profiles of the Shahrekord region.

---

## ⚙️ Model Framework: The ParDeeB DAG Architecture

The optimal implementation derived in the research leverages the parallel processing capabilities of the directed acyclic graph (DAG) structure:

```text
 ┌────────────────────────────────────────────────────────┐
 │                      INPUT DATA                        │
 └──────────────────────────┬─────────────────────────────┘
                            │
       ┌────────────────────┼────────────────────┐
       ▼                    ▼                    ▼
 ┌───────────┐        ┌───────────┐        ┌───────────┐
 │ Branch 1  │        │ Branch 2  │        │ Branch 3  │
 │ (LSTM)    │        │ (GRU)     │        │ (Dense)   │
 └─────┬─────┘        └─────┬─────┘        └─────┬─────┘
       │                    │                    │
       └────────────────────┼────────────────────┘
                            ▼
                    ┌───────────────┐
                    │ Concatenation │
                    └───────┬───────┘
                            ▼
                    ┌───────────────┐
                    │  Dense Output │
                    └───────────────┘
```

* **Branch 1 (LSTM):** Resolves long-term temporal trends in historical load demand (Lookback = 168 hours, Step = 1).
* **Branch 2 (GRU):** Captures short-term exogenous shifts in 19 weather determinants (Lookback = 7 days, Step = 24 hours).
* **Branch 3 (Dense):** Directly integrates static categorical/dummy temporal markers.

---

## 📂 Repository Structure
```text
├── data/
│   └── shahrekord_hourly_load.csv  # Full 3-year energy & weather dataset
├── src/
│   ├── model_pardeeb.py           # DAG Multi-Branch implementation
│   ├── classic_rnn.py             # Baseline Fully-Connected & RNN models
│   └── preprocessing.py           # Z-score normalization & windowing
└── README.md
```

---

## 📄 Citation

If the code or dataset provided in this repository assists your research, please cite the following papers:

```bibtex
@article{neshat2021pardeeb,
  title={ParDeeB: A Graph Framework for Load Forecasting Based on Parallel DeepNet Branches},
  author={Neshat, Najmeh and Zarchi, Mohsen Sardari and Mahlooji, Hashem},
  journal={Scientia Iranica},
  volume={28},
  number={6},
  pages={3551--3567},
  year={2021},
  doi={10.24200/sci.2021.56343.4673}
}

@article{neshat2020application,
  title={Application of Deep Learning Models Based on Fully-Connected and Recurrent Neural Networks to Residual Peak Load Forecasting},
  author={Neshat, N. and Sardari Zarchi, M. and Mahlooji, H.},
  journal={Sharif Journal of Industrial Engineering \& Management},
  volume={36},
  number={1.2},
  pages={103--111},
  year={2020}
}
```

