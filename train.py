#!/usr/bin/env python
# coding: utf-8



from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


dataset = mnist.load_data('mymnist.npz')
train , test = dataset
X_train , y_train = train
X_test , y_test = test
L=28
W=28
D=L*W
no_of_matrix=512


X_train_1d = X_train.reshape(-1 , D)
X_test_1d = X_test.reshape(-1 , D)
X_train = X_train_1d.astype('float32')
X_test = X_test_1d.astype('float32')
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)


def build_layers(lyr, repeat):
	model = Sequential()
	model.add(Dense(units=no_of_matrix, input_dim=D, activation='relu'))
	p=1
	for i in range(0,lyr):
		p=p*2
		model.add(Dense(units=no_of_matrix//p, activation='relu'))
		if repeat!=0 :
			model.add(Dense(units=no_of_matrix//p, activation='relu'))
			repeat-=1
	model.add(Dense(units=10, activation='softmax'))
	return model
file1=open("/ws/layers.txt","r")
file2=open("/ws/repeats.txt","r")
file3=open("/ws/accuracy.txt","w")
repeat=int(file2.read())
lyr=int(file1.read())

model=build_layers(lyr,repeat)
model.compile(optimizer= Adam(learning_rate=0.0001), loss='categorical_crossentropy', 
             metrics=['accuracy']
             )
h = model.fit(X_train, y_train_cat, epochs=5,verbose=0)

model.save("/ws/MyMNIST.h5")
score = model.evaluate(X_test,y_test_cat,verbose=0)
accuracy = score[1]
file3.write(str(accuracy))
file1.close()
file2.close()
file3.close()





