import shlex
import sqlite3

region_list = ["Great Lakes", "Harrisburg Scranton", "Hartford Springfield", "Houston", "Indianapolis", "Jacksonville",
               "Las Vegas", "Los Angeles", "Louisville", "Miami Ft Lauderdale", "Nashville", "New Orleans Mobile",
               "New York", "Northeast", "Northern New England"]

# Initialize search to allow for user to quit without searching
search = False
# Initialize tokens
tokens = list()
# Keep track if the user has loaded the data into the database
dataLoaded = False


def main():
    cursor = ""
    print("Welcome to the Avocado data parsing program")
    get_info()
    print()
    print("Please enter 'load date' to load the dataset")
    while parse() != 0:
        if search:
            if not dataLoaded:
                print("please enter 'Load Data' before attempting to search the database")
            else:
                if cursor == "":
                    conn = sqlite3.connect('Avocado.db')
                    cursor = conn.cursor()
                query(tokens, cursor)

    if cursor != "":
        conn.close()


def get_info():
    print()
    print("You can search for avocado average price, total volume, or best month (of sales)")
    print("Begin your search by specifying one of these fields followed by 'region' + region name")
    print("You then enter month (1-12) followed by type (organic, conventional)")
    print("Ex: total volume region 'New York' month 4 type organic")
    print("Enter 'region list' for a list of regions")
    print("Enter q to quit")


def get_user_input():
    usr_input = str(input(""))
    return usr_input


def get_region_list():
    return region_list


def load_tables(region_file, sales_file):
    regions = open(region_file, "r")
    sales = open(sales_file, "r")

    # Connect to database
    conn = sqlite3.connect('Avocado.db')
    c = conn.cursor()

    # Drop tables
    c.execute('DROP TABLE IF EXISTS region')
    c.execute('DROP TABLE IF EXISTS sales')

    # Create new tables
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

    # Fill region table
    for line in regions:
        region_data = line.strip("\n")
        region_data = region_data.strip()
        region_data = region_data.split(",")
        c.execute('INSERT INTO Region VALUES (?, ?, ?, ?, ?, ?)', region_data)

    # Fill sales table
    for line in sales:
        sale_data = line.strip("\n")
        sale_data = sale_data.split(",")
        c.execute('INSERT INTO Sales VALUES (?, ?, ?, ?, ?, ?)', sale_data)

    # Save changes
    conn.commit()

    # Close connection and files
    conn.close()
    regions.close()
    sales.close()


def query(tokens_list, cursor):
    # Determine which table is being queried
    if tokens_list[2] == '':
        get_region_data(tokens_list, cursor)
    # TODO: get sales data


def get_region_data(query_list, cursor):
    # Choose and execute correct query for avg price
    if query_list[0] == "AveragePrice":
        if query_list[3] == "organic":
            cursor.execute('SELECT fldAvgPriceOrg FROM Region WHERE fldRegionName = ?', query_list[1:2])
        else:
            cursor.execute('SELECT fldAvgPriceCon FROM Region WHERE fldRegionName = ?', query_list[1:2])
        # get result
        result = cursor.fetchone()[0]
        # display and format result
        print("$", result, sep="")
    # choose and execute correct query for avg price
    if query_list[0] == "BestMonth":
        if query_list[3] == "organic":
            cursor.execute('''SELECT Sales.fldMonth, Sales.fldTotalVolume FROM Region
                           INNER JOIN Sales
                           ON Region.pfkBestMonOrgID = Sales.pmkSalesID
                           WHERE fldRegionName = ?''', query_list[1:2])
        else:
            cursor.execute('''SELECT Sales.fldMonth, Sales.fldTotalVolume FROM Region
                           INNER JOIN Sales
                           ON Region.pfkBestMonConID = Sales.pmkSalesID
                           WHERE fldRegionName = ?''', query_list[1:2])
        # get result
        result = cursor.fetchone()
        # display and format
        print("Month:", result[0], "Sales:", result[1])


