from lab8.classes.data_handler import DataHandler
from lab8.classes.data_visualizer import DataVisualizer
from lab8.classes.visualization import BarChart, Histogram, PieChart, MultiPlot

def run():
    file_path = r"C:\Users\victo\OneDrive - Національний університет Львівська політехніка\LPNU\3 курс\Спеціалізовані мови програмування\Calculator\lab8\sources\mobile_usage_behavioral_analysis.csv"

    data_handler = DataHandler(file_path)

    visualizer = DataVisualizer(data_handler, BarChart('Gender', 'Social_Media_Usage_Hours'))

    print("Visualizing with Bar Chart...")
    visualizer.visualize()

    print("\nSwitching to Histogram...")
    visualizer.set_strategy(Histogram('Age', bins=15))
    visualizer.visualize()

    print("\nSwitching to Pie Chart...")
    visualizer.set_strategy(PieChart('Gender'))
    visualizer.visualize()

    print("\nSwitching to MultiPlot...")
    visualizer.set_strategy(MultiPlot())
    visualizer.visualize()


if __name__ == "__main__":
    run()
