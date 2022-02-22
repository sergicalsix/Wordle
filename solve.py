import pandas as pd
#https://github.com/alex1770/wordle/blob/main/wordlist_hidden

df = pd.read_csv('wordle_ans.csv',header=None)
#df = pd.read_csv('wordle_all.csv',header=None)
#print(df.head())
ans0:list = df[0].values

pos_dict = {3:'o'}
non_pos_dict = {}
character_list = ['o','r','t']
non_character_list = ['a','i','s','l','f','u','e']
#non_character_list = []

def character_select(ans_candidate,character_list:list):
    if len(character_list) == 0:
        return ans_candidate
    ans_set = set([])
    for c in character_list:
        ans_ = [a for a in ans_candidate if c in a]
        if len(ans_set) == 0:
            ans_set = set(ans_)
        else:
            ans_set = ans_set.intersection(set(ans_))
    return list(ans_set)

def character_not_select(ans_candidate,character_list:list):
    if len(character_list) == 0:
        return ans_candidate
    ans_set = set([])
    for c in character_list:
        ans_ = [a for a in ans_candidate if c not in a]
        if len(ans_set) == 0:
            ans_set = set(ans_)
        else:
            ans_set = ans_set.intersection(set(ans_))
    return list(ans_set)

def character_position_select(ans_candidate,character_position_dict):
    if len(character_position_dict.keys()) == 0:
        return ans_candidate
    """
    character_postion_dict: {1:'f'}
    """
    ans_set = set([])
    for k,v in character_position_dict.items():
        ans_ = [a for a in ans_candidate if a[int(k) - 1] == v]
        if len(ans_set) == 0:
            ans_set = set(ans_)
        else:
            ans_set = ans_set.intersection(set(ans_) )
    return list(ans_set)

def character_position_not_select(ans_candidate,character_position_dict):
    if len(character_position_dict.keys()) == 0:
        return ans_candidate
    """
    character_postion_dict: {1:'f'}
    """
    ans_set = set([])
    for k,v in character_position_dict.items():
        ans_ = [a for a in ans_candidate if a[int(k) - 1] != v]
        if len(ans_set) == 0:
            ans_set = set(ans_)
        else:
            ans_set = ans_set.intersection(set(ans_) )
    return list(ans_set)
#def count_alpha(ans_candidate):
    
    
#文字と場所による絞り込み
#含まれている文字による絞り込み
ans1 = character_position_select(ans0, pos_dict )
ans2 = character_select(ans1, character_list )
ans3 = character_not_select(ans2,non_character_list)
print(ans3)
print(len(ans1),len(ans2),len(ans3),len(ans0))

        
        
    
    
