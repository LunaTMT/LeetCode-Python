def dayOfYear(self, s: str) -> int:
    year, month, day = s.split("-")
    year, month, day = int(year), int(month), int(day)
    list_year=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    return list_year[month-1] + day + (1 if year%4==0 and year!=1900 and month>2 else 0)
    
