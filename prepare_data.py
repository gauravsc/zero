import pandas as pd
import random 
import model
data=pd.read_csv('fMRI_data/data-science-P1.csv')


def select_2_classes_to_test():
	global data
	classes=pd.unique(data['class'].values)
	test_classes=random.sample(classes, 2)
	return test_classes

def prepare_train_data(test_classes):
	global data
	idx=data['class'].isin(test_classes)
	train_data=data[~idx]
	return train_data

def prepare_test_data(test_classes):
	global data
	idx=data['class'].isin(test_classes)
	test_data=data[idx]
	return test_data


def train_model(train_data):	
	model_train=model.Model()
	model_train.train(train_data)
	return model_train

def get_accuracy(a1, a2):
	cnt=0
	for i in xrange(len(a1)):
		print a1[i],":", a2[i]
		if a1[i].strip()==a2[i].strip():
			cnt+=1
	return cnt/len(a1)

def evaluate_model(model, test_data):
	true_classes=test_data['class'].values
	X=test_data[[col for col in test_data.columns if col not in ["class"]]].values
	predicted_labels=model.predict(X)
	print "Accuracy: ", get_accuracy(predicted_labels, true_classes)


def main():
	test_classes=select_2_classes_to_test()
	train_data=prepare_train_data(test_classes)
	test_data=prepare_test_data(test_classes)
	model=train_model(train_data)
	evaluate_model(model, test_data)

main()
