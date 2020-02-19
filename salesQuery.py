import sqlite3

def getSalesData(queryList, c):
    
    if queryList[0] == "TotalVolume":
        c.execute('''SELECT Sales.fldTotalVolume FROM Sales
                INNER JOIN Region
                ON Sales.pfkRegionID = Region.pmkRegionID
                WHERE Sales.fldMonth == (?) AND Sales.fldType == (?) AND Region.fldRegionName == (?) ''',
            (queryList[2], queryList[3], queryList[1]))
        result = c.fetchone()[0]
        print("Sales:",result)
       

    elif queryList[0] == "AveragePrice":
        c.execute('''SELECT Sales.fldAvgPrice FROM Sales
                INNER JOIN Region
                ON Sales.pfkRegionID = Region.pmkRegionID
                WHERE Sales.fldMonth == (?) AND Sales.fldType == (?) AND Region.fldRegionName == (?) ''',
            (queryList[2], queryList[3], queryList[1]))
        result = c.fetchone()[0]
        print("$",result)
        
conn = sqlite3.connect('Avocado.db')
c = conn.cursor()
list1 = ['AveragePrice', 'great lakes', '5', 'organic']

getSalesData(list1, c)
conn.close()
