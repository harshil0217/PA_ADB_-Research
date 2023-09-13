import numpy as np
import pandas as pd

df = pd.read_csv("2007data.csv", encoding='cp1252')
print(df)

topten = []
votingpower = df["Voting power"]
votingpower = np.sort(votingpower)[::-1]
print(votingpower)
i = 0
while(i<35):
    temp = votingpower[i]
    templist = []
    for j in range(len(df["Voting power"])):
        if (df.iloc[j][1] == temp):
            templist.append(df.iloc[j][0])
    if (len(templist)==1):
        topten.append(templist[0] + "(" + str(temp) + ")")
        i += 1
    else:
        for k in range(len(templist)):
            topten.append(templist[k] + "(" + str(temp) + ")" + "(T)")
        i += len(templist)

print(topten)
print(len(topten))