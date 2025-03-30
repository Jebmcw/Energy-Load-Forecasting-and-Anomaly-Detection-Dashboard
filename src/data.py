import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate 72 hours of hourly data
n_hours = 72
timestamps = [datetime(2024, 3, 1) + timedelta(hours=i) for i in range(n_hours)]
usage = np.random.normal(10, 2, size=n_hours).clip(min=0)  # ← fixed typo: "clips" → "clip"
temperature = np.random.normal(65, 5, size=n_hours)

# Build DataFrame
df = pd.DataFrame({
    'customer_id': [1] * n_hours,  # All for customer 1
    'timestamp': timestamps,
    'usage_kwh': usage,            # ← column name correction
    'temperature': temperature
})

# Save to CSV
df.to_csv('data/load_data.csv', index=False)

