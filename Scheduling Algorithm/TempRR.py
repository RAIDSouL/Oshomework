bt = [3, 4, 23, 7, 8, 2, 2, 2, 4, 7, 2, 20, 6, 39, 6, 4, 2, 7, 6, 6, 8, 20, 20, 6, 39, 2, 27, 8, 25, 4, 29, 35, 3, 6, 2, 20, 38, 7, 21, 36, 28, 3, 25, 4, 4, 3, 3, 4, 6, 2, 4, 6, 6, 4, 6, 7, 7, 6, 40, 26]
n = 60
quantum = 2; 
rem_bt = [0] * n 
wt = [0] * n 
# Copy the burst time into rt[]  
for i in range(n):  
    rem_bt[i] = bt[i] 
t = 0 # Current time  

# Keep traversing processes in round  
# robin manner until all of them are 
# not done.  
while(1): 
    done = True

    # Traverse all processes one by 
    # one repeatedly  
    for i in range(n): 
            
        # If burst time of a process is greater  
        # than 0 then only need to process further  
        if (rem_bt[i] > 0) : 
            done = False # There is a pending process 
                
            if (rem_bt[i] > quantum) : 
                
                # Increase the value of t i.e. shows  
                # how much time a process has been processed  
                t += quantum  

                # Decrease the burst_time of current  
                # process by quantum  
                rem_bt[i] -= quantum  
                
            # If burst time is smaller than or equal   
            # to quantum. Last cycle for this process  
            else: 
                
                # Increase the value of t i.e. shows  
                # how much time a process has been processed  
                t = t + rem_bt[i]  

                # Waiting time is current time minus  
                # time used by this process  
                wt[i] = t - bt[i]  

                # As the process gets fully executed  
                # make its remaining burst time = 0  
                rem_bt[i] = 0
                
    # If all processes are done  
    if (done == True): 
        break
total_wt = 0
for i in range(n):
    total_wt = total_wt + wt[i]  
print("waiting time = %.5f "% total_wt )
print("\nAverage waiting time = %.5f "%(total_wt /n) )