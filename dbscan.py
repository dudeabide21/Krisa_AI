import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Generate synthetic leaf feature data
np.random.seed(42)
n_samples = 300

# Healthy leaves: tight cluster, low RGB intensity, low texture variance
healthy = np.random.normal(loc=[0.3, 0.2], scale=0.1, size=(100, 2))
# Bacterial infection: spread cluster, high RGB intensity
bacterial = np.random.normal(loc=[0.7, 0.6], scale=0.15, size=(100, 2))
# Fungal infection: distinct cluster, moderate variance
fungal = np.random.normal(loc=[0.5, 0.8], scale=0.12, size=(80, 2))
# Outliers (noise, rare diseases)
outliers = np.random.uniform(low=0, high=1, size=(20, 2))

# Combine data
X = np.vstack([healthy, bacterial, fungal, outliers])

# Standardize features
X_scaled = StandardScaler().fit_transform(X)

# Apply DBSCAN
db = DBSCAN(eps=0.2, min_samples=10).fit(X_scaled)
labels = db.labels_  # Cluster labels (-1 for noise)

# Plotting
plt.figure(figsize=(10, 6))
unique_labels = set(labels)
colors = ["blue", "green", "red", "purple", "orange"]  # Colors for clusters
for k, col in zip(unique_labels, colors[: len(unique_labels)]):
    if k == -1:
        col = "black"  # Noise points
        label = "Noise (Outliers)"
    else:
        label = f"Cluster {k} ({'Healthy' if k == 0 else 'Bacterial' if k == 1 else 'Fungal'})"

    # Plot points in this cluster
    mask = labels == k
    plt.scatter(X[mask, 0], X[mask, 1], c=col, s=50, label=label, alpha=0.6)

# Labels and title
plt.xlabel("Mean RGB Intensity (Normalized)")
plt.ylabel("Texture Variance (Normalized)")
plt.title("DBSCAN Clustering for Leaf Disease Detection (KRISA Tower)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.annotate(
    "Potential Disease Clusters",
    xy=(0.7, 0.6),
    xytext=(0.8, 0.8),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
plt.tight_layout()
plt.savefig("dbscan_leaf_disease_clusters.png", dpi=300, bbox_inches="tight")
plt.show()
