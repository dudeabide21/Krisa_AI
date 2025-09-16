import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate synthetic leaf feature data
np.random.seed(42)
n_samples = 500
# Features: mean RGB intensity, texture variance, edge density, lesion area
healthy_features = np.random.normal(loc=[0.3, 0.2, 0.1, 0.05], scale=0.1, size=(250, 4))
diseased_features = np.random.normal(
    loc=[0.7, 0.6, 0.5, 0.4], scale=0.15, size=(250, 4)
)
X = np.vstack([healthy_features, diseased_features])
feature_names = [
    "Mean RGB Intensity",
    "Texture Variance",
    "Edge Density",
    "Lesion Area",
]
df = pd.DataFrame(X, columns=feature_names)

# Step 2: Compute correlation matrix
corr_matrix = df.corr(method="pearson")

# Step 3: Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    center=0,
    fmt=".2f",
    square=True,
    cbar_kws={"label": "Correlation Coefficient"},
)
plt.title(
    "Correlation Heatmap of Leaf Features for Disease Detection\n(Smart Krishi Tower)"
)
plt.tight_layout()
plt.savefig("leaf_feature_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()

# Step 4: Create formal correlation table
corr_table = corr_matrix.reset_index().melt(
    id_vars="index", var_name="Feature 2", value_name="Correlation (%)"
)
corr_table = corr_table.rename(columns={"index": "Feature 1"})
corr_table["Correlation (%)"] = (corr_table["Correlation (%)"] * 100).round(2)
corr_table["Description"] = corr_table.apply(
    lambda x: f"Correlation between {x['Feature 1']} and {x['Feature 2']} for leaf disease detection.",
    axis=1,
)

# Filter out redundant pairs (e.g., A-B and B-A) and self-correlations
corr_table = corr_table[corr_table["Feature 1"] < corr_table["Feature 2"]]
corr_table = corr_table[["Feature 1", "Feature 2", "Correlation (%)", "Description"]]

# Save to CSV
corr_table.to_csv("leaf_feature_correlation_table.csv", index=False)

# Print table for verification
print("Formal Correlation Table for Leaf Feature Analysis:")
print(corr_table)
