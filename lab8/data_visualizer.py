from matplotlib import pyplot as plt
from data_handler import DataHandler
from visualization import Visualization

class DataVisualizer:
    def __init__(self, data_handler: DataHandler, strategy: Visualization):
        self.data_handler = data_handler
        self.strategy = strategy

    def set_strategy(self, strategy: Visualization):
        self.strategy = strategy

    def visualize(self):
        self.strategy.visualize(self.data_handler.get_data())


