import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
# Ensure the file '94_95_96_97_all .csv' is in your working directory
file_path = '94_95_96_97_all .csv'
df = pd.read_csv(file_path)

# 2. Split the data based on the 'YEAR' column
# Years 1, 2, and 3 are for Training; Year 4 is for Testing
train_data = df[df['YEAR'].isin([1.0, 2.0, 3.0])]
test_data = df[df['YEAR'] == 4.0]

print(f"Training samples: {len(train_data)}")
print(f"Testing samples: {len(test_data)}")

# 3. Visualize the Train/Test Split
plt.figure(figsize=(15, 6))

# Plotting the 'Demand' target variable
plt.plot(train_data.index, train_data['Demand'], label='Train (Years 1-3)', color='blue', alpha=0.7)
plt.plot(test_data.index, test_data['Demand'], label='Test (Year 4)', color='orange', alpha=0.8)

# Formatting the plot
plt.title('Shahrekord Electricity Demand: Train vs Test Split', fontsize=14)
plt.xlabel('Time (Hourly Index)', fontsize=12)
plt.ylabel('Demand (MW)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
