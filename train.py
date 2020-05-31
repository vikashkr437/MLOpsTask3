#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


dataset = mnist.load_data('mymnist.npz')
train , test = dataset
X_train , y_train = train
X_test , y_test = test


X_train_1d = X_train.reshape(-1 , 28*28)
X_test_1d = X_test.reshape(-1 , 28*28)
X_train = X_train_1d.astype('float32')
X_test = X_test_1d.astype('float32')
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)


model = Sequential()
model.add(Dense(units=512, input_dim=28*28, activation='relu'))
#model.summary()
model.add(Dense(units=256, activation='relu'))
#model.add(Dense(units=128, activation='relu'))
#model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.compile(optimizer= Adam(learning_rate=0.0001), loss='categorical_crossentropy', 
             metrics=['accuracy']
             )
h = model.fit(X_train, y_train_cat, epochs=5,verbose=0)

model.save("MyMNIST.h5")
score = model.evaluate(X_test,y_test_cat,verbose=0)
accuracy = score[1]
accuracy


# In[ ]:




