import numpy as np
import random

class Model(object):
	label_vectors={}
	alpha=0.00002
	W=None 

	def __init__(self):
		#load label vectors
		self.load_label_vectors()
		self.num_iter=40
		
	def load_label_vectors(self):
		fread=open('fMRI_data/wordvectors.txt','r')
		cnt=0
		for line in fread:
			line=line.strip()
			if cnt %2 ==1 and cnt >0:
				self.label_vectors[prev_line]=np.asarray(map(float, line.strip().split()))
				self.label_vectors[prev_line]=self.label_vectors[prev_line]/np.linalg.norm(self.label_vectors[prev_line])
			prev_line=line
			cnt+=1
		# print self.label_vectors.keys()
	def get_loss(self, X, L):
		return np.linalg.norm(X*self.W-L)

	def train(self, train_data):
		labels=train_data['class'].values
		cnt=0
		for label in labels:
			if cnt==0:
				L=np.asmatrix(self.label_vectors[label.strip()], dtype=float)
			else:
				L=np.vstack((L,np.asmatrix(self.label_vectors[label], dtype=float)))
			cnt+=1
		lrow, lcol= L.shape
		cols = [col for col in train_data.columns if col not in ["class"]]
		train_data=train_data[cols]
		X=np.asmatrix(train_data.values)
		xrow, xcol=X.shape
		self.W=np.random.rand(xcol, lcol)		
		for iteration in xrange(self.num_iter):
			if iteration > 0 and iteration % 15 ==0:
				self.alpha=self.alpha/3
			print "iteration: ", iteration
			i,j=random.sample(xrange(xrow), 2)
			gradient=2*np.transpose(X[i])*X[i]*self.W \
			-4*np.transpose(X[j])*X[i]*self.W + 2*np.transpose(X[j])*X[j]*self.W \
			+ 2*np.transpose(X[i])*(L[j]-L[i]) + 2*np.transpose(X[j])*(L[i]-L[j])
			self.W=self.W-self.alpha*gradient
			# print self.W
			if iteration %5 == 0:
				print "loss: ", self.get_loss(X, L)

	def dist(self, v1, v2):
		v=np.asarray(v1)-np.asarray(v2)
		return np.linalg.norm(v)

	def find_nearest_vector(self, lvector):
		min_dist=100000000
		for key, value in self.label_vectors.items():
			distance=self.dist(value,lvector)
			if(distance < min_dist):
				best_label=key
				min_dist=distance
		return best_label

	def predict(self, X):
		predicted_labels=[]
		L_new=X*self.W
		for i in xrange(L_new.shape[0]):
			predicted_labels.append(self.find_nearest_vector(L_new[i]))
		return predicted_labels



