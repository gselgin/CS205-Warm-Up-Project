# Greg Elgin, Connor Hamilton
# CS 205: Warm up project
# Parsing system to take a string input and return token values
# Calls query function with tokens as parameters


# TODO: TOKENS: Region, Month, type (conventional vs organic), more? Figure out with SQL team
# token list index values region
# [region, AveragePrice, Total Volume, Date, type ]
# token list index values sales
# [type, month, price, num sales, region]


def main():
    print()
    print("Welcome to the Avocado data parsing program")
    get_info()

    parse()


def get_info():
    print()
    print("You can search avocado date by region or sales")
    print("Begin your search by typing 'region' followed by a region name")
    print("or 'sales' followed by the avocado type (conventional or organic)")
    print("Enter 'get region' for list of regions")
    print("Enter q to quit")
    # TODO: Add more info


def get_user_input():
    usr_input = str(input(""))
    return usr_input

# function to return a list of regions
def get_region_list():
    region_list = [
        "GreatLakes",
        "HarrisburgScranton",
        "HartfordSpringfield",
        "Houston",
        "Indianapolis",
        "Jacksonville",
        "LasVegas",
        "LosAngeles",
        "Louisville",
        "MiamiFtLauderdale",
        "Nashville",
        "NewOrleansMobile",
        "NewYork",
        "Northeast",
        "NorthernNewEngland"
    ]


def parse():
    # Initialize valid to enter while loop
    valid = False
    finish = False

    while not valid or not finish:

        # get user input

        user_input = get_user_input()
        input_list = list(user_input.split(" "))
        tokens = list()

        # If the first word in the search is "region"
        # Then the first token is the word after region
        if input_list[0] == "region":
            valid = True

            tokens.append(input_list[1])

            # placeholder tokens
            token_list = ["averagePrice", "Total Volume", "Date", "type"]



            # search for second token if exists
            if len(input_list) >= 3:
                if input_list[2] in token_list:
                    tokens.append(input_list[2])
                    query_region(tokens)
                else:
                    valid = False
                    print("Invalid token in region")
            else:
                query_region(tokens)

        # If the first word in the search is "sales"
        # Then the first token is the word after sales (conventional or organic)
        elif input_list[0] == "sales":
            valid = True
            tokens.append(input_list[1])
            query_sales(tokens)

            # placeholder tokens
            token_list = ["type", "month", "price", "num sales", "region"]

            # search for second token if exists
            if len(input_list) >= 3:
                if input_list[2] in token_list:
                    tokens.append(input_list[2])
                else:
                    valid = False
                    print("Invalid search")

        # exit program if input is "q"
        elif input_list[0].lower() == "q":
            valid = True
            finish = True

        else:
            valid = False
            print("Invalid search: ")
            get_info()
            get_user_input()





# FOR TESTING PURPOSES
def query_sales(tokens):
    print ("query_sales")
    print(tokens)
def query_region(tokens):
    print ("query_region")
    print(tokens)


main()