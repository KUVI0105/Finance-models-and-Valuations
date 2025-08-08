import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Number of simulations
n = 10000

# -------------------------------
# GIGA GPO (AR Infra) Monte Carlo Simulation
# -------------------------------

# Inputs from scenario table
# TAM ($B)
tam_gpo = np.random.triangular(12.12, 13.46, 14.81, n)

# Uptake Rate (%)
uptake_rate = np.random.triangular(0.315, 0.35, 0.385, n)

# Capture Rate (%)
capture_rate = np.random.triangular(0.225, 0.25, 0.275, n)

# GIGA's Charge Rate (%)
charge_rate = np.random.triangular(0.027, 0.03, 0.033, n)

# Revenue formula
# Revenue = TAM × Uptake × Capture × UpfrontLoan% × GIGA Charge Rate
revenue_gpo = tam_gpo * uptake_rate * capture_rate * charge_rate

# -------------------------------
# RESULTS & SUMMARY
# -------------------------------

results_gpo = pd.DataFrame({
    "TAM": tam_gpo,
    "Uptake Rate": uptake_rate,
    "Capture Rate": capture_rate,
    "GIGA Charge Rate": charge_rate,
    "Revenue ($B)": revenue_gpo
})

# Display summary stats
summary = results_gpo.describe(percentiles=[0.05, 0.5, 0.95])
print("=== GIGA GPO Monte Carlo Simulation Summary ===")
print(summary[["Revenue ($B)"]])

# -------------------------------
# OPTIONAL: Histogram
# -------------------------------
plt.figure(figsize=(10, 6))
plt.hist(revenue_gpo, bins=50, color='salmon', edgecolor='black')
plt.title("GIGA GPO Revenue Distribution (2025)")
plt.xlabel("Revenue ($B)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
