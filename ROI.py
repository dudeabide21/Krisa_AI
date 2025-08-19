import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([0, 1, 2, 3, 4, 5])
investment = 20100  # NPR
annual_benefit = 19440  # NPR per year
maintenance_per_year = 1000  # NPR
cumulative_benefits = np.array([0, 19440, 38880, 58320, 77760, 97200])  # Gross benefits
cumulative_maintenance = np.array(
    [0, 1000, 2000, 3000, 4000, 5000]
)  # Cumulative maintenance
net_profits = (
    cumulative_benefits - cumulative_maintenance - investment
)  # Net profit after costs
annual_net_benefits = np.array(
    [0, 19440 - 1000, 19440 - 1000, 19440 - 1000, 19440 - 1000, 19440 - 1000]
)  # Annual benefits minus maintenance

# Plot 1: Bar Plot of Annual Net Benefits
plt.figure(figsize=(10, 6))
plt.bar(
    years[1:],
    annual_net_benefits[1:],
    color="skyblue",
    edgecolor="black",
    label="Annual Net Benefit (NPR)",
)
plt.axhline(
    y=investment,
    color="red",
    linestyle="--",
    alpha=0.5,
    label=f"Initial Investment ({investment} NPR)",
)
plt.xlabel("Years")
plt.ylabel("Annual Net Benefit (NPR)")
plt.title("Annual Benefits of Smart Krishi Tower (5 Ropani Rice Farm)")
plt.grid(True, axis="y", linestyle="--", alpha=0.7)
plt.legend()
plt.annotate(
    "Payback ~1 Year",
    xy=(1, investment),
    xytext=(1.5, investment + 5000),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
plt.tight_layout()
plt.show()

# Plot 2: Line Plot of Cumulative Benefits and Costs
plt.figure(figsize=(10, 6))
plt.plot(
    years,
    cumulative_benefits,
    color="green",
    marker="o",
    label="Cumulative Gross Benefits (NPR)",
)
plt.plot(
    years,
    cumulative_maintenance,
    color="orange",
    marker="s",
    label="Cumulative Maintenance Costs (NPR)",
)
plt.plot(
    years, net_profits, color="blue", marker="d", label="Cumulative Net Profit (NPR)"
)
plt.axhline(y=0, color="red", linestyle="--", alpha=0.5, label="Break-even Point")
plt.xlabel("Years")
plt.ylabel("Amount (NPR)")
plt.title("Cumulative Financial Flows of Smart Krishi Tower")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.annotate(
    "Payback ~1 Year",
    xy=(1, 0),
    xytext=(1.5, 10000),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
plt.tight_layout()
plt.show()

# Plot 3: Area Plot of Cumulative Net Profit
plt.figure(figsize=(10, 6))
plt.fill_between(
    years,
    net_profits,
    where=(net_profits >= 0),
    color="green",
    alpha=0.4,
    label="Positive Net Profit (NPR)",
)
plt.fill_between(
    years,
    net_profits,
    where=(net_profits < 0),
    color="red",
    alpha=0.4,
    label="Negative Net Profit (NPR)",
)
plt.axhline(y=0, color="black", linestyle="-", alpha=0.5, label="Break-even Point")
plt.xlabel("Years")
plt.ylabel("Cumulative Net Profit (NPR)")
plt.title("ROI Growth of Smart Krishi Tower (5 Ropani Rice Farm)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.annotate(
    "Payback ~1 Year",
    xy=(1, 0),
    xytext=(1.5, 10000),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
plt.tight_layout()
plt.show()
