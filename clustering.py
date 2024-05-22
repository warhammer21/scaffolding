from sklearn.cluster import KMeans
import numpy as np

def cluster_data(data):
    # Ensure the input is a NumPy array
    data = np.array(data)
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)
    return kmeans.labels_
