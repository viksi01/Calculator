from matplotlib import pyplot as plt
from visualization import Visualization


class Histogram(Visualization):
    def __init__(self, column, bins=10):
        self.column = column
        self.bins = bins

    def visualize(self, data):
        plt.hist(data[self.column], bins=self.bins, color='skyblue')
        plt.title(f'Histogram of {self.column}')
        plt.xlabel(self.column)
        plt.ylabel('Frequency')
        #plt.show()