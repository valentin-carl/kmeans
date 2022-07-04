from Utils import loadData, plotClusters
from random import randint


def stop(cluster1, cluster2):
    """
    Simple stop criterium,
    compares whethere cluster assignment changes between two clusters
    """
    return cluster1 == cluster2

def distance(p1, p2):
    """
    Euclidian distance function
    """
    dist = 0
    for i in range(len(p1)):
        dist += (p1[i]-p2[i])**2
    return dist**0.5

def randomCentroids(k, data):
    """
    generates k random centroids for data table
    """
    # find min and max value in each dimension
    mins = data[0].copy()
    maxs = data[0].copy()
    for row in data:
        for j in range(len(row)):
            if mins[j] > row[j]:
                mins[j] = row[j]
            elif maxs[j] < row[j]:
                maxs[j] = row[j]
                
    # return list of centroids with random values between min and max in each dimension
    return [[randint(mins[j], maxs[j]) for j in range(len(data[0]))] for i in range(k)]

def generateClusters(centroids, data):
    """
    assigns all points in data table to closest centroid in centroids,
    returns clusters as lists of data points
    """
    # go over all data points
    clusters = [[] for i in range(len(centroids))]
    for row in data:
        closestCluster = 0
        
        # find index of closest cluster
        for centroidIndex in range(len(centroids)):
            if distance(row, centroids[centroidIndex]) < distance(row, centroids[closestCluster]):
                closestCluster = centroidIndex
                
        # assign point to closest cluster
        clusters[closestCluster].append(row)
    
    # return clusters
    return clusters

def updateCentroids(newClusters):
    """
    calculates centroids for clusters in newClusters list
    """
    # find dimensions in data & number of clusters
    dim = len(newClusters[0][0])
    nClusters = len(newClusters)
    
    # for each cluster, get mean value of points within cluster
    centroids = [[0 for i in range(dim)] for j in range(nClusters)]
    for clusterIndex in range(nClusters):
        
        # add value of each value in each point of cluster
        for pointIndex in range(len(newClusters[clusterIndex])):
            for valueIndex in range(dim):
                centroids[clusterIndex][valueIndex] += newClusters[clusterIndex][pointIndex][valueIndex]
        
        # divide by number of points in cluster to get average values
        for clusterValueIndex in range(dim):
            centroids[clusterIndex][clusterValueIndex] /= len(newClusters[clusterIndex])
            
    # return new clusters
    return centroids

def kmeans(k, filename):
    """
    performs k-Means algorithm on data in filename for k clusters,
    returns clusters as lists of data points
    """
    # load data and generate random centroids
    data = loadData(filename)
    centroids = randomCentroids(k, data)
    
    # while stop criterium is not met, generate new centroids and assign points to clusters
    oldClusters, newClusters = None, []
    while not stop(oldClusters, newClusters):
        
        # save old clusters for stop criterium, assign new clusters, and generate new centroids
        oldClusters = newClusters
        newClusters = generateClusters(centroids, data)
        centroids = updateCentroids(newClusters)
        
    # return list of points for each cluster
    return newClusters

if __name__ == "__main__":
    """
    programme entry point
    - filename: name of csv file that contains data
    - k: number of clusters
    """
    # parameters
    filename = "data.csv"
    data = loadData(filename)
    k = 2
    
    # generate clusters and plot
    clusters = kmeans(k, filename)
    plotClusters(clusters, data)
