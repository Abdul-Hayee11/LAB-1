# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'SDN_traffic.csv'  # Adjust this to your file location
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure
print("Dataset Preview:")
print(data.head())

# Group the data by 'category' and calculate the mean of relevant metrics
category_group = data.groupby('category').mean(numeric_only=True)

# Display the summary of traffic metrics for different categories
print("\nTraffic Summary by Category (forward_pc, reverse_size_packets, reverse_duration):")
print(category_group[['forward_pc', 'reverse_size_packets', 'reverse_duration']].sort_values(by='forward_pc', ascending=False))

# Calculate the correlation matrix for the numeric columns
correlation_matrix = data[['forward_pc', 'forward_bc', 'reverse_size_packets', 'reverse_duration']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Plot the correlation matrix
plt.figure(figsize=(8, 6))
plt.title('Correlation Matrix of Traffic Metrics', fontsize=14)
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar(label='Correlation coefficient')

# Displaying the correlation values on the heatmap
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix.columns)):
        plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}", ha="center", va="center", color="black")

plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.tight_layout()
plt.show()
