# Greg Elgin,
# CS 205: Warm up project
# Parsing system to take a string input and output a SQL Query


# TODO: TOKENS: Region, Month, type (conventional vs organic), more?
# region (type, month)
# or 
# sales (all of fields)
def main():
    get_info()

    user_input = get_user_input()

    user_query = parse(user_input)

    print(user_query)


def get_info():
    print()
    print("Welcome to the Avocado data parsing program")
    print("You can search for avocado price and sales by region and date")
    # TODO: Add more info


def get_user_input():
    usr_input = str(input(""))
    return usr_input


def parse(user_input):
    # Initialize valid to enter while loop
    valid = False

    while not valid:
        # Initialize local variables
        input_list = list(user_input.split(" "))
        user_query_list = list()
        user_query = ""

        # If the first word in the search is "region"
        # Then the first part of the query is "region" followed by the region name
        if input_list[0] == "region":
            valid = True
            user_query_list.append("SELECT")
            user_query_list.append(input_list[1])
            user_query_list.append("FROM")
            user_query_list.append("region")

            if len(input_list) >= 4:
                if input_list[2] == "type":
                    user_query_list.append("WHERE")
                    user_query_list.append("type=" + input_list[3])
            else:
                print("empty")

        if len(user_query_list) == 0:
            valid = False
            get_info()
            get_user_input()


    # Turn query list into query string
    for word in user_query_list:
        user_query += word + " "

    # Return query
    return user_query


main()
