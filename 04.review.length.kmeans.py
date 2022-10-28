import pandas as pd
import numpy as np
import statistics
import copy


df = pd.read_json("D:/ESILV/Annee_5/Vietnam/cours/Data_mining_2/archive/yelp_academic_dataset_review.json", lines=True, nrows=10000)
df["length"] = df["text"].str.len()
data = df["length"].to_list()

cluster_nb = input("how many cluster do you want ?")

points_list = []
step = 1 / int(cluster_nb)
for i in range(int(cluster_nb)):
    points_list.append(df.length.quantile([step]).values[0])
    step += 1 / int(cluster_nb)


def closest_point2(liste, value):
    distance_list = []
    for i in liste:
        distance = abs(i - value)
        distance_list.append(distance)

    return min(range(len(distance_list)), key=distance_list.__getitem__)


list_cluster_big = []
for i in range(int(cluster_nb)):
    list_cluster_big.append([])


for i in data:
    index = closest_point2(points_list, i)
    list_cluster_big[index].append(i)

print(list_cluster_big)


overlap = 0

while overlap < 95:  # you can set the precision you want here, here, 95% overlaping between 2 iterations
    # print(list_cluster_big)
    list_cluster_temp = []

    for i in range(int(cluster_nb)):
        list_cluster_temp.append([])

    points_list_temp = []
    for j in list_cluster_big:
        mean = statistics.mean(j)
        points_list_temp.append(mean)

    for i in data:
        index = closest_point2(points_list_temp, i)
        list_cluster_temp[index].append(i)

    overlap = len(set(list_cluster_big[0]) & set(list_cluster_temp[0])) / float(len(set(list_cluster_big[0]) | set(list_cluster_temp[0]))) * 100
    list_cluster_big = copy.deepcopy(list_cluster_temp)

    print(list_cluster_temp)  # this is our clustered nested list
