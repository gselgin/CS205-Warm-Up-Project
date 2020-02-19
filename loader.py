import sqlite3

def loadTables(regionFile, salesFile):
    regions  = open(regionFile, "r")
    sales  = open(salesFile, "r")
    #create or connect to database
    conn = sqlite3.connect('Avocado.db')
    c = conn.cursor()
    
    #drop tables
    c.execute('DROP TABLE IF EXISTS region')
    c.execute('DROP TABLE IF EXISTS sales')
    
    #create new tables
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

    
    #fill region table
    for line in regions:
        regionData = line.strip("\n")
        regionData = regionData.strip()
        regionData = regionData.split(",")
        c.execute('INSERT INTO Region VALUES (?, ?, ?, ?, ?, ?)', regionData)
    #fill sales table
    for line in sales:
        saleData = line.strip("\n")
        saleData = saleData.split(",")
        c.execute('INSERT INTO Sales VALUES (?, ?, ?, ?, ?, ?)', saleData)
    
    #save changes
    conn.commit()
    
    #close connection and files
    conn.close()
    regions.close()
    sales.close()

