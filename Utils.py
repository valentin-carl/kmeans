import csv, re
from matplotlib import pyplot as plt


def loadData(filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        readFirstLine = False
        for row in reader:
            if not readFirstLine:
                if re.search("\D", row[0][0]):
                    readFirstLine = True
                    continue
            new_row = []
            for number in row:
                if re.search("\s", number[0]):
                    new_row.append(float(number[1:]))
                else:
                    new_row.append(float(number))
            data.append(new_row)
    return data
    
def printTable(data, nrow = 5):
    for i in range(nrow):
        for j in range(len(data[0])):
            print(data[i][j], "\t", end="")
        print()
        
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
            if len(newClusters[clusterIndex]) != 0:
                centroids[clusterIndex][clusterValueIndex] /= len(newClusters[clusterIndex])
            else:
                centroids[clusterIndex][clusterValueIndex] /= 1
            
    # return new clusters
    return centroids

def plotClusters(clusters, data):
    clusterAssignments = []
    for row in data:
        assignedCluster = 0
        for clusterIndex in range(len(clusters)):
            if row in clusters[clusterIndex]:
                assignedCluster = clusterIndex
                break
        clusterAssignments.append(assignedCluster)
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    plt.scatter(x, y, c=clusterAssignments)
    centroids = updateCentroids(clusters)
    a = [row[0] for row in centroids]
    b = [row[1] for row in centroids]
    plt.scatter(a, b, marker = "x")
    plt.show()
    