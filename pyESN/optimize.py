# Imports
import sys
import numpy as np
from matplotlib import pyplot as plt

import lorenz as lz
import henon as hn

import MackeyPrediction as mp
import LorenzPrediction as lp
import HenonPrediction as hp

def optimize():

	# Show the plot?
	if len(sys.argv) != 2:
		show_plot = False
	else:
		show_plot = sys.argv[1]

	# ascii art
	print "\n|||//////////////////////////////////////////////////////////////////////////|||"
	print "|||//////////////////////////////////OPTIMIZE////////////////////////////////|||"
	print "|||//////////////////////////////////////////////////////////////////////////|||\n"

	print "Training Length:	Reservoir Size: 	Error:"

	# Variables
	min_error = 1000
	opt_len = 0
	opt_reservoir_size = 0
	train_lens = np.linspace(300, 300, 1)
	reservoir_sizes = np.linspace(10, 501, 50)

	#Iterate through training length and reservoir size
	for i in range(len(train_lens)):
		for j in range(len(reservoir_sizes)):
			future = 200
			spectral_radius = 1.38125
			reservoir_size = int(reservoir_sizes[j])
			train_len = int(train_lens[i])

			# Train the ESN
			#error, prediction, reservoir_size, spectral_radius, train_len, future = mp.mackey(reservoir_size, spectral_radius, train_len, future)
			#error, prediction, reservoir_size, spectral_radius, train_len, future = lp.lorenz(reservoir_size, spectral_radius, train_len, future)
			error, prediction, reservoir_size, spectral_radius, train_len, future = hp.henon(reservoir_size, spectral_radius, train_len, future)


			if(error < min_error):
				min_error = error
				opt_len = train_len
				opt_reservoir_size = reservoir_size

			# Show error
			print train_len, "			", reservoir_size,"			" , error
	# end-for
	print ""

	print "Optimal:"
	print opt_len, "			", opt_reservoir_size,"			" , min_error

	print "\n|||//////////////////////////////////////////////////////////////////////////|||"
	print "|||//////////////////////////////////////////////////////////////////////////|||"
	print "|||//////////////////////////////////////////////////////////////////////////|||\n"

	return opt_len, opt_reservoir_size, min_error

optimize()