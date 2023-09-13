#%%

import numpy as np
import pandas as pd

#Non Legit version
df = pd.read_csv("1997 voting power data.csv")
print(df)

topten = []
votingpower = df["Voting Power"]
votingpower = np.sort(votingpower)[::-1]
print(votingpower)
for i in range(10):
    temp = votingpower[i]
    for j in range (len(df["Voting Power"])):
        if (df.iloc[j][1] == temp):
            check = False
            for k in range(len(topten)):
                if (df.iloc[j][0]==topten[k]):
                    check = True
            if (check == False):
                topten.append(df.iloc[j][0])

print(topten)



# %%

#%%
#Legit Version Below
df = pd.read_csv("1997 voting power data.csv")
print(df)

topten = []
votingpower = df["Voting Power"]
votingpower = np.sort(votingpower)[::-1]
print(votingpower)
i = 0
while(i<10):
    temp = votingpower[i]
    compare = votingpower[i+1]
    for j in range(len(df["Voting Power"])):
        if (df.iloc[j][1] == temp):
            if (temp != compare):
                topten.append(df.iloc[j][0])
                i +=1
            else:
                topten.append(df.iloc[j][0] + "(T)")
                for k in range(j+1,len(df["Voting Power"])):
                    if(df.iloc[k][1] == temp):
                        topten.append(df.iloc[k][0] + "(T)")
                        i += 2
                break
print(topten)
print(len(topten))

# %%
