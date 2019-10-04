#!/usr/bin/python3
#
# Nicole Benoit
# Sep 5 2019  21:47:00.470 -06:00

min_Size = 6
max_Size = 15
####################################
# Create a password validation program utilizing a WhiteList
####################################
import re

print("WhiteList Test")

while True:
    wpsswd = input("Enter in a password between {} and {} characters: ".format(min_Size, max_Size))

    if (len(wpsswd) < 6 or len(wpsswd) > 15):
        print("Outside character range. Try again.")
        continue
    elif re.search('[0-9]', wpsswd) is None:
        print("Must contain at least 1 number")
        continue
    elif re.search('[A-Z]', wpsswd) is None:
        print("Must contain at least 1 capital letter")
        continue

    break

####################################
# Create a password validation program utilizing a BlackList
####################################

print("\nBlackList Test")

# Create blacklist for special chars . , ; : \ | ` ' " # @ $
blackList = ".,;:\\#\@|\`\'\"$()[]{}/"

while True:
    bpsswd = input("Enter in a password between {} and {} characters: ".format(min_Size, max_Size))

    if (len(bpsswd) < 6 or len(bpsswd) > 15):
        print("Outside character range. Try again.")
        continue
    elif any(ch in blackList for ch in bpsswd):
        print("Invalid character: Try again.")
        continue

    break

####################################
# Lab work
####################################

# mylist = ["obj1","obj2","obj3"]
# myvar1 = 32
# myvar2 = "Something else"
#
# print('{}{}'.format(myvar1, myvar2))
# print('{1}{0}'.format(myvar1, myvar2))
# print('{}{}'.format(mylist[1], mylist[2]))
#

# import logging
# logging.basicConfig(filename='logtest.log', level = logging.INFO)
# logger = logging.getLogger(__name__)
#
# logger.info('starting for statement')
# for i in range(1,13):
#     print("{:3d}{:4d}{:5d}".format(i, i**2, i**3))
# logger.info('Done with for loop')
