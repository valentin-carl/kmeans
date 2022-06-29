import csv


def readCsv(filename: str, addId: bool, hasHeader: bool):
    """
    reads data from filename and creates list of tuples, skips header if exists
    use addId to create rowID as first entry in each tuple
    """
    data = []
    with open(filename, newline='') as csvfile:
        r = csv.reader(csvfile)
        readHeaders = False
        rowID = 0
        for row in r:
            if not readHeaders and hasHeader:
                readHeaders = True
            else:
                newRow = [rowID] if addId else []
                for x in row:
                    newRow.append(int(x))
                data.append(tuple(newRow))
                rowID += 1
    return data

def getTableNames(filename: str):
    """
    reads first line of csv file 'filename' and returns as list
    """
    with open(filename, newline='') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            return row
