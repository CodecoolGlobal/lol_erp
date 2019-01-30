""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
from data_manager import get_table_from_file

def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.
    Returns:
        None
    """
    #table = get_table_from_file("hr/persons.csv")
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
        get_oldest_person(table)
    elif answer == "5":
        get_persons_closest_to_average(table)


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

    adding_table = common.add_table()
    table.append(adding_table)
    #print(table)
    return table


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

# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code

