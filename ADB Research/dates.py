import numpy as np
import pandas as pd

dates = np.loadtxt("dates.csv", dtype = str, skiprows = 1)

for i in range(len(dates)):
    dates[i] = dates[i][0:4]
    dates[i] = int(dates[i])

df = pd.DataFrame(dates)
df.to_csv("dates2.csv")