""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    table = data_manager.get_table_from_file("store/games.csv")
    answer = common.store_sub_menu()
    #manufacturer = 'Frictional Games'
    if answer == "0":
        show_table(table)
    elif answer == "1":
        add(table)
    elif answer == "2":
        id_ = common.id_table()
        remove(table, id_)
        #data_manager.write_table_to_file(file_name="./store/games.csv", table=table)
    elif answer == "3":
        id_ = common.id_table()
        update(table, id_)
    elif answer == "4":
        get_counts_by_manufacturers(table)
    elif answer == "5":
        get_average_by_manufacturer(table, manufacturer)


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    common.print_only_table(table)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    new_record = []
    sales_records = ["title: ", "manufacturer" , "price: ", "in stock: "]
    id = common.generate()
    new_record.append(id)
    i = 1
    title = input(sales_records[0])
    new_record.append(title)
    while i < len(sales_records):
        integer_inputs = input(sales_records[i])
        if integer_inputs.isdigit():
            new_record.append(integer_inputs)
            i += 1

        else:
            print("error!")
    print(new_record)
    updated_table = table + [new_record]
    # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    # print("updated table: {}".format(updated_table))
    data_manager.write_table_to_file(file_name="store/games.csv", table=updated_table)
    
    return updated_table
    # titles = ["game", "manofacture", "price", "game in stock"]
    # #updatedtable = []
    # zmienna = ui.get_inputs(titles, "co chcesz zapisac")
    # zmienna.insert(0, common.generate())
    # print(zmienna)
    # table.append(zmienna)
    # data_manager.write_table_to_file('games.csv', table)
    # return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    new_table = [entry for entry in table if entry[0] != id_]
    # print("frm remove() -> {}".format(new_table))
    data_manager.write_table_to_file(file_name="store/games.csv", table=new_table)
    # data_manager.write_table_to_file(file_name="store/games.csv", table=updated_table)
    # your code
    # table.remove(table[id_])
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    for i in table:
        if id_ == i[0]:
            update_table = ["Title",
                            "Manufacturer",
                            "Price",
                            "Games in stock"]
            ui.print_menu("What do you want to change?", update_table, "Back to store menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "0":
                break
            updating = ui.get_inputs([update_table[int(option) - 1] + ": "], "")
            if option == "1":
                i[1] = updating[0]
            elif option == "2":
                i[2] = updating[0]
            elif option == "3":
                i[3] = updating[0]
            elif option == "4":
                i[4] = updating[0]
            #ui.printresult('Transaction succesfully updated!', '')
    if id != i[0]:
        ui.print_error_message("ID do not exist")
        data_manager.write_table_to_file(file_name="./store/games.csv", table=table)
    return table
    # answer = common.add_table()
    # table[id_] = answer
    # return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code
    manufacturer = []
    games = []
    diction = {}

    for element in table:
        if element[2] not in manufacturer:
            manufacturer.append(element[2])

    for i in range(len(manufacturer)):
        for element in table:
            if element[2] == manufacturer[i]:
                games.append(element[1])
        lenght = len(games)
        diction[manufacturer[i]] = lenght

        games = []

    print(diction)
    return diction



def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
