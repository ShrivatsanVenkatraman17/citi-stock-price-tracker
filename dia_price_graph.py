import re
import pandas as pd
import matplotlib.pyplot as plt

java_output = """
2026-10-12T22:38:09.492996945Z | DIA price: 517.84998
2026-10-12T22:36:41.629826672Z | DIA price: 517.84998
2026-10-12T22:36:56.800752359Z | DIA price: 517.84998
"""

matches = re.findall(
    r"([0-9T:.\-]+Z)\s+\|\s+DIA price:\s*([0-9.]+)",
    java_output
)

df = pd.DataFrame(matches, columns=["timestamp", "price"])
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["price"] = df["price"].astype(float)
df = df.sort_values("timestamp")

plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["price"], marker="o")
plt.title("DIA Price Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
