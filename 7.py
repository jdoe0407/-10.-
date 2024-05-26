import random 
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10 
random.shuffle(lst)
data = pd.DataFrame({'whoAmI:_robot':list(map(lambda x: True if x=='robot' else False, lst)), 'whoAmI:_human':list(map(lambda x: True if x=='human' else False, lst))})


print(data)