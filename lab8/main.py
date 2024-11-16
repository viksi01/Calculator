from matplotlib import pyplot as plt
from data_handler import DataHandler
from data_visualizer import DataVisualizer
from exporter import PlotExporter
from histogram import Histogram
from bar_chart import BarChart
from multi_plot import MultiPlot
from pie_chart import PieChart


def main():
    data_handler = DataHandler('mobile_usage_behavioral_analysis.csv')

    histogram_strategy = Histogram(column='Age')
    pie_chart_strategy = PieChart(column='Gender')
    bar_chart_strategy = BarChart(category_column='Gender', value_column='Social_Media_Usage_Hours')
    multi_plot_strategy = MultiPlot()

    # Використання DataVisualizer з різними стратегіями
    visualizer = DataVisualizer(data_handler, histogram_strategy)
    visualizer.visualize()  # Гістограма
    exporter = PlotExporter()
    exporter.export_plot('age', 'png')  
    plt.show() 

    # Зміна стратегії на кругову діаграму
    visualizer.set_strategy(pie_chart_strategy)
    visualizer.visualize()  
    exporter = PlotExporter()
    exporter.export_plot('gender', 'png')  
    plt.show()  

    # Зміна стратегії на стовпчасту діаграму
    visualizer.set_strategy(bar_chart_strategy)
    visualizer.visualize()  
    exporter = PlotExporter()
    exporter.export_plot('gender_social_media', 'png') 
    plt.show()  

    # Зміна стратегії на кілька піддіаграм
    visualizer.set_strategy(multi_plot_strategy)
    visualizer.visualize()  
    exporter = PlotExporter()
    exporter.export_plot('multi_plot', 'png')  
    plt.show()  

main()
    