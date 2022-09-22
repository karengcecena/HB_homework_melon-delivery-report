"""Delivery Reports"""

import sys


def deliveries_for_each_day(a):
    """This function prints out the day number and the deliveries that happen that day
    
    To use it, put in day number when calling the function

    ex: 
    >>> deliveries_for_each_day(1)
    
    """
    # Allows delivery_files to be set to the first index of the function called at the terminal
    delivery_files = open(f"um-deliveries-day-{a}.txt")

     # Finds the day number and prints it out
    day_number = int(a)
    print()
    print(f"Day {day_number}:")

    # Added line and space for clarity
    print("---------------------")
    print()

    for line in delivery_files:
        # This removes trailing white space:
        line = line.rstrip()
        # This separates the line into strings definined by the line
        words = line.split('|')

        # Collect from indexes in words to return corrrect variable
        melon = words[0]
        count = words[1]
        amount = words[2]

    # Prints out the delivery message with the count of melons and total cost. 
        print(f"- Delivered {count} {melon}s for total of ${amount}")

    # Added space for clarity
    print()

deliveries_for_each_day(1)
deliveries_for_each_day(2)
deliveries_for_each_day(3)


########################################################################################
# Alternative method (first version) can be found below where sysargv[] was used
# def deliveries_for_each_day():
#     """This function prints out the day number and the deliveries that happen that day
    
#     To use it, run the program and add the day's text you want to see the delivery for
    
#     ex (missing all outputs): 
#     >>> python3 produce_summary.py um-deliveries-day-1.txt
#     Day 1
#     Delivered 18 Ali Baba Watermelons for total of $25.00
    
#     """
#     # Allows delivery_files to be set to the first index of the function called at the terminal
#     delivery_files = sys.argv[1]

#      # Finds the day number and prints it out
#     day_number = delivery_files[-5]
#     print(f"Day {day_number}")

#     for line in open(delivery_files):
#         # This removes trailing white space:
#         line = line.rstrip()
#         # This separates the line into strings definined by the line
#         words = line.split('|')

#         melon = words[0]
#         count = words[1]
#         amount = words[2]

#     # Prints out the delivery message with the count of melons and total cost. 
#         print(f"Delivered {count} {melon}s for total of ${amount}")

# deliveries_for_each_day()

################################################################