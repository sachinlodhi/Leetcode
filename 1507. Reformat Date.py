class Solution:
    def reformatDate(self, date: str) -> str:
        # date = "26th May 1960"
        date = date.split(" ")
        day = "".join([ i for i in date[0] if i.isdigit()])

        year = date[2]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = str([i for i in range(len(months)) if months[i] == date[1]].pop() + 1)
        if len(day) == 1:
            day = '0'+day
        if len(month) == 1:
             month = '0'+month

        ans = year + "-" + month + "-" + day
        # print(ans)
        return ans
'''
Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
 

Example 1:

Input: date = "20th Oct 2052"
Output: "2052-10-20"
Example 2:

Input: date = "6th Jun 1933"
Output: "1933-06-06"
Example 3:

Input: date = "26th May 1960"
Output: "1960-05-26"
 

Constraints:

The given dates are guaranteed to be valid, so no error handling is necessary.
'''
