from datetime import datetime

from abc import ABC,abstractmethod


class Calculate(ABC):

    def __init__(self,name,date): # Pascal naming convention

        self.name = name
        
        self.date =  date

        self.current_date = datetime.today() # Snake naming convention
    @abstractmethod
    def calculating(self):

        pass
