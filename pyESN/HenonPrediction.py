# coding: utf-8

# learning a Lorenz system

# Imports
import numpy as np
import henon as hn
from pyESN import ESN
from matplotlib import pyplot as plt

# Learn the Lorenz system
def henon(reservoir_size, spectral_radius, train_len, future):

	# Load in mackey-glass numpy array
	data_full = hn.henon()
	data = data_full[0]
	
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