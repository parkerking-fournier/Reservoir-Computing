# Imports
import sys
import numpy as np
from matplotlib import pyplot as plt

import lorenz as lz
import henon as hn

import MackeyPrediction as mp
import LorenzPrediction as lp
import HenonPrediction as hp



def main():

	# Show the plot?
	if len(sys.argv) != 2:
		show_plot = False
	else:
		show_plot = sys.argv[1]

	# Variables
	reservoir_size_1 = 10
	reservoir_size_2 = 20
	reservoir_size_3 = 200
	reservoir_size_4 = 290

	spectral_radius = 1.38125
	train_len = 300
	future = 200
	reservoir_size_array = [10, 20, 200, 490]

	ensemble_size = 4

	error_array = [0,0,0,0]
	prediction_array = [0,0,0,0]
	average_array = [0,0,0]


	# Train the 1st ESN
	#error_1, prediction_1, reservoir_size_1, spectral_radius_1, train_len, future = mp.mackey(reservoir_size_1, spectral_radius, train_len, future, show_plot)
	#error_1, prediction_1, reservoir_size_1, spectral_radius_1, train_len, future = lp.lorenz(reservoir_size_1, spectral_radius, train_len, future, show_plot)
	#error_1, prediction_1, reservoir_size_1, spectral_radius, train_len, future = hp.henon(reservoir_size_1, spectral_radius, train_len, future)

	# Train the 2nd ESN
	#error_2, prediction_2, reservoir_size_2, spectral_radius_2, train_len, future = mp.mackey(reservoir_size_2, spectral_radius, train_len, future, show_plot)
	#error_2, prediction_2, reservoir_size_2, spectral_radius_2, train_len, future = lp.lorenz(reservoir_size_2, spectral_radius, train_len, future, show_plot)
	#error_2, prediction_2, reservoir_size_2, spectral_radius, train_len, future = hp.henon(reservoir_size_2, spectral_radius, train_len, future)

	# Train the 3rd ESN
	#error_3, prediction_3, reservoir_size_3, spectral_radius_3, train_len, future = mp.mackey(reservoir_size_3, spectral_radius, train_len, future, show_plot)
	#error_3, prediction_3, reservoir_size_3, spectral_radius_3, train_len, future = lp.lorenz(reservoir_size_3, spectral_radius, train_len, future, show_plot)
	#error_3, prediction_3, reservoir_size_3, spectral_radius, train_len, future = hp.henon(reservoir_size_3, spectral_radius, train_len, future)

	# Train the 4th ESN
	#error_4, prediction_4, reservoir_size_4, spectral_radius_4, train_len, future = mp.mackey(reservoir_size_4, spectral_radius, train_len, future, show_plot)
	#error_4, prediction_4, reservoir_size_4, spectral_radius_4, train_len, future = lp.lorenz(reservoir_size_4, spectral_radius, train_len, future, show_plot)
	#error_4, prediction_4, reservoir_size_4, spectral_radius, train_len, future = hp.henon(reservoir_size_4, spectral_radius, train_len, future)

	# Train the 5th ESN
	#error_5, prediction_5, reservoir_size_5, spectral_radius_5, train_len, future = mp.mackey(reservoir_size_5, spectral_radius, train_len, future, show_plot)
	#error_5, prediction_5, reservoir_size_5, spectral_radius_5, train_len, future = lp.lorenz(reservoir_size_5, spectral_radius, train_len, future, show_plot)
	#error_5, prediction_5, reservoir_size_5, spectral_radius, train_len, future = hp.henon(reservoir_size_5, spectral_radius, train_len, future)

	# Train the 5th ESN
	#error_5, prediction_5, reservoir_size_5, spectral_radius_5, train_len, future = mp.mackey(reservoir_size_5, spectral_radius, train_len, future, show_plot)
	#error_5, prediction_5, reservoir_size_5, spectral_radius_5, train_len, future = lp.lorenz(reservoir_size_5, spectral_radius, train_len, future, show_plot)
	#error_5, prediction_5, reservoir_size_5, spectral_radius, train_len, future = hp.henon(reservoir_size_5, spectral_radius, train_len, future)



	data_full = hn.henon()
	data = data_full[0]

	#error_array[0], prediction_array[0], reservoir_size_array[0], spectral_radius_0, train_len, future = hp.henon(reservoir_size_array[0], spectral_radius, train_len, future, show_plot)


	for i in range(0, ensemble_size):
		error_array[0], prediction_array[0], reservoir_size_array[i], spectral_radius, train_len, future = hp.henon(reservoir_size_array[i], spectral_radius, train_len, future)


	#for i in range(0, (ensemble_size-1)):
	#	average_array[i] = np.append(average_array[i], prediction_array[i+1], axis=1)
	#	print average_array[i].shape
	
	#	average_array[i] = np.average(average_array[i], axis=1)

	#average_1 = np.append(prediction_1, prediction_2, axis=1)
	#average_2 = np.append(average_1, prediction_2, axis=1)
	#average_3 = np.append(average_2, prediction_3, axis=1)
	#average_4 = np.append(average_3, prediction_4, axis=1)

	#average_1 = np.average(average_1, axis=1)
	#average_2 = np.average(average_2, axis=1)
	#average_3 = np.average(average_3, axis=1)
	#average_4 = np.average(average_4, axis=1)

	if show_plot:
		plt.figure(figsize=(20,3))

		plt.plot(range(train_len,train_len+future),prediction_array[0],'k', linewidth=0.1,  label="ESN_1")
		plt.plot(range(train_len,train_len+future),prediction_array[1],'k', linewidth=0.2,  label="ESN_2")
		plt.plot(range(train_len,train_len+future),prediction_array[2],'k', linewidth=0.3,  label="ESN_3")
		plt.plot(range(train_len,train_len+future),prediction_array[3],'k', linewidth=0.4,  label="ESN_3")

		plt.plot(range(train_len,train_len+future),data[train_len:train_len+future],'r', linewidth=0.4, label="Target")

		lo,hi = plt.ylim()
		plt.plot([train_len,train_len],[lo+np.spacing(1),hi-np.spacing(1)],'k:')
		plt.legend(loc=(0.61,1.1),fontsize='x-small')
		plt.show();


main()