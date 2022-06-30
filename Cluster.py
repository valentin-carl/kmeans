from Table import Table
from Utils import dist
from random import randint


def kMeans(k: int, data: Table):

    # get k random initial centroids
    centroids = []
    for i in range(k):
        pass
        # TODO init random clusters or use argument => new function?

    # do k-means
    old, rowClusterAssignments = None, []
    while assignmentsDiffer(old, rowClusterAssignment):
        # next iteration
        old = rowClusterAssignments
        rowClusterAssignments = assignToClusters(centoids, data)
        clusters = generateClusters(rowClusterAssignments, k)
        centroids = updateCentroids(clusters, data)
    return clusters

def randomCentroids(data: Table, k: int) -> list:
    centroids = []
    mins = [data.min(i) for i in range(data.shape[1])]
    maxs = [data.max(i) for i in range(data.shape[1])]
    for i in range(k):
        centroid = []
        for j in range(data.shape[1]):
            centroid.append(randint(mins[j], maxs[j]))
        centroids.append(centroid)
    return centroids

def assignToClusters(centroids: list, data: Table):
    """
    returns list of tuples, where each tuple is in the form (rowIndex, clusterIndex)
    """
    new = []
    for i in range(data.shape[0]):
        clusterIndex = 0
        for j in range(len(centroids)):
            if dist(data.row(i), centroids[j]) < dist(data.row(i),centroids[j]):
                clusterIndex = j
        new.append((i, clusterIndex))
    return new

def generateClusters(new, k):
    """
    generates list of clusters,
    each cluster is a list of indices,
    each index is an index of a row in table
    """
    clusters = [[] for x in range(k)]
    for row in new:
        clusters[row[1]].append(row[0])
    return clusters

def updateCentroids(clusters, data):
    centroids = [mean([data.row(index) for index in cluster]) for cluster in clusters]
    return centroids

def plotClusters():
    # TODO plot clusters
    pass

def assignmentsDiffer(old, new):
    """
    compares the two clusters
    old, new should be lists of lists in the form
    id | assigned_cluster
    :return: True if old != new, else False
    """
    return old != new

def mean(dataPoints):
    """
    calculates center point of dataPoints list
    :return centroid as tuple
    """
    centroid = []
    n = len(list)
    for j in range(len(dataPoints[0])):
        centroid.add(0)
        for i in range(n):
            centroid[j] += dataPoints[i][j]
        centroid[j] /= n
    return tuple(centroid)
