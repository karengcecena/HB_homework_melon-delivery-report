"""Delivery Reports"""

import sys

def deliveries_for_each_day():
    """This function prints out the day number and the deliveries that happen that day
    
    To use it, run the program and add the day's text you want to see the delivery for
    
    ex (missing all outputs): 
    >>> python3 produce_summary.py um-deliveries-day-1.txt
    Day 1
    Delivered 18 Ali Baba Watermelons for total of $25.00
    
    """
    # Allows delivery_files to be set to the first index of the function called at the terminal
    delivery_files = sys.argv[1]

     # Finds the day number and prints it out
    day_number = delivery_files[-5]
    print(f"Day {day_number}")

    for line in open(delivery_files):
        # This removes trailing white space:
        line = line.rstrip()
        # This separates the line into strings definined by the line
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

   

    # Prints out the delivery message with the count of melons and total cost. 
        print(f"Delivered {count} {melon}s for total of ${amount}")

deliveries_for_each_day()

################################################################

# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()