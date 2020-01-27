# Greg Elgin
# CS 205: Warm up project
# Parsing system to take a string input and output a SQL Query


# TOKENS: Region, Date, type (conventional vs organic),



def main():
    get_info()

    user_input = get_user_input()

    user_query = parse(user_input)

    print(user_query)


def get_info():
    print("Welcome to the Avocado data parsing program")
    print("You can search for avocado price and sales by region and date")
    # TODO: Add more info


def get_user_input():
    usr_input = str(input(""))
    return usr_input


def parse(user_input):
    # Initialize local variables
    input_list = list(user_input.split(" "))
    user_query_list = list()
    user_query = ""

    # If the first word in the search is region
    # Then the first part of the query is region followed by the region name
    if input_list[0] == "region":
        user_query_list.append("region")
        user_query_list.append(input_list[1])

    # Turn query list into query string
    for word in user_query_list:
        user_query += word + " "

    # Return query
    return user_query


main()
