""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

    table = data_manager.get_table_from_file("sales/sales.csv")
    answer = common.sales_sub_menu()
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
        get_lowest_price_item_id(table)
    elif answer == "5":
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)


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
    sales_records = ["title: ", "price" , "month: ", "day: ","year"]
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
    data_manager.write_table_to_file(file_name="sales/sales.csv", table=updated_table)
    
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
    new_table = [entry for entry in table if entry[0] != id_]
    # print("frm remove() -> {}".format(new_table))
    data_manager.write_table_to_file(file_name="sales/sales.csv", table=new_table)
    #for i in table:
    #    if id_ in i[0]:
    #        table.remove(i)
    #        ui.print_result()
    #if id_ != i[0]:
    #    ui.print_error_message('ID not found!')
    #return table
    # table.remove(table[id_])
    #return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.
    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
    Returns:
        table with updated record
    """

    for i in table:
        if id_ == i[0]:
            update_table = ["Title",
                            "Price",
                            "Month",
                            "Day",
                            "Year"]
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
            elif option == "5":
                i[5] = updating[0]
            #ui.printresult('Transaction succesfully updated!', '')
    if id != i[0]:
        ui.print_error_message("ID do not exist")
        data_manager.write_table_to_file(file_name="./sales/sales.csv", table=table)
    return table

# special functions:

# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code

