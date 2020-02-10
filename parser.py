# Greg Elgin, Connor Hamilton
# CS 205: Warm up project
# Last Updated: 02/10/20
# Parsing system to take a string input and return token values
# Calls query function with tokens as parameters

# TODO: TOKENS: Region, Month, type (conventional vs organic), more? Figure out with SQL team

import shlex

region_list = ["Great Lakes", "Harrisburg Scranton", "Hartford Springfield", "Houston", "Indianapolis", "Jacksonville",
               "Las Vegas", "Los Angeles", "Louisville", "Miami Ft Lauderdale", "Nashville", "New Orleans Mobile",
               "New York", "Northeast", "Northern New England"]


def main():
    print("Welcome to the Avocado data parsing program")
    get_info()
    parse()


def get_info():
    print()
    print("You can search for avocado average price or total volume")
    print("Enter 'region list' for list of regions")
    print("Enter q to quit")
    # TODO: Add more info


def get_user_input():
    usr_input = str(input(""))
    return usr_input


def get_region_list():
    return region_list


def parse():
    # Initialize valid to enter while loop
    valid = False
    # Initialize search to allow for user to quit without searching
    search = False

    while not valid:
        # get user input, turn into list of words, create empty token list
        user_input = get_user_input()
        user_input = user_input.lower()
        input_list = shlex.split(user_input)
        tokens = list()

        # Save length of user input
        length = len(input_list)

        # If user types "region list" display a list of regions
        if length >= 2 and input_list[0] == "region" and input_list[1] == "list":
            print("Region list: ")
            for item in region_list:
                print(item)
            print()

        # First word needs to be "average price" or "total volume"
        if length >= 2 and input_list[0] == "average" and input_list[1] == "price" or \
                input_list[0] == "total" and input_list[1] == "volume":
            if input_list[0] == "average" and input_list[1] == "price":
                tokens.append("AveragePrice")
            elif input_list[0] == "total" and input_list[1] == "volume":
                tokens.append("TotalVolume")

            # Next word should be 'region' followed by a valid region name
            if length >= 4 and input_list[2] == "region":
                region_list_lower = [x.lower() for x in region_list]
                if input_list[3] in region_list_lower:
                    tokens.append(input_list[3])

                    # FOR TESTING PURPOSES
                    valid = True
                    query(tokens)

                else:
                    print("That is not a valid region")
                    print("Input 'region list' to see valid regions")
                    print("If region is multiple words input it in quotes")
                    valid = False
            else:
                print("Please input 'region' followed by a region after you specify average price or total volume")
                valid = False

            # Next item should be 'month' followed by an int 1-12

            # Last item should be 'type' followed by 'conventional' or 'organic'



        # exit program if input is "q"
        elif length >= 1 and input_list[0] == "q":
            valid = True
            search = False

        else:
            print("Please begin your search with 'average price' or 'total volume")
            print("Or input 'q' to quit")
            valid = False


# FOR TESTING PURPOSES
def query(tokens):
    print(tokens)


main()
