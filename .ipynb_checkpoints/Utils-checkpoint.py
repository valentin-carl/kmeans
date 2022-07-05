import csv, re
from matplotlib import pyplot as plt
from Clustering import updateCentroids


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
    