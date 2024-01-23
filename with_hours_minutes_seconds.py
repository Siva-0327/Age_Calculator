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
    
    def day(self):
        
        count = self.calculating()

        return count
    
    def hours(self):

        count = self.calculating()

        hour = count*24

        return hour
    
    def minutes(self):

        minute = self.hours()

        minutes_count = minute*60

        return minutes_count
    
    def seconds(self):

        minute = self.minutes()

        sec_count =  minute*60

        return sec_count
    
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
    
    def total_week_remain(self):

        total_day = self.calculating()

        week_remain = total_day % 7

        return week_remain

        
    

        

        
