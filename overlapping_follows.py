import main_f
import pandas as pd

def get_follows(user_set):
    user_set_keys = list(user_set.keys())
    user_ids = [user_set[user_set_keys[0]], user_set[user_set_keys[1]]]
    main_f(user_ids)
    dict_of_follows = {} #create empty dictionary for the follows of each user in the list user_id
    for key in user_set:
        filename = '%s.csv' % user_set[key]
        df = pd.read_csv(filename) #read the file created by main(user_id)
        follows = df['username'].tolist() #convert follows column to list
        dict_of_follows[key] = follows #append follows list to user key of dictionary
    return dict_of_follows

def overlap(dict_of_follows):
    list_of_users = list(dict_of_follows)
    user1 = list_of_users[0]
    user2 = list_of_users[1]
    user1_follows = set(dict_of_follows[user1])
    user2_follows = set(dict_of_follows[user2])
    length_of_overlap = len(user1_follows.intersection(user2_follows))
    return length_of_overlap

def pct_overlap(dict_of_follows):
    avg_overlap = 0.05  # hardcoded average overlap value
    list_of_users = list(dict_of_follows)
    user1 = list_of_users[0]
    user2 = list_of_users[1]
    user1_follows = dict_of_follows[user1]
    user2_follows = dict_of_follows[user2]

    similarity = overlap(dict_of_follows)
    length = 0.0
    length = len(dict_of_follows[user1])
    overlap_amt = similarity/length * 1.0
    deviation_from_norm = round((overlap_amt - avg_overlap)/avg_overlap, 2) * 100.0
    output = ''
    if(deviation_from_norm < 0):
        output = str(round((similarity/length)*100,0)) + f'% of {user1}\'s follows overlap with {user2}\'s follows' + '\n' + 'That\'s ' + str(abs(deviation_from_norm)) + '% lower than average for two unrelated users.'
    else:
        output = str(round((similarity/length)*100,0)) + f'% of {user1}\'s follows overlap with {user2}\'s follows' + '\n' + 'That\'s ' + str(abs(deviation_from_norm)) + '% higher than expected for two unrelated users.'
    return output
