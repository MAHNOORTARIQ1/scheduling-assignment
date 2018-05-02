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


for j in range(count-1):
	for k in range(count-1-j):
		if plist[k]['Arrival Time']>plist[k+1]['Arrival Time']:
			dict1={}
			dict1=plist[k]
			plist[k]=plist[k+1]
			plist[k+1]=dict1

for m in range(count):
	plist[m]['Rbursttime']=plist[m]['Burst Time']


cur=0
quantum=3



finishtime=starttime=plist[0]['Arrival Time']

while 1:
	finish='true'
	for l in range(count):
		if plist[l]['Rbursttime']>0:
			finish='false'
			if plist[l]['Rbursttime']>quantum:
				cur=cur+quantum
				plist[l]['Rbursttime']=plist[l]['Rbursttime']-quantum
			else:
				cur=cur+plist[l]['Rbursttime']
				plist[l]['Waiting Time']=cur-plist[l]['Burst Time']-plist[l]['Arrival Time']
				plist[l]['Turnaround Time']=cur-plist[l]['Arrival Time']
				plist[l]['Rbursttime']=0
	if finish=='true':
		break

avgwaitingtime=0
avgturnaround=0

for g in range(count):
	print plist[g]
	avgwaitingtime=avgwaitingtime+plist[g]['Waiting Time']
	avgturnaround=avgturnaround+plist[g]['Turnaround Time']


print 'Average waiting time: ',avgwaitingtime/count
print 'Average Turnaround time: ',avgturnaround/count


















	

























	
