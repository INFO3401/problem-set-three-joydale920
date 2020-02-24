## run credit data here with the load and clean code
from utils import *

df = loadAndCleanData("./data/creditData.csv")

print (df)


#computerPDF = plt.show(credit_df)

computerPDF("age",df)


# loop through column names 

for column in df:
	computerPDF(column,df) 


viewDistribution("age",df)

for column in df:
	viewDistribution(column,df)

# number 7 need help on




bins = computeBins(row, data)
for bin in bins:
	print(row, bin)
	computeDefaultRisk("SeriousDlqin2yrs",[bin.left,bin.right],row,data)




new_df = loadAndCleanData("./data/newLoans.csv")
print(new_df)

# Office hours for 11-18 =(





