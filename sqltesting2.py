import sqlite3

def loadTables(regionFile, salesFile):
    regions = open(regionFile, "r")
    sales = open(salesFile, "r")
    conn = sqlite3.connect('Avocado.db')
    c = conn.cursor()

    # drop tables
    c.execute('DROP TABLE IF EXISTS region')
    c.execute('DROP TABLE IF EXISTS sales')

    # create new tables
    c.execute('''CREATE TABLE Region
        (pmkRegionID int NOT NULL,
        fldRegionName varchar(64),
        fldAvgPriceCon smallmoney,
        fldAvgPriceOrg smallmoney,
        pfkBestMonConID int,
        pfkBestMonOrgID int,
        PRIMARY KEY (pmkRegionID),
        FOREIGN KEY (pfkBestMonConID) REFERENCES Sales(pmkSalesID),
        FOREIGN KEY (pfkBestMonOrgID) REFERENCES Sales(pmkSalesID))''')

    c.execute('''CREATE TABLE Sales
        (pmkSalesID int NOT NULL,
        pfkRegionID int NOT NULL,
        fldAvgPrice smallmoney,
        fldTotalVolume int,
        fldMonth tinyint,
        fldType varchar(64),
        PRIMARY KEY (pmkSalesID),
        FOREIGN KEY (pfkRegionID) REFERENCES Region(pmkRegionID))''')

    # fill region table
    for line in regions:
        regionData = line.strip("\n")
        regionData = regionData.strip()
        regionData = regionData.split(",")
        #print(regionData)
        c.execute('INSERT INTO Region VALUES (?, ?, ?, ?, ?, ?)', regionData)
    # fill sales table
    for line in sales:
        saleData = line.strip("\n")
        saleData = saleData.split(",")
        c.execute('INSERT INTO Sales VALUES (?, ?, ?, ?, ?, ?)', saleData)

    # save changes
    conn.commit()

    # close connection and files
    conn.close()
    regions.close()
    sales.close()

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

def main():
    loadTables("avocado-region-data.csv", "avocado-sales-data.csv")
    getSalesData(['TotalVolume', 'great lakes', 12, 'conventional'])
    getSalesData(['AveragePrice', 'cincinnati dayton', 1, 'organic'])
    getSalesData(['AveragePrice', 'albany', 1, 'organic'])
    getSalesData(['TotalVolume', 'miami ft lauderdale', 4, 'conventional'])

main()