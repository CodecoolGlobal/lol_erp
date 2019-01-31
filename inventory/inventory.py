""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""
# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.
    Returns:
        None
    """

    table = data_manager.get_table_from_file("inventory/inventory.csv")
    answer = common.hr_sub_menu()
    if answer == "0":
        show_table(table)
    elif answer == "1":
        add(table)
    elif answer == "2":
        id_ = common.id_table()
        remove(table, id_)
    elif answer == "3":
        id_ = common.id_table()
        update(table, id_)
    elif answer == "4":
        get_available_items(table)
    elif answer == "5":
        get_average_durability_by_manufacturers(table)


def show_table(table):
    """
    Display a table
    Args:
        table: list of lists to be displayed.
    Returns:
        None
    """

    common.print_only_table(table)


def add(table):
    """
    Asks user for input and adds it into the table.
    Args:
        table: table to add new record to
    Returns:
        Table with a new record
    """
    new_record = []
    sales_records = ["year: ", "manufacturer: " , "purchase_year: ", "durabelity:  ",]
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
    data_manager.write_table_to_file(file_name="inventory/inventory.csv", table=updated_table)
    
    return updated_table
    #adding_table = common.add_table()
    #table.append(adding_table)
    #return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.
    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed
    Returns:
        Table without specified record.
    """

    table.remove(table[id_])
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.
    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
    Returns:
        table with updated record
    """

    answer = common.add_table()
    table[id_] = answer
    return table

#special functions

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code


