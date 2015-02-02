import pandas as pd
import random 

import fileinput


def select_classes():
	data=pd.read_csv('fMRI_data/data-science-P1.csv')
	classes=pd.unique(data['class'].values)
	return classes

cnt=0
fwrite=open('fMRI_data/wordvectors.txt', 'w')
classes=select_classes()
fread=open('/Users/singhgaurav/Downloads/wordvectors.txt','r')
for line in fread:
	if cnt%10000 == 0:
		print cnt
	line=line.strip()
	if cnt>0 and prev_line in classes and cnt %2 !=0:
		fwrite.write(prev_line+'\n')
		fwrite.write(line+'\n')
	# elif cnt >0 and random.random()<0.03 and cnt%2 !=0:
	# 	fwrite.write(prev_line+'\n')
	# 	fwrite.write(line+'\n')
	prev_line=line

	cnt+=1

fread.close()
fwrite.close()