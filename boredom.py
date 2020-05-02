# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:11:46 2019
@author: marie
"""
# use a random # generator
# make a method - call service - you would form the url then

# start by importing requests - this is an HTTP library for Python
import requests
from random import randint


# users enter the corresponding number of the activity type they want to try
def type_of_act():
    types = input("Type the number only for each of the following choices "'\n'
                  "you can only choose one "'\n'
                  "1: charity, 2: relaxtion, 3: education, 4: recreational"'\n'
                  "5: music, 6: social, 7: cooking, 8: busywork, 9: diy "'\n')

    # run the number returned through check_num to be sure it's valid, if it's not go to the api
    check = check_num(int(types))
    if check != -1:
        # this matches the integer to the dictionary - this does not stop someone from putting in the
        # wrong number...so then they would get the wrong answer
        print(check)
        answer = types_dic[check]

        # this is taking the value from the dictionary and searching it in the api
        find_activity_types(answer)
    else:
        exit()


# this is used to check numbers entered by the users are between 1 and 9 (needs to be 10 since it includes 9)
def check_num(number):
    if number in range(1, 10):
        return number
    else:
        print("This entry is not valid")
        return -1

# method to find activities, call this when user wants to search for a type of activity
def find_activity_types(activity):
    url = "https://www.boredapi.com/api/activity?type="
    # formatting to set up the url so you can add the link and variable
    new_url = "{}{}".format(url, activity)
    # making a get request to the url send url to print_output
    values = print_output(new_url)
    # values is a tuple
    # print(type(values))

    print('One activity to try is ' + values)

def print_output(url):
    activity_response = requests.get(url)
    # save the response
    json_output = activity_response.json()
    # I don't want to return some of the fields, they are unnecessary - so I'm going to pull
    # out the fields I want - I put it in print_output method since I need it for all my calls
    activity = json_output['activity']
    # need to make price a string to print it - otherwise it will return an error
    # returns a tuple
    return activity


# find type of activities
def find_activities(activity):
    activity_response = requests.get("https://www.boredapi.com/api/activity?" + '"' + activity + '"')
    # print(activity_response.status_code)
    print(activity_response.json())

# types_dic is the dictionary of activity types to number
types_dic = {1: 'charity', 2: 'relaxation', 3: 'education', 4: 'recreational',
             5: 'music', 6: 'social', 7: 'cooking', 8: 'busywork', 9: 'diy'}

def random_act():
    import random
    print("Random activity generator!")
    rand_number = randint(1, 10)
    activityType = types_dic[rand_number]
    find_activity_types(activityType)


def num_of_participants(part):
    url = ("https://www.boredapi.com/api/activity?participants=" + str(part))
    retParticipant = print_output(url)
    print('One activity to try is ' + retParticipant)

def imBored():
    """use a while loop so that you can keep going through activities if you
    don't like what was offered you can go again - start by asking if the person is bored"""
    while True:
        bored = input('Are you bored? Answer y or n ')
        # If they are not bored, break the loop
        if bored == 'n':
            break
        else:
            """If they are bored there are three choices: choose based on a keyword (I give them
            choose by # of participants, or choose a random generated event - I added the hard return
            so that the user prompt is easier to read"""
            kind = input("Do you want to search based on a type of activity or by the number of participants? Or "
                         "should I get the random activity generator? \n" 
                         "1 to search by activity type" + '\n' + "2 to search by number of participants \n" 
                         "3 is to use the 'Random Activity Generator' \n")
            # Search by activity type - go up to the type_of_act() method
            if int(kind) == 1:
                type_of_act()

            if int(kind) == 2:
                num_part = input("Give the number of participants, use a number between 1 and 8 (max) \n")
                print(num_part)
                # has to have int before it or it will not be a number
                part = check_num(int(num_part))
                num_of_participants(part)
            if int(kind) == 3:
                random_act()

        input2 = input("Press any key to try again, type n to exit '\n")
        if input2 != 'n':
            continue
        else:
            break
    else:
        exit()

# main method
imBored()
