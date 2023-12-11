import calendar
class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
      _, ans = calendar.monthrange(year, month)
      return ans