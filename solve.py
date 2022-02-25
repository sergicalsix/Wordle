import pandas as pd
#https://github.com/alex1770/wordle/blob/main/wordlist_hidden
from _func import *
df = pd.read_csv('wordle_ans.csv',header=None)
#df = pd.read_csv('wordle_all.csv',header=None)
#print(df.head())
ans0:list = df[0].values

pos_dict = {}
non_pos_dict = {}
non_character_list = ['a','r','e','s','f','l','o','u','t','g','h']
character_list = []
    
ans1 = character_position_select(ans0, pos_dict )
ans2 = character_select(ans1, character_list )
ans3 = character_not_select(ans2,non_character_list)
print(ans3)
print(count_alpha(ans3))
print(len(ans1),len(ans2),len(ans3),len(ans0))

        
        
    
    
