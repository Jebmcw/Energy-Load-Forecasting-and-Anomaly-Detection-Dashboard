import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/load_data.csv', parse_dates=['timestamp'])

# Forecast (simple 24-hour moving average)
df['forecast'] = df['usage_kwh'].rolling(window=24, min_periods=1).mean()

# Anomaly detection
df['anomaly'] = abs(df['usage_kwh']- df['forecast']) > 3 # threshold in kwh

# Save output
df.to_csv('data/forecast_results.csv', index=False)

# Plot
plt.figure(figsize=(12,6))
plt.plot(df['timestamp'], df['usage_kwh'], label='Actual usage')
plt.plot(df['timestamp'], df['forecast'], label='Forecast (24 hr MA)', linestyle='--')
plt.scatter(df[df['anomaly']]['timestamp'],df[df['anomaly']]['usage_kwh'], color='red', label='Anomaly')
plt.title('Energy usage Forecast and Anomaly Detection')
plt.xlabel('Time')
plt.ylabel('Usage (kwh)')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/forecast_plot.png')
plt.show()