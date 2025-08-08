import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Number of simulations
n = 10000

# -------------------------------
# GIGA AR INFRA (Scenario 2)
# -------------------------------
tam_ar = np.random.triangular(0.14, 0.15, 0.17, n)                     # TAM ($B)
uptake_ar = np.random.triangular(0.315, 0.35, 0.385, n)                # Uptake Rate (%)
loan_pct_ar = np.random.triangular(0.72, 0.80, 0.88, n)                # Loan % of Claim
charge_rate_ar = np.random.triangular(0.027, 0.03, 0.033, n)           # GIGA's Charge Rate (%)

# Revenue = TAM × Uptake × Loan % × Charge Rate
revenue_ar = tam_ar * uptake_ar * loan_pct_ar * charge_rate_ar

# -------------------------------
# GIGA HNPL (Scenario 2)
# -------------------------------
tam_hnpl = np.random.triangular(9.14, 10.15, 11.17, n)                 # TAM ($B)
uptake_hnpl = np.random.triangular(0.18, 0.20, 0.22, n)                # Uptake Rate (%)
loan_pct_hnpl = np.random.triangular(0.72, 0.80, 0.88, n)              # Loan % of Claim
charge_rate_hnpl = np.random.triangular(0.027, 0.03, 0.033, n)         # GIGA's Charge Rate (%)

# Revenue = TAM × Uptake × Loan % × Charge Rate
revenue_hnpl = tam_hnpl * uptake_hnpl * loan_pct_hnpl * charge_rate_hnpl

# -------------------------------
# TOTAL FINANCIAL INFRA REVENUE
# -------------------------------
total_financial_infra = revenue_ar + revenue_hnpl

# -------------------------------
# RESULTS & SUMMARY
# -------------------------------
results = pd.DataFrame({
    "GIGA AR Infra": revenue_ar,
    "GIGA HNPL": revenue_hnpl,
    "Total Infra Revenue": total_financial_infra
})

summary = results.describe(percentiles=[0.05, 0.5, 0.95])
print("=== GIGA Financial Infra Revenue Simulation Summary ===")
print(summary[["GIGA AR Infra", "GIGA HNPL", "Total Infra Revenue"]])

# -------------------------------
# OPTIONAL: Visualization
# -------------------------------
plt.figure(figsize=(10, 6))
plt.hist(total_financial_infra, bins=50, color='orchid', edgecolor='black')
plt.title("Total Financial Infra Revenue Distribution (2025)")
plt.xlabel("Revenue ($B)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
