# coding: utf-8

# learning a [Mackey-Glass](http://www.scholarpedia.org/article/Mackey-Glass_equation) system

# Imports
import numpy as np
from pyESN import ESN
from matplotlib import pyplot as plt

# Learn the Mackey Glass system
def mackey(reservoir_size, spectral_radius, train_len, future):

	# Load in mackey-glass numpy array
	data = np.load('mackey_glass_t17.npy') #  http://minds.jacobs-university.de/mantas/code
	
	#Initialize ESN
	esn = ESN(n_inputs = 1,
	          n_outputs = 1,
	          n_reservoir = reservoir_size,
	          spectral_radius = spectral_radius,
	          random_state=42)

	# Fit the model
	pred_training = esn.fit(np.ones(train_len),data[:train_len])

	# Predict and find the error
	prediction = esn.predict(np.ones(future))
	error = np.sqrt(np.mean((prediction.flatten() - data[train_len:train_len+future])**2))

	return error, prediction, reservoir_size, spectral_radius, train_len, future