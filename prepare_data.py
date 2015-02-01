import pandas as pd
import random 

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
	model=Model()
	model.train(train_data)
	return model

def evaluate_model(model, test_data):



def main():
	test_classes=select_2_classes_to_test()
	train_data=prepare_train_data(test_classes)
	test_data=prepare_test_data(test_classes)
	model=train_model(train_data)
	results=evaluate_model(model, test_data)
	print results

