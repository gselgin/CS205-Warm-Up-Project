# Greg Elgin, Connor Hamilton
# CS 205: Warm up project
# Last Updated: 02/10/20
# Parsing system to take a string input and return token values
# Calls query function with tokens as parameters

import shlex

region_list = ["Great Lakes", "Harrisburg Scranton", "Hartford Springfield", "Houston", "Indianapolis", "Jacksonville",
               "Las Vegas", "Los Angeles", "Louisville", "Miami Ft Lauderdale", "Nashville", "New Orleans Mobile",
               "New York", "Northeast", "Northern New England"]
# Initialize search to allow for user to quit without searching
search = False
# Initialize tokens
tokens = list()


def main():
    print("Welcome to the Avocado data parsing program")
    get_info()
    parse()

    if search:
        query(tokens)


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
    global search

    while not valid:

        # get user input, turn into list of words, initialize empty token list
        user_input = get_user_input()
        user_input = user_input.lower()
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
                            if int(input_list[5]) in range(1, 13):
                                tokens.append(int(input_list[5]))
                            else:
                                print("you must specify a month between 1 and 12")
                                valid = False

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
                print("Please input 'region' followed by a region after you specify average price or total volume")
                valid = False

        # exit program if input is "q"
        elif length >= 1 and input_list[0] == "q":
            valid = True
            search = False

        else:
            print("Please begin your search with 'average price', 'total volume', or 'best month'")
            print("Or input 'q' to quit")
            valid = False


# FOR TESTING PURPOSES
def query(tokens_list):
    print(tokens_list)


main()
