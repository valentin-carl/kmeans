import Utils
import matplotlib.pyplot as plt

class Table:
    def __init__(self, filename: str, addId = False, hasHeader = False):
        self.names = Utils.getTableNames(filename) if hasHeader else ['test']
        self.data = Utils.readCsv(filename, addId, hasHeader)
        self.shape = (len(self.data), len(self.data[0])) # n rows x m cols
        self.hasNames = hasHeader
        self.hasIDs = addId

    def row(self, rowIndex: int):
        """
        :param rowIndex: index of row to return
        :return: row as tuple
        """
        return self.data[rowIndex]

    def peek(self, nRows = 5):
        """
        prints first five rows
        :return: none
        """
        if self.hasNames:
            for name in self.names:
                print(name, '\t', end='')
            print()
            for i in range(self.shape[1]):
                print('===', end='')
            print()
        for i in range(nRows):
            for value in self.row(i):
                print(value, '\t', end='')
            print()

    def plot(self):
        """
        plots the data
        important: data should to be 2-dimensional
        :return: none
        """
        i, j = 0, 1
        if self.hasIDs:
            i += 1
            j += 1
        plt.scatter([x[i] for x in self.data], [x[j] for x in self.data])
        plt.show()
