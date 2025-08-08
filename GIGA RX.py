import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Number of simulations
n = 10000

# -------------------------------
# TECHNOLOGY (2025)
# -------------------------------
# TAM ($B), Capture Rate (%), Charge Rate (%)
tam_tech = np.random.triangular(0.41, 0.45, 0.50, n)
capture_tech = np.random.triangular(0.31, 0.35, 0.385, n)
charge_tech = np.random.triangular(0.045, 0.05, 0.055, n)

# Revenue in $M
revenue_tech = tam_tech * capture_tech * charge_tech * 1000

# -------------------------------
# MARKETING (2025)
# -------------------------------
tam_marketing = np.random.triangular(35.78, 39.76, 43.73, n)
capture_marketing = np.random.triangular(0.135, 0.15, 0.165, n)
charge_marketing = np.random.triangular(0.045, 0.05, 0.055, n)

revenue_marketing = tam_marketing * capture_marketing * charge_marketing * 1000  # in $M

# -------------------------------
# TOTAL REVENUE
# -------------------------------
total_revenue = revenue_tech + revenue_marketing

# -------------------------------
# RESULTS
# -------------------------------
results = pd.DataFrame({
    "Technology Revenue ($M)": revenue_tech,
    "Marketing Revenue ($M)": revenue_marketing,
    "Total Revenue ($M)": total_revenue
})

summary = results.describe(percentiles=[0.05, 0.5, 0.95])
print("=== Monte Carlo Simulation Summary ===")
print(summary[["Technology Revenue ($M)", "Marketing Revenue ($M)", "Total Revenue ($M)"]])

# -------------------------------
# OPTIONAL: Plot
# -------------------------------
plt.figure(figsize=(10, 6))
plt.hist(total_revenue, bins=50, color='skyblue', edgecolor='black')
plt.title("Total Revenue Distribution (2025) - Technology + Marketing")
plt.xlabel("Revenue ($M)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
