# Greg Elgin,
# CS 205: Warm up project
# Parsing system to take a string input and return token values
# Calls query function with tokens as parameters


# TODO: TOKENS: Region, Month, type (conventional vs organic), more? Figure out with SQL team
# token list index values region
# [region, ]
# token list index values sales
# [type, month, price, num sales, ]


def main():
    print()
    print("Welcome to the Avocado data parsing program")
    get_info()

    user_input = get_user_input()

    parse(user_input)


def get_info():
    print()
    print("You can search avocado date by region or sales")
    print("Begin your search by typing 'region' followed by a region name")
    print("or 'sales' followed by the avocado type (conventional or organic)")
    # TODO: Add more info


def get_user_input():
    usr_input = str(input(""))
    return usr_input


def parse(user_input):
    # Initialize valid to enter while loop
    valid = False

    while not valid:
        input_list = list(user_input.split(" "))
        tokens = list()

        # If the first word in the search is "region"
        # Then the first token is the word after region
        if input_list[0] == "region":
            valid = True
            tokens.append(input_list[1])


            query_region(tokens)


        # If the first word in the search is "sales"
        # Then the first token is the word after sales (conventional or organic)
        elif input_list[0] == "sales":
            valid = True
            tokens.append(input_list[1])
            query_sales(tokens)

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
