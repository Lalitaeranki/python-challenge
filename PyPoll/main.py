import os,csv
#declaring the arrays
total_votes=[]
County=[]
Candidate=[]
candidate_no=[]
#reading the csv file
py_bank=os.path.join('..','PyPoll',"election_data.csv")
with open ("election_data.csv",'r')as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
#remove header from file
    headers=next(csvreader,None)
    count=0
    vote1=0
    vote2=0
    vote3=0
    vote4=0
    totalvotes_sum=0
#calculations for total months and total profit/loss
    for i in csvreader:
        total_votes.append(i[0])
        County.append(str(i[1]))
        Candidate.append(str(i[2]))
        count+=1
#print(count)
cand=set(Candidate)
candidate_no=sorted(cand,reverse=True)
#print(candidate_no)
#print(cand)
for k in range(1,count):       
    if (str(candidate_no[0])==str(Candidate[k])):
        vote1+=1
    if (str(candidate_no[1])==str(Candidate[k])):
        vote2+=1
    if (str(candidate_no[2])==str(Candidate[k])):
        vote3+=1
    if (str(candidate_no[3])==str(Candidate[k])):
        vote4+=1
votes=[vote1,vote2,vote3,vote4]   
#print("Total Votes:",len(total_votes))
#print(votes)
totalvotes_sum=sum(votes)
percentage_change_voter_1=(vote1/totalvotes_sum)
percentage_change_voter_2=(vote2/totalvotes_sum)
percentage_change_voter_3=(vote3/totalvotes_sum)
percentage_change_voter_4=(vote4/totalvotes_sum)
winner_votes=max(votes)
for j in range(0,3):
    if (winner_votes==votes[j]):
        winner_candidate=candidate_no[j]

print("Election Results")
print("-------------------------")
print("Total Votes:",len(total_votes))
print("-------------------------")
print(f'{candidate_no[2]}: {percentage_change_voter_3:.3%} ({vote3})')
print(f'{candidate_no[3]}: {percentage_change_voter_4:.3%} ({vote4})')
print(f'{candidate_no[1]}: {percentage_change_voter_2:.3%} ({vote2})')
print(f'{candidate_no[0]}: {percentage_change_voter_1:.3%} ({vote1})')
#print(candidate_no[3],":",round(percentage_change_voter_4,5),"(",vote4,")")
#print(candidate_no[1],":",round(percentage_change_voter_2,5),"(",vote2,")")
#print(candidate_no[0],":",round(percentage_change_voter_1,5),"(",vote1,")")
print("-------------------------")
print("Winner:",winner_candidate)
print("-------------------------")

#python main.py > result_bank.txt