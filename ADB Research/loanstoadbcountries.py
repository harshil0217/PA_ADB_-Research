import numpy as np
import pandas as pd

loans = pd.read_csv("worldbankloans.csv")
print(loans)

commitments = pd.DataFrame()

def unique(c_list):
    u_list = []
    for entry in c_list:
        test = False
        for item in u_list:
            if (entry == item):
                test = True
        if (test == False):
            u_list.append(entry)
    return u_list

years = np.sort(unique(loans["Years"]))
print(years)

dmcs = unique(np.sort(np.loadtxt("adbdmcs.csv", skiprows = 1, usecols=0, dtype = str, delimiter = ",", unpack = True)))
dmcs[0] = "Taipei"
dmcs = np.sort(dmcs)
print(dmcs)

countries = []
for i in range(len(loans["Country"])):
    inlist = False
    for j in range(len(dmcs)):
        if (loans["Country"][i]==dmcs[j]):
            inlist = True
    if (inlist == True):
        countries.append(loans["Country"][i])

countries = unique(countries)
print(countries)
print(len(countries))

print(len(years))

commitments = pd.DataFrame(index = countries, columns = years)
print (commitments)
    
for country in countries:
    for year in years:
        sum = 0
        for i in range(len(loans["Country"])):
            if (loans.iloc[i,2] == "Commitments"):
                if ((loans.iloc[i,0] == year) and (loans.iloc[i,1] == country)):
                    sum = sum + loans.iloc[i,3]
        commitments.loc[country, year] = sum

print(commitments)

disbursements = pd.DataFrame(index = countries, columns = years)

for country in countries:
    for year in years:
        sum = 0
        for i in range(len(loans["Country"])):
            if (loans.iloc[i,2] == "Gross Disbursements"):           
                if ((loans.iloc[i,0] == year) and (loans.iloc[i,1] == country)):
                    sum = sum + loans.iloc[i,3]
        disbursements.loc[country, year] = sum

print(disbursements)

commitments.to_csv("commitments.csv")
disbursements.to_csv("disbursements.csv")
