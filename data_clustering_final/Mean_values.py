import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA

customers_data = pd.read_csv("dataset.csv")
customers_data = customers_data.drop('CustomerID', axis=1)

encode = LabelEncoder()
encoded_se = encode.fit_transform(customers_data.iloc[:, 0])


customers_data['Genre'] = encoded_se

from sklearn.cluster import KMeans

pca_reducer = PCA(n_components=2)
reduced_data = pca_reducer.fit_transform(customers_data)

from sklearn.cluster import KMeans

km = KMeans(n_clusters=5)

cluster = km.fit(reduced_data)

from kmeans_numpy_improved import *

km_numpy = KMeans_numpy(n_clusters=5, tolerance=0.0001)

clusters, clusterd_data = km_numpy.fit(reduced_data)
clusters = np.array(clusters)

cluster_one_data = np.array(clusterd_data[0])
cluster_two_data = np.array(clusterd_data[1])
cluster_three_data = np.array(clusterd_data[2])
cluster_four_data = np.array(clusterd_data[3])
cluster_five_data = np.array(clusterd_data[4])



full_data_kmeans = KMeans_numpy(n_clusters=5)
centroids, clus_data = full_data_kmeans.fit(customers_data.values)

cluster_1 = pd.DataFrame(clus_data[0], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
cluster_2 = pd.DataFrame(clus_data[1], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
cluster_3 = pd.DataFrame(clus_data[2], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
cluster_4 = pd.DataFrame(clus_data[3], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
cluster_5 = pd.DataFrame(clus_data[4], columns=['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])


def data_write(): 
    
    print("file writing")
    f = open("cluster.txt", "a")

    f.write("Average age for customers in cluster one: " +str((np.array(cluster_1['Age']).mean())))
    f.write("\n")
    f.write("Average age for customers in cluster one:"+str(np.array(cluster_1['Age']).mean()))
    f.write("\n")
    f.write("Average annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_1['Annual Income (k$)']).mean()))
    f.write("\n")
    f.write("Deviation of the mean for annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_1['Annual Income (k$)']).std()))
    f.write("\n")
    f.write("In cluster one we have:  customers"+str(cluster_1.shape[0]))
    f.write("\n")

    f.write("Average age for customers in cluster one: " +str((np.array(cluster_2['Age']).mean())))
    f.write("\n")
    f.write("Average age for customers in cluster one:"+str(np.array(cluster_2['Age']).mean()))
    f.write("\n")
    f.write("Average annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_2['Annual Income (k$)']).mean()))
    f.write("\n")
    f.write("Deviation of the mean for annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_2['Annual Income (k$)']).std()))
    f.write("\n")
    f.write("In cluster one we have:  customers"+str(cluster_2.shape[0]))
    f.write("\n")

    f.write("Average age for customers in cluster one: " +str((np.array(cluster_3['Age']).mean())))
    f.write("\n")
    f.write("Average age for customers in cluster one:"+str(np.array(cluster_3['Age']).mean()))
    f.write("\n")
    f.write("Average annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_3['Annual Income (k$)']).mean()))
    f.write("\n")
    f.write("Deviation of the mean for annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_3['Annual Income (k$)']).std()))
    f.write("\n")
    f.write("In cluster one we have:  customers"+str(cluster_3.shape[0]))
    f.write("\n")

    f.write("Average age for customers in cluster one: " +str((np.array(cluster_4['Age']).mean())))
    f.write("\n")
    f.write("Average age for customers in cluster one:"+str(np.array(cluster_4['Age']).mean()))
    f.write("\n")
    f.write("Average annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_4['Annual Income (k$)']).mean()))
    f.write("\n")
    f.write("Deviation of the mean for annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_4['Annual Income (k$)']).std()))
    f.write("\n")
    f.write("In cluster one we have:  customers"+str(cluster_4.shape[0]))
    f.write("\n")

    f.write("Average age for customers in cluster one: " +str((np.array(cluster_5['Age']).mean())))
    f.write("\n")
    f.write("Average age for customers in cluster one:"+str(np.array(cluster_5['Age']).mean()))
    f.write("\n")
    f.write("Average annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_5['Annual Income (k$)']).mean()))
    f.write("\n")
    f.write("Deviation of the mean for annual income (in thousends) for customers in cluster one: "+str(np.array(cluster_5['Annual Income (k$)']).std()))
    f.write("\n")
    f.write("In cluster one we have:  customers"+str(cluster_5.shape[0]))
    f.write("\n")


    f.close()