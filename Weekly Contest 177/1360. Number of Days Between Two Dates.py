class Solution:    
    def find_leap_year(self, year) -> int:
        return year // 4 - year // 100 + + year // 400
    
    # using magic formula
    # https://leetcode.com/problems/number-of-days-between-two-dates/discuss/517582/Python-Magical-Formula
    def find_month(self, month) -> int:
        return ((153 * month) + 8) // 5

    def find_days(self, date) -> int:
        if date[1] == 1 or date[1] == 2:
            date[1] += 12
            date[0] -= 1

        days = 365 * date[0]
        days += self.find_leap_year(date[0])
        days += self.find_month(date[1])
        return  days + date[2]


    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1, date2 = date1.split("-"), date2.split("-")
        date1 = [ int(val) for val in date1 ]
        date2 = [ int(val) for val in date2 ]

        return abs(self.find_days(date1) - self.find_days(date2) )


print( Solution().daysBetweenDates("2019-06-30", "2019-06-29") )
print( Solution().daysBetweenDates("2020-01-15", "2019-12-31") )