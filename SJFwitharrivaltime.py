print ('Enter the processes data')
check='yes'
plist=[0]*10
count=0

while check=='yes':
	plist[count]=dict={}
	processname=raw_input('Enter process name: ')
	dict['process name']=processname
	arrivaltime=input('Enter arrival time: ')
	dict['Arrival Time']=arrivaltime
	bursttime=input('Enter burst time: ')
	dict['Burst Time']=bursttime
	check=raw_input('Do you want to enter more processes..Enter yes or no: ')
	count=count+1

curtime=0
for j in range(count-1):
	for k in range(count-1-j):
		if plist[k]['Burst Time']>plist[k+1]['Burst Time'] and plist[k]['Arrival Time']>curtime:
			dict1={}
			dict1=plist[k]
			plist[k]=plist[k+1]
			plist[k+1]=dict1
	curtime=curtime+plist[k]['Burst Time']


finishtime=starttime=plist[0]['Arrival Time']



for i in range(count):	
	waitingtime=0
	turnaround=0

	if finishtime<plist[i]['Arrival Time']:
		temp=plist[i]['Arrival Time']-finishtime
		finishtime=finishtime+temp
		starttime=plist[i]['Arrival Time']

	finishtime=finishtime+plist[i]['Burst Time']
	waitingtime=starttime-plist[i]['Arrival Time']
	plist[i]['Waiting Time']=waitingtime
	turnaround=finishtime-plist[i]['Arrival Time']
	plist[i]['Turnaround Time']=turnaround
	print ('Start Time Process Name Finishtime')
	print starttime,'       ',plist[i]['process name'],'       ',finishtime
	print plist[i]['process name'],' waiting time is: ',plist[i]['Waiting Time']
	print plist[i]['process name'],' turnaround time is: ',plist[i]['Turnaround Time']
	starttime=starttime+plist[i]['Burst Time']

avgwaiting=0;
avgturnaround=0;

for m in range(count):
	avgwaiting=avgwaiting+plist[m]['Waiting Time']
	avgturnaround=avgturnaround+plist[m]['Turnaround Time']

print 'Average Waiting time is: ',avgwaiting/count
print 'Average Turnaround time is: ',avgturnaround/count























	
