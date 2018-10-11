import pandas as pd
import numpy as np

s=pd.Series([1,3,5,np.nan,6,8])
print(s)
print(type(s))


s1=pd.Series(['A','B',2,5,np.nan,'C'])
print(s1)
print(type(s1))

s2=pd.Series([1,3,5,6,8])
print(s2)
print(type(s2))
