
# Shahrekord Electricity Demand Dataset

This directory contains the hourly electricity consumption and meteorological dataset for Shahrekord, Iran, spanning from 2015 to 2018.

---

## 📂 Data File
The primary dataset is located in:
**`94_95_96_97_all .csv`**

## 📊 Dataset Structure
The dataset is chronologically organized to support time-series forecasting research:
*   **Training & Validation Set:** Years 1, 2, and 3 (approximately 23,076 hourly samples).
*   **Test Set:** Year 4 (approximately 7,692 hourly samples).

---

## 📋 Feature Definitions

### **Target Variable**
*   **`Demand`**: The actual hourly electricity demand/consumption value.

### **Temporal & Administrative Features**
*   **`Load`**: Specifies the type of **peak hours** as categorized by the government (e.g., low, moderate, and high load periods).
*   **`Holiday`**: Binary variable indicating public holidays.
*   **`Weekday`**: Categorical index for the day of the week.
*   **`YEAR`**: Numerical index for the four-year study period.
*   **`Month Num` / `Day of Month` / `Hour`**: Specific time markers for each observation.

### **Meteorological Features**
| Column Name | Full Description | Unit/Type |
| :--- | :--- | :--- |
| **`Min Tem`** | **Minimum Temperature** | °C |
| **`Max Tem`** | **Maximum Temperature** | °C |
| **`avr tem`** | **Average Temperature** | °C |
| **`min hum`** | **Minimum** Humidity | % |
| **`max hum`** | **Maximum** Humidity | % |
| **`avr hum`** | **Average** Humidity | % |
| **`rain`** | Rain precipitation | mm |
| **`snow`** | Snow precipitation | cm |
| **`T precipitation`**| **Total Precipitation** (Rain + Snow) | mm/cm |
| **`snow level`** | Recorded snow accumulation height | cm |

### **Wind (WD/WS) Features**
Wind data is recorded at specific daily intervals (03:00, 09:00, 15:00) and as daily maximums:
*   **`W D`**: Wind Direction (measured in degrees).
*   **`W S`**: Wind Speed (measured in m/s).

---

## 🛠 Usage Guidelines
*   **Splitting Logic:** Ensure the model is trained on the first three years of data and evaluated only on the fourth year to prevent data leakage.
*   **Preprocessing:** It is highly recommended to apply Z-score normalization to all meteorological features and the target `Demand` column to improve model convergence in deep learning frameworks.
