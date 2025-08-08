import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Number of simulations
n = 10000

# -------------------------------
# CONTRACTORS (EoR)
# -------------------------------
# EoR Addressable Market ($B)
eor_market_contractors = np.random.triangular(0.71, 0.79, 0.87, n)
# EoR Capture Rate (%)
capture_rate_contr = np.random.triangular(0.18, 0.20, 0.22, n)
# Take Rate (%)
take_rate_contr = np.random.triangular(0.18, 0.20, 0.22, n)

# Revenue = Market × Capture × Take Rate
revenue_contr = eor_market_contractors * capture_rate_contr * take_rate_contr

# -------------------------------
# VENDORS (EoR)
# -------------------------------
eor_market_vendors = np.random.triangular(0.86, 0.96, 1.05, n)
capture_rate_vendors = np.random.triangular(0.32, 0.35, 0.39, n)
take_rate_vendors = np.random.triangular(0.18, 0.20, 0.22, n)

revenue_vendors = eor_market_vendors * capture_rate_vendors * take_rate_vendors

# -------------------------------
# IT/DEVICES (EoR)
# -------------------------------
eor_market_it = np.random.triangular(1.51, 1.68, 1.85, n)
capture_rate_it = np.random.triangular(0.32, 0.35, 0.39, n)
take_rate_it = np.random.triangular(0.18, 0.20, 0.22, n)

revenue_it = eor_market_it * capture_rate_it * take_rate_it

# -------------------------------
# TOTAL EoR REVENUE
# -------------------------------
total_eor_revenue = revenue_contr + revenue_vendors + revenue_it

# -------------------------------
# RESULTS & SUMMARY
# -------------------------------
results_eor = pd.DataFrame({
    "Contractors": revenue_contr,
    "Vendors": revenue_vendors,
    "IT/Devices": revenue_it,
    "Total EoR Revenue": total_eor_revenue
})

# Summary statistics
summary_eor = results_eor.describe(percentiles=[0.05, 0.5, 0.95])
print("=== GIGA EoR Revenue Simulation Summary ===")
print(summary_eor[["Contractors", "Vendors", "IT/Devices", "Total EoR Revenue"]])

# -------------------------------
# OPTIONAL: Visualization
# -------------------------------
plt.figure(figsize=(10, 6))
plt.hist(total_eor_revenue, bins=50, color='lightgreen', edgecolor='black')
plt.title("Total EoR Revenue Distribution (2025)")
plt.xlabel("Revenue ($B)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
