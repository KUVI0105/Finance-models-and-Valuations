import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Number of simulations
n = 10000

# -------------------------------
# CARE NAVIGATION (Triangular Distribution)
# -------------------------------
tam_cn = np.random.triangular(8.93, 9.92, 10.91, n)             # TAM ($B)
capture_rate_cn = np.random.triangular(0.31, 0.35, 0.38, n)     # Capture Rate
charge_rate_cn = np.random.triangular(0.045, 0.05, 0.055, n)    # Charge Rate

revenue_cn = tam_cn * capture_rate_cn * charge_rate_cn

# -------------------------------
# CONCIERGE (Triangular Distribution)
# -------------------------------
tam_con = np.random.triangular(0.90, 1.00, 1.10, n)              # TAM ($B)
capture_rate_con = np.random.triangular(0.32, 0.34, 0.35, n)     # Capture Rate
charge_rate_con = np.random.triangular(1000, 1050, 1100, n)      # ARPU (INR)

ar_con = capture_rate_con * charge_rate_con
revenue_con = tam_con * ar_con / 8300  # Convert INR to USD ($B)

# -------------------------------
# LONG TERM CARE (Triangular Distribution)
# -------------------------------
tam_ltc = np.random.triangular(5.40, 6.00, 6.60, n)              # TAM ($B)
capture_rate_ltc = np.random.triangular(0.225, 0.250, 0.275, n)
charge_rate_ltc = np.random.triangular(0.027, 0.030, 0.033, n)

revenue_ltc = tam_ltc * capture_rate_ltc * charge_rate_ltc

# -------------------------------
# TOTAL REVENUE
# -------------------------------
total_revenue = revenue_cn + revenue_con + revenue_ltc

# -------------------------------
# RESULTS & SUMMARY
# -------------------------------
results = pd.DataFrame({
    "Care Navigation": revenue_cn,
    "Concierge": revenue_con,
    "Long-Term Care": revenue_ltc,
    "Total Revenue": total_revenue
})

# Summary statistics
summary = results.describe(percentiles=[0.05, 0.5, 0.95])

# Print summary
print("=== Monte Carlo Simulation Summary ===")
print(summary[["Care Navigation", "Concierge", "Long-Term Care", "Total Revenue"]])

# -------------------------------
# OPTIONAL: Visualization
# -------------------------------
plt.figure(figsize=(10, 6))
plt.hist(total_revenue, bins=50, color='skyblue', edgecolor='black')
plt.title("Total Revenue Distribution (2025) - Giga Health")
plt.xlabel("Revenue ($B)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