def parse():
    # Initialize valid to enter while loop
    valid = False
    global search, dataLoaded

    while not valid:
        try:

            # get user input, turn into list of words, initialize empty token list
            user_input = get_user_input()
            user_input = user_input.lower()

            # Display help information when prompted
            if user_input == "help":
                get_info()
                search = False
                return 1

            # Load data from csv into data base when prompted
            if user_input == "load data" and not dataLoaded:
                load_tables("avocado-region-data.csv", "avocado-sales-data.csv")
                print("Data has been loaded")
                dataLoaded = True
                search = False
                return 1
            input_list = shlex.split(user_input)
            tokens.clear()

            # Save length of user input
            length = len(input_list)

            # If user types "region list" display a list of regions
            if length >= 2 and input_list[0] == "region" and input_list[1] == "list":
                print("Region list: ")
                for item in region_list:
                    print(item)
                print()

            # First word needs to be "average price" or "total volume" or "best month
            if length >= 2 and (input_list[0] == "average" and input_list[1] == "price" or
                                input_list[0] == "total" and input_list[1] == "volume" or
                                input_list[0] == "best" and input_list[1] == "month"):
                if input_list[0] == "average" and input_list[1] == "price":
                    tokens.append("AveragePrice")
                elif input_list[0] == "total" and input_list[1] == "volume":
                    tokens.append("TotalVolume")
                elif input_list[0] == "best" and input_list[1] == "month":
                    tokens.append("BestMonth")

                # Next word should be 'region' followed by a valid region name
                if length >= 4 and input_list[2] == "region":
                    region_list_lower = [x.lower() for x in region_list]
                    if input_list[3] in region_list_lower:
                        tokens.append(input_list[3])

                        # Next item should be 'month' followed by an int 1-12
                        # This field is optional for AvgPrice, mandatory for TotalVol, and empty for BestMonth
                        if length >= 6 and input_list[4] == "month":
                            if input_list[0] == "best":
                                print("When searching for Best Month you do not need to input a month")
                                valid = False
                            elif input_list[0] == "average":
                                if (input_list[5] == "1" or input_list[5] == "2" or input_list[5] == "3" or
                                        input_list[5] == "4" or input_list[5] == "5" or input_list[5] == "6" or
                                        input_list[5] == "7" or input_list[5] == "8" or input_list[5] == "9" or
                                        input_list[5] == "10" or input_list[5] == "11" or input_list[5] == "12"):
                                    tokens.append(int(input_list[5]))
                                else:
                                    print("you must specify a month between 1 and 12")
                                    valid = False

                            elif input_list[0] == "total":
                                try:
                                    if int(input_list[5]) in range(1, 13):
                                        tokens.append(int(input_list[5]))
                                    else:
                                        print("you must specify a month between 1 and 12")
                                        valid = False
                                except ValueError:
                                    print("you must specify a month between 1 and 12")

                            # Last item should be 'type' followed by 'conventional' or 'organic'
                            if length >= 8 and input_list[6] == "type":
                                if input_list[7] == 'conventional' or input_list[7] == "organic":
                                    tokens.append(input_list[7])
                                    if length == 8:
                                        valid = True
                                        search = True
                                    else:
                                        print("You input too much information")

                                else:
                                    print("type must be 'organic' or 'conventional'")
                                    valid = False
                            else:
                                print("You must specify a type after month")
                                valid = False

                        elif length >= 5 and input_list[4] != "month" and (input_list[0] == "best" or
                                                                           input_list[0] == 'average'):
                            tokens.append("")

                            # Last item should be 'type' followed by 'conventional' or 'organic'
                            if length >= 6 and input_list[4] == "type":
                                if input_list[5] == 'conventional' or input_list[5] == "organic":
                                    tokens.append(input_list[5])
                                    if length == 6:
                                        valid = True
                                        search = True
                                    else:
                                        print("You input too much information")

                                else:
                                    print("type must be 'organic' or 'conventional'")
                                    valid = False
                            else:
                                print("You must specify a type after region")
                                valid = False

                        elif input_list[0] != "best":
                            print("You must enter month followed by a number 1-12 after you specify region")
                            valid = False

                        else:
                            print("You must specify a type after region")
                            valid = False

                    else:
                        print("That is not a valid region")
                        print("Input 'region list' to see valid regions")
                        print("If region is multiple words input it in quotes")
                        valid = False
                else:
                    print("Please input 'region' followed by a region name after you specify average price, "
                          "total volume, or best month")
                    valid = False

            # exit program if input is "q"
            elif length >= 1 and input_list[0] == "q":
                return 0

            else:
                print("Please begin your search with 'average price', 'total volume', or 'best month'")
                print("Or input 'q' to quit")
                valid = False
        except ValueError:
            print("Invalid input")
            print("Did you forget to close your quotes?")

            valid = False


main()
