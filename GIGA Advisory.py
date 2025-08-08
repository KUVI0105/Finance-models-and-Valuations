import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Number of simulations
n = 10000

# -------------------------------
# TECHNOLOGY
# -------------------------------
tam_tech = np.random.triangular(2.68, 3.00, 3.27, n)
capture_tech = np.random.triangular(0.32, 0.35, 0.39, n)
charge_tech = np.random.triangular(0.045, 0.05, 0.055, n)
revenue_tech = tam_tech * capture_tech * charge_tech * 1000  # Convert to $M

# -------------------------------
# MARKETING
# -------------------------------
tam_marketing = np.random.triangular(0.42, 0.47, 0.51, n)
capture_marketing = np.random.triangular(0.32, 0.35, 0.39, n)
charge_marketing = np.random.triangular(0.045, 0.05, 0.055, n)
revenue_marketing = tam_marketing * capture_marketing * charge_marketing * 1000

# -------------------------------
# COMPLIANCES
# -------------------------------
tam_compliance = np.random.triangular(0.13, 0.14, 0.16, n)
capture_compliance = np.random.triangular(0.32, 0.35, 0.39, n)
charge_compliance = np.random.triangular(0.045, 0.05, 0.055, n)
revenue_compliance = tam_compliance * capture_compliance * charge_compliance * 1000

# -------------------------------
# SERVICES
# -------------------------------
tam_services = np.random.triangular(16.86, 18.73, 20.61, n)
capture_services = np.random.triangular(0.32, 0.35, 0.39, n)
charge_services = np.random.triangular(0.045, 0.05, 0.055, n)
revenue_services = tam_services * capture_services * charge_services * 1000

# -------------------------------
# TOTAL PLATFORM REVENUE
# -------------------------------
total_platform_revenue = (
    revenue_tech +
    revenue_marketing +
    revenue_compliance +
    revenue_services
)

# -------------------------------
# RESULTS & SUMMARY
# -------------------------------
results = pd.DataFrame({
    "Technology": revenue_tech,
    "Marketing": revenue_marketing,
    "Compliances": revenue_compliance,
    "Services": revenue_services,
    "Total Platform Revenue": total_platform_revenue
})

# Summary stats
summary = results.describe(percentiles=[0.05, 0.5, 0.95])
print("=== GIGA Platform Revenue Simulation Summary ===")
print(summary[["Technology", "Marketing", "Compliances", "Services", "Total Platform Revenue"]])

# -------------------------------
# OPTIONAL: Plot
# -------------------------------
plt.figure(figsize=(10, 6))
plt.hist(total_platform_revenue, bins=50, color='steelblue', edgecolor='black')
plt.title("Total Platform Revenue Distribution (2025)")
plt.xlabel("Revenue ($M)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
