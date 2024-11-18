from matplotlib import pyplot as plt
from visualization import Visualization


class PieChart(Visualization):
    def __init__(self, column):
        self.column = column

    def visualize(self, data):
        plt.figure(figsize=(8, 8))
        data[self.column].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'orange', 'green', 'pink'])
        plt.title(f"Distribution of {self.column}")
        plt.ylabel('')  
        #plt.show()