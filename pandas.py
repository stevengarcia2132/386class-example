import pandas as pd
import numpy as np
x= [1,2,3,4,5]
lab = ['a','b','c','d','e']
s= pd.Series(x,index=lab)
print(pd.__version__)

s.mean()
np.mean(s)

df = pd.DataFrame()
d = pd.DataFrame()
#d= {'state',:['ohio','wyoming','utah']}
#df

#df.index = df['state']
#del df['state']


#iris.head()
