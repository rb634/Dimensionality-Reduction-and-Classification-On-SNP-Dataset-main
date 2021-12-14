import math
import sys

datafilename = sys.argv[1]
f=open(datafilename)
data=[]
dataread=f.readline()
while (dataread != ''):
    datasplit=dataread.split()
    tempdata=[]
    for j in range(0, len(datasplit), 1):
        tempdata.append(int(datasplit[j]))
    data.append(tempdata)
    dataread=f.readline()
rows=len(data)
cols =len(data[0])
f.close()

datafilename = sys.argv[2]
f=open(datafilename)
trainlabels= []
dataread=f.readline()
while(dataread != ''):
    datasplit=dataread.split()
    trainlabels.append(int(datasplit[0]))
    dataread=f.readline()
f.close()


datafilename = sys.argv[3]
f=open(datafilename)
testdata=[]

dataread=f.readline()
while (dataread != ''):
    datasplit=dataread.split()
    tempdata=[]
    for j in range(0, len(datasplit), 1):
        tempdata.append(int(datasplit[j]))
    testdata.append(tempdata)
    dataread=f.readline()
f.close()

def fselect(data, trainlabels):
    xchi = []
    for j in range(0, len(data[0]),1):
	    contigency = [[1,1],[1,1],[1,1]]    
	    for i in range(0, len(data),1):
	        if trainlabels[i] == 0:
	            if data[i][j] == 0:
	                contigency[0][0] += 1
	            elif data[i][j] == 1:
	                contigency[1][0] += 1
	            elif data[i][j] == 2:
	                contigency[2][0] += 1
	        elif trainlabels[i] == 1:
	            if data[i][j] == 0:
	                contigency[0][1] += 1
	            elif data[i][j] == 1:
	                contigency[1][1] += 1
	            elif data[i][j] == 2:
	                contigency[2][1] += 1

	    colss = [ sum(x) for x in contigency]
	    rowss = [ sum(x) for x in zip(*contigency) ]
	    total = sum(colss)
	    expected = [[(row*col)/total for row in rowss] for col in colss]
	    chisq = [[((contigency[i][j] - expected[i][j])**2)/expected[i][j] for j in range(0,len(expected[0]),1)] for i in range(0,len(expected),1)]
	    final_chisq = sum([sum(x) for x in zip(*chisq)])
	    xchi.append(final_chisq)
    chi_sort = sorted(range(len(xchi)), key=xchi.__getitem__, reverse=True)
    index = chi_sort[:15]
    return index

def feature_reduce(data, column_no):
	reduce_data = []
	l1 = list(zip(*data))
	for j in column_no:
		reduce_data.append(l1[j])
	reduce_data = list(zip(*reduce_data))
	return reduce_data
	
column_no = fselect(data, trainlabels)
print(column_no)
feature_file=open("output1.txt",mode="w",encoding="utf-8")

for i in range(0, len(column_no),1):
    st=str(column_no[i])
    feature_file.write(st + "\n")

reduce_data=feature_reduce(data, column_no)
reduce_testdata=feature_reduce(testdata, column_no)

from sklearn import svm
classfr = svm.SVC(kernel='rbf', C = 1.0, gamma=0.001)
classfr.fit(reduce_data,trainlabels)
pl=classfr.predict(reduce_testdata)
pf=open("output2.txt",mode="w",encoding="utf-8")

for i in range(0, len(pl),1):
    st=str(i)+" "+str(pl[i])
    pf.write(st + "\n")
