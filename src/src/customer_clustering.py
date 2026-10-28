import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# -----------------------------------
# Load RFM data
# -----------------------------------
df = pd.read_csv(
    "outputs/customer_analysis/customer_rfm.csv"
)


# -----------------------------------
# Select ML features
# -----------------------------------
features = [
    "recency",
    "frequency",
    "monetary"
]

X = df[features].copy()


# -----------------------------------
# Scale the data
# -----------------------------------
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# -----------------------------------
# Find best number of clusters
# -----------------------------------
inertias = []
silhouette_scores = []

k_values = range(2, 8)

for k in k_values:

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    inertias.append(model.inertia_)

    silhouette_scores.append(
        silhouette_score(X_scaled, labels)
    )


# -----------------------------------
# Choose best K using silhouette score
# -----------------------------------
best_k = list(k_values)[
    silhouette_scores.index(
        max(silhouette_scores)
    )
]

print("=" * 60)
print("K-MEANS CUSTOMER CLUSTERING")
print("=" * 60)

print("\nSilhouette scores:")

for k, score in zip(k_values, silhouette_scores):
    print(f"K = {k}: {score:.4f}")

print(f"\nBest number of clusters: {best_k}")


# -----------------------------------
# Train final K-Means model
# -----------------------------------
kmeans = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(X_scaled)


# -----------------------------------
# Cluster summary
# -----------------------------------
cluster_summary = df.groupby("cluster").agg(
    customers=("customer_id", "count"),
    avg_recency=("recency", "mean"),
    avg_frequency=("frequency", "mean"),
    avg_monetary=("monetary", "mean")
).round(2)


print("\nCluster Summary:")
print(cluster_summary)


# -----------------------------------
# Save results
# -----------------------------------
os.makedirs(
    "outputs/customer_analysis",
    exist_ok=True
)

df.to_csv(
    "outputs/customer_analysis/customer_clusters.csv",
    index=False
)

cluster_summary.to_csv(
    "outputs/customer_analysis/cluster_summary.csv"
)


# -----------------------------------
# Create cluster evaluation chart
# -----------------------------------
plt.figure(figsize=(10, 6))

plt.plot(
    list(k_values),
    silhouette_scores,
    marker="o"
)

plt.title("K-Means Cluster Evaluation")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Silhouette Score")
plt.xticks(list(k_values))

plt.tight_layout()

plt.savefig(
    "outputs/customer_analysis/"
    "kmeans_silhouette.png"
)

plt.close()


print("\nFiles saved:")
print("- customer_clusters.csv")
print("- cluster_summary.csv")
print("- kmeans_silhouette.png")