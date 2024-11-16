from matplotlib import pyplot as plt
from visualization import Visualization


class MultiPlot(Visualization):
    def visualize(self, data):
        fig, axs = plt.subplots(1, 2, figsize=(14, 7))

        # Перший графік: Стовпчаста діаграма для 'Number_of_Apps_Used'
        data['Number_of_Apps_Used'].value_counts().plot(kind='bar', ax=axs[0], color='green')
        axs[0].set_title('Distribution of Number of Apps Used')
        axs[0].set_xlabel('Number of Apps')
        axs[0].set_ylabel('Frequency')

        # Другий графік: Секторна діаграма для 'Number_of_Apps_Used'
        data['Number_of_Apps_Used'].value_counts().plot(kind='pie', ax=axs[1], autopct='%1.1f%%', colors=['lightblue', 'orange', 'yellow', 'pink'])
        axs[1].set_title('Number of Apps Used Distribution')
        axs[1].set_ylabel('')

        plt.tight_layout()
        #plt.show()