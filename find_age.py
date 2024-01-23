from datetime import datetime

from days import Difference

class AgeCalculating(Difference):

    def years(self):

        total_day = self.calculating()

        years = total_day//365

        return years
    def months(self):

          total_day = self.calculating()

          remaining_days =  total_day %365

          months = remaining_days //30

          return months
    def days_count(self):


        days = self.current_date.day - self.birthday_date.day

        return days
    
    def total_months(self):

        year = self.years()

        month = self.months()

        total_mon = year*12+month        

        return total_mon
    def mon_remain_days(self):

        remain_days = self.current_date.day - self.birthday_date.day

        return remain_days
    
    def total_week(self):

        total_day = self.calculating()

        week = total_day//7

        return week
    def day(self):
        
        count = self.calculating()

        return count
    
    def total_week_remain(self):

        total_day = self.calculating()

        week_remain = total_day % 7

        return week_remain

        
        

        
