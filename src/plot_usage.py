import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/load_data.csv', parse_dates=['timestamp'])

# Plot usage
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['usage_kwh'], label='usage (kwh)', color='blue')
plt.title('Simulated Energy Usage Over 72 Hours')
plt.xlabel('Timestamp')
plt.ylabel('Usage (kwh)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('outputs/usage_plot.png')
plt.show()