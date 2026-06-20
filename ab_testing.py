import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load data
df = pd.read_csv("marketing_data.csv")

print("Dataset:")
print(df)

# Separate groups
group_a = df[df["Group"] == "A"]["Converted"]
group_b = df[df["Group"] == "B"]["Converted"]

# Perform T-Test
t_stat, p_value = ttest_ind(group_a, group_b)

print("\nT-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Significant difference between groups")
else:
    print("No significant difference between groups")

# Conversion rates
conversion_rates = df.groupby("Group")["Converted"].mean()

print("\nConversion Rates:")
print(conversion_rates)

# Plot
conversion_rates.plot(kind="bar")
plt.title("Conversion Rate Comparison")
plt.ylabel("Conversion Rate")
plt.savefig("conversion_chart.png")
plt.show()