class Solution:
    def reformatDate(self, date: str) -> str:
        date=date.split();rev=''
        months = {"Jan": "01","Feb": "02","Mar": "03","Apr": "04","May": "05","Jun": "06","Jul": "07","Aug": "08","Sep": "09","Oct": "10","Nov": "11","Dec": "12"}
        rev+=date[2]+"-"
        rev+=months[date[1]]+"-"
        if len(date[0])==3:
            rev+="0"+date[0][0]
        else:
            rev+=date[0][:2]
        return rev
