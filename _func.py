from collections import Counter, OrderedDict
#from prettytable import PrettyTable

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
def count_alpha(ans_candidate):
    #alpha_list = [chr(ord("a")+i) for i in range(26)]
    ans_str = ''.join(ans_candidate)
    count_dict = Counter(ans_str)
    count_dict = OrderedDict({key_:count_dict[key_] /len(ans_str) * 5  for key_ in count_dict} )
    sorted_dict = OrderedDict( sorted(count_dict.items(), key=lambda x: x[1], reverse=True) )
    
    #table = PrettyTable()
    #table.add_column('alpha', sorted_dict.keys())
    #table.add_column('percentage', sorted_dict.values())
    
    return sorted_dict
        
    
    
        
        
    
    
