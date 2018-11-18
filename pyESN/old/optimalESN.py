# coding: utf-8

# learning a [Mackey-Glass](http://www.scholarpedia.org/article/Mackey-Glass_equation) system 
# and finding the optimal hyper-parameter setting. The values of n_reservoir and spectral radius
# used in the file mackey.py are the values that result from this script.

# In[1]:

import time
import numpy as np
import MackeyPrediction as mp
from pyESN import ESN
from tqdm import tqdm

data = np.load('mackey_glass_t17.npy') #  http://minds.jacobs-university.de/mantas/code

min_error = 100
optimum_reservoir_size = 0
optimum_spectral_radius = 0
length = 500
min_spectral_radius = 0
max_spectral_radius = 1.7

results = np.array([0.0, 0.0, 0.0])

for reservoir_size in tqdm(range(1, length)):
	time.sleep(1)
	for spectral_radius in np.linspace(min_spectral_radius, max_spectral_radius, 17):
		results = mp.mackey(reservoir_size, spectral_radius)
		if results[0] < min_error:
			min_error 				= results[0]
			optimum_reservoir_size 	= results[1]
			optimum_spectral_radius = results[2]

print ""
print "The optimum network:"
print "		Reservoir Size: ", optimum_reservoir_size
print "		Spectral Radius: ", optimum_spectral_radius
print "		Error: ", min_error
print ""