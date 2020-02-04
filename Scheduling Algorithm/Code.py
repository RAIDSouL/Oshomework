import random
processCount = int(input("Please enter number of process : "))

percentProcessOne = int(input("Please enter percentage of processOne : "))
percentProcessTwo = int(input("Please enter percentage of processTwo : "))
percentProcessThree = int(input("Please enter percentage of processThree : "))

processOneCount = int(processCount*percentProcessOne/100)
processTwoCount = int(processCount*percentProcessTwo/100)
processThreeCount = int(processCount*percentProcessThree/100)

process = []

#ProcessOne
for i in range(processOneCount):
    process.append(random.randrange(2,9,1))
#ProcessTwo
for i in range(processTwoCount):
    process.append(random.randrange(20,31,1))
#ProcessThree
for i in range(processThreeCount):
    process.append(random.randrange(35,41,1))

#shuffle values in process
random.shuffle(process)
print("DataSet :" , *process, sep = " ")

#First Come First Serve
############################################################################################
waitTime = [0]
sumWaitTime = 0
for i in range (0 , len(process)):
    waitTime.append(process[i] + waitTime[i])
    sumWaitTime += waitTime[i]
avgWaitTime = sumWaitTime/len(process) 
print("Sum FCFS: " + str(sumWaitTime))
print("Avg FCFS: " + str(avgWaitTime))
############################################################################################

#Shortest Job First
############################################################################################
#applying bubble sort to sort process according to their burst time
SJFProcess = process
for i in range(0,len(SJFProcess)-1):
    for j in range(0,len(SJFProcess)-i-1):
        if(SJFProcess[j]>SJFProcess[j+1]):
            temp=SJFProcess[j]
            SJFProcess[j]=SJFProcess[j+1]
            SJFProcess[j+1]=temp
# print(*SJFProcess ,sep = ", ")
#simply apply FCFS
waitTime = [0]
sumWaitTime = 0
for i in range (0 , len(process)):
    waitTime.append(process[i] + waitTime[i])
    sumWaitTime += waitTime[i]
avgWaitTime = sumWaitTime/len(process) 
print("Sum SJF: " + str(sumWaitTime))
print("Avg SJF: " + str(avgWaitTime))
############################################################################################

#Round Robin 
############################################################################################
waitTime = [0]
quantum = 5
waitTime = [0] * len(process)
rem_process = [0] * len(process) 
for i in range(len(process)):  
    rem_process[i] = process[i] 
t = 0 
while(1): 
    done = True
    for i in range(len(process)): 
        if (rem_process[i] > 0) :
            done = False
            if (rem_process[i] > quantum) : 
                t += quantum 
                rem_process[i] -= quantum  
            else:
                t = t + rem_process[i]  
                waitTime[i] = t - process[i] 
                rem_process[i] = 0 
    if (done == True): 
        break
sumWaitTime = 0
for i in range(len(process)): 
    sumWaitTime += waitTime[i]
avgWaitTime = sumWaitTime/len(process) 
print("Sum RR: " + str(sumWaitTime))
print("Avg RR: " + str(avgWaitTime))
############################################################################################