import scipy.io 
import pickle
import csv

#global variables
filename=""


get_data_from_mat_file(filename):
	mat=scipy.io.loadmat(filename)
	mat=mat['data'][0]




get_labels_from_mat_file(filename)




csvfile=open(filename, 'r')
csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for i in range(mat.shape[0]):
	csvwriter.writerow(mat[i])


csvfile.close()


