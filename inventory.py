
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''

        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#=============Shoe list===========

#==========Functions outside the class==============
def read_shoes_data(file_name):
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    '''
    The list will be used to store a list of objects of shoes.
    '''
    shoe_list = []

    shoe_list_file = []
    try:
        input_file = open(file_name, 'r+', encoding='utf-8')  # Open the file
        input_lines = input_file.readlines()  # reading lines and storing them in a list
        for value in input_lines:
            value = value.strip()
            value = value.split(",")
            shoe_list_file.append(value)

        input_file.close()  # Close files

        # looping through shoe_list
        for shoe_ in shoe_list_file[1:]:  # Removing the title
            # Creating objects
            shoe_obj = Shoe(shoe_[0], shoe_[1], shoe_[2], shoe_[3], shoe_[4])
            shoe_list.append(shoe_obj)

        return shoe_list

    except FileNotFoundError as error_msg:
        print("\nFile name, {} doesn't exit. Enter valid file name.".format(file_name))
        print(error_msg)
#read_shoes_data("inventory.txt")
#print(shoe_list)

def write_On_file(OFile_name, write_values):
    """
     write_On_file, function that writes values in each line of an output file
     inputs = output file name and Value you want to write
     output = writes a line of value onto output file """
    # Opening the output file
    output_file = open(OFile_name, 'a')
    output_file.write(write_values)  # writing values into output file
    # Closing the file once done
    output_file.close()


def capture_shoes(file_name):
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Capturing a shoe data
    # Request input from users
    print("\nCapture the shoe detail here: ")
    country = input("Country: ")
    code = input("code: ")
    product = input("product: ")
    cost = input("cost: ")
    quantity = input("quantity: ")

    # Capturing the shoe obj
    shoe_cpt = Shoe(country, code, product, cost, quantity)

    # Adding the capture shoe object in shoe_list
    shoe_list = read_shoes_data(file_name)
    shoe_list.append(shoe_cpt)

    # Update the inventory file
    shoe_file_list = []
    for shoe_ in shoe_list:
        shoe_file_list.append(shoe_.__str__())

    # First clear the tasks file
    open(file_name, "w").close()

    for items in shoe_file_list:
        write_On_file(file_name, items + "\n")

    print("You successfully captured a product!")


#capture_shoes("try.txt")


def view_all(file_name):
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    # Read invetory.txt file first
    shoe_list = read_shoes_data(file_name)

    for shoe_ in shoe_list:
        # Printing __str__
        #print(shoe_.__str__())

        # For more user friendly view
        print("-------------------------------")
        print(f"Product:      \t", shoe_.product)
        print("Code:          \t", shoe_.code)
        print("Price:         \t", shoe_.cost)
        print("Quantity:      \t", shoe_.quantity)
        print("Country:       \t", shoe_.country)
        print("-------------------------------")

#view_all()


def re_stock(file_name):
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Read invertory.txt file first
    shoe_list = read_shoes_data(file_name)

    # Finding shoe with the lowest quantity
    shoe_quant_list = []   # Empty list to store shoe quantities
    shoe_dict = {}      # Empty dictionary to store shoe_obj as key and shoe Quantity as a value

    # Looping through shoe_list
    for shoe_ in shoe_list:
        # Adding value into shoe_quant_list
        shoe_quant_list.append(shoe_.quantity)
        # Adding value to shoe_dict
        shoe_dict[shoe_] = shoe_.quantity

    # Converting shoe_quant_list elements into an int
    shoe_quant_list = [int(shoe) for shoe in shoe_quant_list]
    #print(shoe_quant_list)

    # Getting the lowest value from shoe_quant_list
    lowest_quant = (min(shoe_quant_list))
    #print(lowest_quant)

    # Using the lowest_quant to find the shoe obj
    # Empty list to store shoe objects with the lowest quantity
    shoes_with_lowest_quant = []
    for quantity, shoe_obj in zip(shoe_dict.values(), shoe_dict.keys()):
        if quantity == str(lowest_quant):
            shoes_with_lowest_quant.append(shoe_obj)

    # Printing lowest stock shoes
    print("\nThe following shoes are almost out of stock: ")

    for shoe, shoe_num in zip(shoes_with_lowest_quant, range(len(shoes_with_lowest_quant))):
        print("-------------------------------")
        print(f"Product {shoe_num + 1}:    \t", shoe.product)
        print("Code:          \t", shoe.code)
        print("Price:         \t", shoe.cost)
        print("Quantity:      \t", shoe.quantity)
        print("Country:       \t", shoe.country)
        print("-------------------------------")

    #  Request the user to input product number of the shoe they want to re-stock
    index_num = input("Pick the product you want to re-stock(enter the product number to pick; Enter \'stp\' to go back): ")# to get the index number

    try:
        while index_num != "stp":
            if int(index_num) <= len(shoes_with_lowest_quant):
                index_num = int(index_num) - 1
                # Request input(new stock value) from the user
                new_stock_value = int(input("Add stock: "))

                # Shoe info before making the re_stock update
                shoe_bfr_re_stock = shoes_with_lowest_quant[index_num].__str__()
                # print(shoe_bfr_re_stock)

                # Updating the stock
                country = shoes_with_lowest_quant[index_num].country
                code = shoes_with_lowest_quant[index_num].code
                product = shoes_with_lowest_quant[index_num].product
                cost = shoes_with_lowest_quant[index_num].cost
                shoes_with_lowest_quant[index_num] = Shoe(country, code, product, cost,
                                                          (new_stock_value + lowest_quant))

                # Shoe info after the update
                sheo_aft_re_stock = shoes_with_lowest_quant[index_num].__str__()
                # print(sheo_aft_re_stock)

                # Updating on file with the new info
                shoe_file_list = []
                for shoe_ in shoe_list:
                    shoe_file_list.append(shoe_.__str__())

                # Updating the shoe obj in the file
                # Removing the old shoe detail
                shoe_file_list.remove(shoe_bfr_re_stock)
                # print(len(shoe_file_list))

                # Adding the new shoe detail
                shoe_file_list.append(sheo_aft_re_stock)
                # print(len(shoe_file_list))

                # First clear the tasks file
                open(file_name, "w").close()

                # Updating the inventory.txt.txt file for later use
                for items in shoe_file_list:

                    write_On_file(file_name, items + "\n")
                print("\nRe-Stock successful")
                break

                if index_num == "stp":
                    exit()
            else:
                print("\nPlease select a valid product number")


    except:
        print("\nPlease select a valid product number")


