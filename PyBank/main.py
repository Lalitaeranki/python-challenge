import os,csv
#declaring the arrays
Months=[]
Pro_loss=[]
ave_change=[]
revenue_change=[]
#reading the csv file
py_bank=os.path.join('..','PyBank',"budget_data.csv")
with open ("budget_data.csv",'r')as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
#remove header from file
    headers=next(csvreader,None)
    count=0
    total_amount=0
#calculations for total months and total profit/loss
    for i in csvreader:
        Months.append(i[0])
        Pro_loss.append(float(i[1]))
        count+=1
#calculating aerage change maximun and minimum change
for k in range(1,count):
    
    ave_change.append((Pro_loss[k])-(Pro_loss[k-1]))
    revenue_change=sum(ave_change)/len(ave_change)
maximum_change=max(ave_change)
index_maximum= ave_change.index(max(ave_change))
minimum_change=min(ave_change)
index_minimum= ave_change.index(min(ave_change))
#since the ave-change has 85 rows added +1 to point to correct month
print('Financial Analysis')
print("-------------------------------")
print("Total Months:",len(Months))
print("Total:",round(sum(Pro_loss),2))
print("Average Change:",round(revenue_change,2))
print("Greatest Increase in Profits:",Months[index_maximum+1],"(","$",round(maximum_change),")")
print("Greatest Decrease in Profits:",Months[index_minimum+1],"(","$",round(minimum_change),")")
#python main.py > result_bank.txt