import pandas as pd
data = pd.read_csv("Sports.csv")
print(data)
number_of_attributes=len(data.columns)-1
hypothesis=['0']*number_of_attributes
print("H-0:",hypothesis)
for index, row in data.iterrows():
    if row[len(row)-1]== 'Yes':
        for colIndex in range(len(row)-1):
            if hypothesis[colIndex]=='0':
                hypothesis[colIndex]=row[colIndex]
            elif hypothesis[colIndex] != row[colIndex]:
                hypothesis[colIndex]='?'
    print("H-",str(index+1),":",hypothesis)
print("S:",hypothesis)
