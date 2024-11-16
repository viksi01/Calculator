from matplotlib import pyplot as plt
from visualization import Visualization


class BarChart(Visualization):
    def __init__(self, category_column, value_column):
        self.category_column = category_column
        self.value_column = value_column

    def visualize(self, data):
        data_grouped = data.groupby(self.category_column)[self.value_column].mean()
        data_grouped.plot(kind='bar', figsize=(10, 5), color='green')
        plt.xlabel(self.category_column)
        plt.ylabel(f"Average {self.value_column}")
        plt.title(f"Average {self.value_column} by {self.category_column}")
        #plt.show()
