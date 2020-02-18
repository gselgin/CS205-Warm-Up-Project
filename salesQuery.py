import sqlite3

def regionToID(arg):
    switch = {
        "albany": 1,
        "atlanta": 2,
        "baltimore washington": 3,
        "boise": 4,
        "boston": 5,
        "buffalo rochester": 6,
        "california": 7,
        "charlotte": 8,
        "chicago": 9,
        "cincinnati dayton": 10,
        "columbus": 11,
        "dallas ft worth": 12,
        "denver": 13,
        "detroit": 14,
        "grand rapids": 15,
        "great lakes": 16,
        "harrisburg scranton": 17,
        "hartford springfield": 18,
        "houston": 19,
        "indianapolis": 20,
        "jacksonville": 21,
        "las vegas": 22,
        "los angeles": 23,
        "louisville": 24,
        "miami ft lauderdale": 25,
        "nashville": 26,
        "new orleans mobile": 27,
        "new york": 28,
        "northeast": 29,
        "northern new england": 30
    }
    return switch.get(arg, "null")

def getSalesData(queryList):
    conn = sqlite3.connect('Avocado.db')
    c = conn.cursor()

    if queryList[0] == "TotalVolume":
        c.execute(
            '''SELECT fldTotalVolume FROM Sales WHERE fldMonth == (?) AND fldType == (?) AND pfkRegionID == (?) ''',
            (queryList[2], queryList[3], regionToID(queryList[1])))
        result = c.fetchall()
        print(result)

    elif queryList[0] == "AveragePrice":
        c.execute(
            '''SELECT fldAvgPrice FROM Sales WHERE fldMonth == (?) AND fldType == (?) AND pfkRegionID == (?) ''',
            (queryList[2], queryList[3], regionToID(queryList[1])))
        result = c.fetchall()
        print(result)

    conn.close()