#re_stock("inventory_file_name.txt")


def search_shoe(file_name, shoe_id):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    # Read inventory.txt file first
    shoe_list = read_shoes_data(file_name)

    print("\nYou searched for the following product")
    # looping through the shoe obj
    for shoe_ in shoe_list:
        # looking for instance with the shoe code we are looking for
        if shoe_.code == shoe_id:
            # Returning search value
            print("-------------------------------")
            print(f"Product:      \t", shoe_.product)
            print("Code:          \t", shoe_.code)
            print("Price:         \t", shoe_.cost)
            print("Quantity:      \t", shoe_.quantity)
            print("Country:       \t", shoe_.country)
            print("-------------------------------")

#search_shoe("SKU95000")


def value_per_item(file_name):
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Read inventory.txt file first
    shoe_list = read_shoes_data(file_name)

    print("\nProducts and their total value")

    # Looping through shoe objects
    for shoe_ in shoe_list:
        cost = shoe_.get_cost()  # Getting cost
        quantity = shoe_.get_quantity()    # Getting quantity
        value = round(float(cost) * float(quantity), 3)    # cost * quantity

        print("-------------------------------")
        print(f"Product:      \t", shoe_.product)
        print("Code:          \t", shoe_.code)
        print("Price:        R\t", shoe_.cost)
        print("Quantity:      \t", shoe_.quantity)
        print("Total value:  R\t", str(value))
        print("-------------------------------")


#value_per_item()


def highest_qty(file_name):
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Read inventory.txt file first
    shoe_list = read_shoes_data(file_name)

    shoe_quant_list = []  # Empty shoe quantity list

    # Looping through shoe_list
    for shoe_ in shoe_list:
        # Adding value into shoe_quant_list
        shoe_quant_list.append(shoe_.quantity)


    # Returning search with highest quantity

    # First Converting elements in shoe_quant_list into an int
    shoe_quant_list = [int(shoe) for shoe in shoe_quant_list]

    # Getting the highest value from shoe_quant_list
    highest_quant = (max(shoe_quant_list))

    # Using the highest_quant to find the shoe_obj
    print("\nThe following shoes are on sale!")

    # looping through the shoe obj
    for shoe_ in shoe_list:
        # looking for instance with the highest quantity we are looking for
        if shoe_.quantity == str(highest_quant):
            # Returning search values
            print("-------------------------------")
            print(f"Product:      \t", shoe_.product)
            print("Code:          \t", shoe_.code)
            print("Price:         \t", shoe_.cost)
            print("Quantity:      \t", shoe_.quantity)
            print("Country:       \t", shoe_.country)
            print("-------------------------------")



#highest_qty()


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

user_choice = ""

while user_choice != "qt":
    # Variables
    file_name = "inventory.txt"
    ofile_name = "inventory.txt"

    # First read inventory.txt
    read_shoes_data(file_name)

    user_choice = input('''\nWhat would you like to do - 
va - View all products
cpt - Capture a product
rs - Re_stock products with lowest quantity
ss - Search for a product
val - View value per product
hg - View products with highest quantity
qt - quit? \n: ''')
    if user_choice == "va":
        # Run view_all function
        view_all(file_name)
    elif user_choice == "cpt":
        # Run capture_shoes function
        capture_shoes(file_name)

        # Read inventory.txt again to update the shoe_list for later use
        read_shoes_data(file_name)

    elif user_choice == "rs":
        # Run re_stock function
        re_stock(file_name)

        # Read inventory.txt again to update the shoe_list for later use
        read_shoes_data(file_name)

    elif user_choice == "ss":
        # Run search_shoe function
        shoe_id = input("\nEnter shoe code to search: ")
        search_shoe(file_name, shoe_id)

    elif user_choice == "val":
        # Run val_per_item function
        value_per_item(file_name)

    elif user_choice == "hg":
        # Run highest_qty function
        highest_qty(file_name)

    elif user_choice == "qt":
        print("\nGoodbye")
        exit()

    else:
        print("\nOops - incorrect input")




