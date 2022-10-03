import datetime as dt

# convert string to datetime
def csd(datept: str) -> dt.datetime:
    date, time = datept.split("T")
    date = list(map(int, date.split("-")))
    time = list(map(int, time.split(":")))
    return dt.datetime(*(date + time))


# conver datetime to string
def cds(datept: dt.datetime) -> str:
    return datept.strftime("%Y-%m-%dT%H:%M:%S")