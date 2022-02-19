import pandas as pd
import copy
#https://github.com/alex1770/wordle/blob/main/wordlist_hidden
df = pd.read_csv('wordle_ans.csv',header=None)
#print(df.head())
ans0:list = df[0].values

pos_dict = {3:'i'}
character_list = ['i','s']
non_character_list = ['r','e','a','t','o','u','g','h','p','k','y']

def character_select(ans_candidate,character_list:list):
    ans_set = set([])
    for c in character_list:
        if len(ans_set) == 0:
            ans_set = set([a for a in ans_candidate if c in a]) 
        else:
            ans_set = ans_set.intersection(set([a for a in ans_candidate if c in a]) )
    return list(ans_set)

def character_position_select(ans_candidate,character_postion_dict):
    """
    character_postion_dict: {1:'f'}
    """
    ans_ = copy.deepcopy(ans_candidate)

    for k,v in character_postion_dict.items():
        ans_ = [a for a in ans_ if a[int(k) - 1] == v]
    return ans_

def character_not_select(ans_candidate,character_list:list):
    ans_set = set([])
    for c in character_list:
        if len(ans_set) == 0:
            ans_set = set([a for a in ans_candidate if c not in a])
        else:
            ans_set = ans_set.intersection(set([a for a in ans_candidate if c not in a]) )
    return list(ans_set)

#def count_alpha(ans_candidate):
    

#文字と場所による絞り込み
#含まれている文字による絞り込み
ans1 = character_position_select(ans0, pos_dict )
ans2 = character_select(ans1, character_list )
ans3 = character_not_select(ans2,non_character_list)
print(ans3)
print(len(ans1),len(ans2),len(ans3),len(ans0))

        
        
    
    
