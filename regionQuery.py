import sqlite3

def getRegionData(queryList, cursor):
    if queryList[0] == "AveragePrice":
        if queryList[3] == "organic":
            cursor.execute('SELECT fldAvgPriceOrg FROM Region WHERE fldRegionName = ?', queryList[1:2])
        else:
            cursor.execute('SELECT fldAvgPriceCon FROM Region WHERE fldRegionName = ?', queryList[1:2])
            
        result = cursor.fetchone()[0]
        print("$",result,sep = "")
    if queryList[0] == "BestMonth":
        if queryList[3] == "organic":
            cursor.execute('''SELECT Sales.fldMonth, Sales.fldTotalVolume FROM Region
                           INNER JOIN Sales
                           ON Region.pfkBestMonOrgID = Sales.pmkSalesID
                           WHERE fldRegionName = ?''', queryList[1:2])
        else:
            cursor.execute('''SELECT Sales.fldMonth, Sales.fldTotalVolume FROM Region
                           INNER JOIN Sales
                           ON Region.pfkBestMonConID = Sales.pmkSalesID
                           WHERE fldRegionName = ?''', queryList[1:2])
        result = cursor.fetchone()
        print("Month:",result[0],"Sales",result[1])
conn = sqlite3.connect('Avocado.db')
c = conn.cursor()
list1 = ['AveragePrice', 'great lakes', '', 'organic']

getRegionData(list1, c)
conn.close()
