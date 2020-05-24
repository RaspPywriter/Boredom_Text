# Boredom_Text 
This is a simple Python program that allows a user to pick activities in one of three ways:
1. By activity type (ex: charitable, DIY)
2. Number of participants
3. Random Activity Generator

This version of the program does not have a UI interface at this point.

This program uses the bored API (https://www.boredapi.com/) to return activities to users. Users can choose to keep trying to get more activities or exit the program.
## Program Details
This program is just one Python file. It is divided into different methods:
### def imBored() 
The imBored method is the main method of the program. It starts by asking the user if they are bored, and if yes, it gives them three options for finding an activity.
1. Find an activity by the type of activity (ex: charitable) - this is accessed by the type_of_act method.
2. Find an activity by the number of participants - this method is accessed through the num_of_participants method.
3. Finally, the user can choose for a random activity to be selected for them, this method is called by random_act.
### def type_of_act()
This method is called when a user wants to search by type of activity. There are 9 options. The user selects numbers 1 -9, and that leads to the check_num method which verifies that it's a number between 1 and 9. If it is between 1 - 9, then it takes the number and pulls that key from the dictionary that I created based upon the options on the boredom api.

### def num_of_participants(part)

### def check_num(number)
This method is called anytime you want to verify that it's a number between 1 and 9
### def random_act()

