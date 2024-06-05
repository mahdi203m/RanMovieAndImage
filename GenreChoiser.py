import datetime
import requests
from collections import OrderedDict
import numpy as np
import webbrowser

def Number_Of_People():
    '''
    This Function Will Identify The Number
    Of People As I Named This Function
    '''
    repeater = True
    counter = 0
    global horror_counter,romance_counter,comedy_counter,history_counter,adventure_counter,action_counter
    horror_counter = 0
    romance_counter = 0
    comedy_counter = 0
    history_counter = 0 
    adventure_counter = 0
    action_counter = 0
    people_counter = int(input('Please Enter The People Number:'))
    for i in range(1,people_counter+1):
        counter = 0
        people_name = input(f'Please Enter Person {i} Name:')
        while(repeater):
            people_choise = input(f'Mr/Mrs {people_name} Please Choise Between (Horror, Romance, Comedy, History , Adventure , Action):')
            counter+=1
            if(counter == 3):
                break
            match people_choise:
                case 'Horror':
                    horror_counter+=1
                case 'Romance':
                    romance_counter+=1
                case 'Comedy':
                    comedy_counter+=1
                case 'History':
                    history_counter+=1
                case 'Adventure':
                    adventure_counter+=1
                case 'Action':
                    action_counter+=1

Number_Of_People()

def printer():
    '''
    This Function Will Display All Data To User
    '''
    global horror_counter,romance_counter,comedy_counter,history_counter,adventure_counter,action_counter,my_dictionary,sorted_dict
    print(f'The Data Displayed At:{datetime.datetime.now()}')
    my_dictionary = {f'Horror':{horror_counter},f'Romance':{romance_counter},f'Comedy':{comedy_counter},f'History':{history_counter},f'Adventure':{adventure_counter},f'Action':{action_counter}}
    keys = list(my_dictionary.keys())
    values = list(my_dictionary.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    print(sorted_dict)

printer()

def search_movie_by_genre():
    """
    this function will find a movie by the 
    more point that genre has
    """
    global horror_counter,romance_counter,comedy_counter,history_counter,adventure_counter,action_counter,my_dictionary,sorted_dict
    webbrowser.open("https://api3.haji-api.ir/majid/fun/wallpaper/random?license=jkoIUSraDCVyJwMddGf0dSLcjTZWuumaMvVFGnNdLy")

search_movie_by_genre()


