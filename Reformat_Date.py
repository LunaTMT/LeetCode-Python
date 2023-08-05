def reformatDate(self, date: str) -> str:
    
    date = date.split(" ")
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    months = {month: str(i) for i, month in enumerate(months, start=1)}

    year = date[2]
    month = months[date[1]]
    day = date[0][:-2]

    return f"{year}-{'0' + month if int(month) < 10 else month}-{'0' + day if int(day) < 10 else day}"