import pandas as pd

data = {'a':[1,2,3],'b':[4,5,6]}
rowlabel = ['c','d','e']

newdataframe = pd.DataFrame(data,index=rowlabel)

print(newdataframe)