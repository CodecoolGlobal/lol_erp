""" Common module
implement commonly used functions here
"""

import random

import hr

def generate():
    numbers = '0123456789'
    lowwerCaseLetters = 'abcdefghijklmnopqrstuvwxyz'
    upperCaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowwer = random.choice(lowwerCaseLetters)
    upper = random.choice(upperCaseLetters)
    num = random.choice(numbers)
    generated = num + num + lowwer + lowwer + upper + upper
    return generated

def checking_ids(table):
    ids = []
    for element in table:
        if element[0]:
            ids.append(element[0])

    generated = generate()

    while True:
        if generated in ids:
            generated = generate()
        else:
            break

    return generated


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    checking_ids(table)


    return generated


def hr_sub_menu():
    print("""(0)Show table
             (1)Add
             (2)Remove
             (3)Update
             (4)Get oldest person
             (5)Get persons closest to average""")
    answer = input("Choose number: ")
    return answer

def store_sub_menu():
    print("""(0)Show table
            (1)Add
            (2)Remove
            (3)Update
            (4)Get counts by manufacturers
            (5)Get average by manufacturers""")
    answer = input("Choose number: ")
    return answer

def sales_sub_menu():
    print("""(0)Show table
        (1)Add
        (2)Remove
        (3)Update
        (4)Get lowest price item id
        (5)Get items sold between""")
    answer = input("Choose number: ")
    return answer


def print_only_table(table):
    longest_w = longest_words(table)
    lenght = table_lenght(longest_w)
    print("/" + "-" * (lenght + 3) + "\\")

    z = 1
    for element in table:
        j = 0

        print("|" + " " + str(z).zfill(2) + " ", end="")
        z += 1


        for item in element:
            print("|" + " " * (len(longest_w[j]) - len(item)) + item + " ", end="")
            j += 1
        print("|", end="")
        print('\n', end="")
        k = 0
        print("|" + "----", end="")
        for item in element:
            print("|" + "-" * len(longest_w[k]) + "-", end="")
            k += 1
        print("|", end="")
        print("\n", end="")

    print("\\" + "-" * (lenght + 3) + "/")

def table_lenght(longest_words):
    lenght = 0
    for i in range(0, len(longest_words)):
        lenght += (len(longest_words[i]) + 2)
    return lenght


def longest_words(table):
    longest_words = []
    for i in range(0, len(table[0])):
        longest_words.append("")
    for element in table:
        i = 0
        for item in element:
            if len(item) > len(longest_words[i]):
                longest_words[i] = item


            i += 1
    return longest_words


def add_table():
    answer = [str(x) for x in input("write somefing :) ").split(',')]
    return answer

def id_table():
    id_ = int(input("enter the ID from the table you want to change "))
    return id_

def sorted_function(item):

    return sorted(item)