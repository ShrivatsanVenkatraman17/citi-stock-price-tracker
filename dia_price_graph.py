import re
import pandas as pd
import matplotlib.pyplot as plt

# Paste the output copied from your Java program here
java_output = """
2026-10-12T22:38:09.492996945Z | DIA price: 517.84998
2026-10-12T22:36:41.629826672Z | DIA price: 517.84998
2026-10-12T22:36:56.800752359Z | DIA price: 517.84998
"""

# Extract timestamps and prices
matches = re.findall(
    r"([0-9T:.+\-Z]+)\s+\|\s+DIA price:\s*([0-9.]+)",
    java_output
)

# Create a DataFrame
df = pd.DataFrame(matches, columns=["timestamp", "price"])

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["price"] = df["price"].astype(float)

# Sort by timestamp
df = df.sort_values("timestamp")

# Plot the prices
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["price"], marker="o")

plt.title("DIA Price Over Time")
plt.xlabel("Timestamp")
plt.ylabel("DIA Price ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
