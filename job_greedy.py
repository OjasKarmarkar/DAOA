n = int(input("Enter no of jobs to schedule : "))
jobs = []
max_d = 0
profit=0

for i in range(0,n):
    deadline = int(input(f"Enter deadline of Job J{i+1} : "))
    max_d = max(deadline , max_d)
    profit = int(input(f"Enter profit of Job J{i+1} : "))
    jobs.append({"name" : f"J{i+1}" , "d" : deadline , "pr" : profit})

gantt = ['0' for i in range(0,max_d)]

jobs = sorted(jobs , key = lambda x : x['pr'] , reverse=True)

for job in jobs:
    placed=False

    for j in reversed(range(len(gantt[:job['d']]))):
        if(gantt[j] == '0'):
            gantt[j] = job['name']
            placed = True
            profit+=job['pr']
            break

    if placed == False:
        print(f"Job {job['name']} is not placed")

print("".join(gantt))
print(profit)