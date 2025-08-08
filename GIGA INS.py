import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Number of simulations
n = 10000

# -------------------------------
# TECHNOLOGY (2025) Monte Carlo Simulation
# -------------------------------

# Input distributions from scenario table
tam_tech = np.random.triangular(93.37, 103.75, 114.12, n)          # TAM ($B)
capture_tech = np.random.triangular(0.09, 0.10, 0.11, n)           # Capture Rate (%)
charge_tech = np.random.triangular(0.0266, 0.0295, 0.0325, n)      # GIGA Charge Rate (%)

# Revenue = TAM × Capture × Charge × 1000 (convert to $M)
revenue_tech = tam_tech * capture_tech * charge_tech * 1000

# Create DataFrame
results = pd.DataFrame({
    "TAM ($B)": tam_tech,
    "Capture Rate (%)": capture_tech,
    "Charge Rate (%)": charge_tech,
    "Revenue ($M)": revenue_tech
})

# Summary statistics
summary = results.describe(percentiles=[0.05, 0.5, 0.95])
print("=== Technology Revenue Simulation (2025) ===")
print(summary[["Revenue ($M)"]])

# -------------------------------
# OPTIONAL: Plot Distribution
# -------------------------------
plt.figure(figsize=(10, 6))
plt.hist(revenue_tech, bins=50, color='lightgreen', edgecolor='black')
plt.title("Technology Revenue Distribution (2025)")
plt.xlabel("Revenue ($M)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
