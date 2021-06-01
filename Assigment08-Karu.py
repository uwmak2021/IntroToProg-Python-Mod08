# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MKarumuhinzi,05.31.2021,Modified code to complete assignment 8
# MKarumuhinzi,06.01.2021,Tested code to ensure everything run properly.
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""  # Captures the user option selection


class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
        
    methods:
        add_data_to_list(self, list_of_product_objects): -> (list) list of product objects
        
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MKarumuhinzi,05.31.2021,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, product_name, product_price):
        # Attributes
        self.__product_name = product_name
        self.__product_price = product_price
    
    # -- Properties --
    # product_name
    @property
    def product_name(self):  # getter
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):  # setter
        if value and value.strip():
            self.__product_name = value
        else:
            raise Exception("Names cannot be empty.")
        
    # product_price
    @property
    def product_price(self):  # getter
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):  # setter
        try:
            self.__product_price = float(value)
        except ValueError:
            raise Exception("Price must be a number.")
    
    def add_data_to_list(self, list_of_product_objects):
        """ Add a product to the list/Table

        :param list_of_product_objects: (list) list of product objects to add product to:
        :return: (list, boolean) list of product objects rows
        """
        list_of_product_objects.append({"Product":str(self.__product_name).strip(), "Price":str(self.__product_price).strip()})
        return list_of_product_objects
    
# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): -> (list, boolean)
        a list of product objects and True if succeeded writing in the file, False otherwise

        read_data_from_file(file_name): -> (list, boolean) 
        a list of product objects and True if succeeded reading the file, False otherwise

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MKarumuhinzi,05.31.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Write data to a file from a list of rows

        :param file_name: (string) with name of file
        :param list_of_product_objects: (list) of data saved to file
        :return: (list, boolean) of rows and True if succeeded writing in the file, False otherwise
        """
        is_success = False
        
        try:
            # deleting all the products is success
            if len(list_of_product_objects) == 0:
                is_success = True
            
            file = open(file_name, "w")
            for row in list_of_product_objects:
                file.write(row["Product"] + ", $" + row["Price"] + "\n")
                is_success = True
            file.close()
        except FileNotFoundError as e:
            print("Data file not found: ", file_name)
        except Exception as e:
            print("There was a non-specific error: ")
            print(e, e.__doc__, type(e), sep='\n')
        
        return list_of_product_objects, is_success
    
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of rows
        
        :param file_name: (string) with name of file:
        :return: (list, boolean) of rows and True if the file contains some data, False otherwise
        """
        is_success = False
        list_of_rows = []  # A list that acts as a 'table' of rows

        try:
            file = open(file_name, "r")
            for line in file:
                product_name, product_price = line.split(", ")
                row = {"Product": product_name.strip(), "Price": product_price.replace('$', '').strip()}
                list_of_rows.append(row)
                is_success = True
            file.close()
        except FileNotFoundError as e:
            print("Data file not found: ", file_name)
        except Exception as e:
            print("There was a non-specific error: ")
            print(e, e.__doc__, type(e), sep='\n')
        
        return list_of_rows, is_success

# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks:

    methods:
        print_menu_Tasks(): -> None
        input_menu_choice(): -> (int) choice
        print_current_data_in_list(list_of_rows): -> None
        input_yes_no_choice(message): -> (string) choice
        input_press_to_continue(optional_message=''): -> None
        input_product(): -> (product_name, product_price) product name and price

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MKarumuhinzi,05.31.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add Product
        2) Save Data to File        
        3) Reload Data from File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks
    
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice
    
    @staticmethod
    def print_current_data_in_list(list_of_rows):
        """ Shows the current products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for row in list_of_rows:
            print(row["Product"] + ": $" + row["Price"])
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :param message: (string) question yes/no to to display
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_product():
        """ Gets product name and price from the user

        :return: (string, string) product name and price
        """
        product_name = input("Enter the name:")
        product_price = input("Enter the price:")
        
        return product_name, product_price
    
# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects, bSuccess = FileProcessor.read_data_from_file(strFileName)  # read file data
print()

product = Product("", 0.0)  # initialization
# Display a menu of choices to the user
while(True):
    # Show current data
    IO.print_current_data_in_list(lstOfProductObjects)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Process user's menu choice
    if strChoice.strip() == '1':  # New Product
        product_name, product_price = IO.input_product()
        
        is_success = False
        try:
            product.product_name = product_name
            product.product_price = product_price
            lstOfProductObjects = product.add_data_to_list(lstOfProductObjects)
            is_success = True;
        except Exception as e:
            print(e)
        
        print()
        if is_success == True:
            print('Product added')
        else:
            print("Operation failed")

        IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '2':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstOfProductObjects, bSuccess = FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print()
            if bSuccess == True:
                print("Data saved.")
                IO.print_current_data_in_list(lstOfProductObjects)
            else:
                print("Data not saved.")
            IO.input_press_to_continue()
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '3':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstOfProductObjects, bSuccess = FileProcessor.read_data_from_file(strFileName)
            print()
            if bSuccess == True:
                IO.print_current_data_in_list(lstOfProductObjects)
            else:
                print('No product found.')
            IO.input_press_to_continue()
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  #  Exit Program
        print("Goodbye!")
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #

