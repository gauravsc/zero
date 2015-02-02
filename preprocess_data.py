import scipy.io 
import pickle
import csv
import numpy as np
#global variables
input_filename="fMRI_data/data-science-P1.mat"
output_filename="fMRI_data/data-science-P1.csv"

def get_data_from_mat_file(filename):
	mat_data=scipy.io.loadmat(filename)
	for i in xrange(360):
		mat_temp=np.asmatrix(mat_data['data'][i][0][0])
		if i==0:
			mat=mat_temp
		else:
			mat=np.vstack((mat,mat_temp))

	return mat

def get_labels_from_mat_file(filename):
	m2=[]
	mat_data=scipy.io.loadmat(filename)
	for i in xrange(360):
		m2.append([mat_data['info'][0][i][2][0]])
	return m2

m1=get_data_from_mat_file(input_filename)
m2=get_labels_from_mat_file(input_filename)
csvfile=open(output_filename, 'w')
header=["c"+str(i) for i in xrange(len(list(np.asarray(m1)[0])))]+["class"]
csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(header)

for i in xrange(360):
	data_to_write=list(np.asarray(m1)[i])+m2[i]
	csvwriter.writerow(data_to_write)

csvfile.close()


