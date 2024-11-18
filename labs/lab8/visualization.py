from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class Visualization(ABC):
    @abstractmethod
    def visualize(self, data):
        pass

