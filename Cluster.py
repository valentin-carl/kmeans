from Table import Table


def kMeans(k: int, data: Table):

    # get k random initial centroids
    centroids = []
    for i in range(k):
        pass

    #
    old, new = [], []
    while assignmentsDiffer():
        new = assignToClusters(centoids, data)
        pass

def assignToClusters(centroids: list, data: Table):
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

def dist(x, y):
    """
    :return euclidian distance between x & y
    """
    sum = 0
    for i in range(len(x)):
        sum += (x[i]-y[i])**2
    return sum**(0.5)
