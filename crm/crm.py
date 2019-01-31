""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
    table = data_manager.get_table_from_file("crm/customers.csv")
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
        get_longest_name_id(table)
    elif answer == "5":
        get_subscribed_emails(table)

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
    new_record = []
    sales_records = ["name ", "e-mail: " , "subscribed: "]
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
    data_manager.write_table_to_file(file_name="crm/customers.csv", table=updated_table)
    
    return updated_table
    # your code
    #adding_table = common.add_table()
    #table.append(adding_table)
    #return table


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
    data_manager.write_table_to_file(file_name="crm/customers.csv", table=new_table)
    # your code
    # table.remove(table[id_])
    # return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    answer = common.add_table()
    table[id_] = answer
    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
