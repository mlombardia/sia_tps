from abc import ABC, abstractmethod

class SearchMethod():

    @abstractmethod
    def search(self, start_node):
        pass
