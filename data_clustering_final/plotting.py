import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
wcss = []

# Importing the dataset
dataset = pd.read_csv('Big_data.csv')
X = dataset.iloc[:, [3, 4]].values

def plot_function(data):
    Cmeans = KMeans(n_clusters=int(data), init='k-means++', random_state=42)
    y_kmeans = Cmeans.fit_predict(X)

    # Visualising the clusters
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=50, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=50, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=50, c='green', label='Cluster 3')
    plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=50, c='cyan', label='Cluster 4')
    plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=50, c='magenta', label='Cluster 5')
    plt.scatter(Cmeans.cluster_centers_[:, 0], Cmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
    plt.title('Clusters of data ')
    plt.xlabel('component 1 dependent variable')
    plt.ylabel('component 2 independent variable')
    plt.legend()
    plt.show()
    print(Cmeans)
    print(y_kmeans[0])


#plot_function(4)
