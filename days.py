from datetime import datetime

from info import Calculate

class Difference(Calculate):

    def calculating(self):
        
        self.birthday_date = datetime.strptime(self.date,"%Y-%m-%d")

        age_calculator = self.current_date - self.birthday_date
        
        return age_calculator.days


        
