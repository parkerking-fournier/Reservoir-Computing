# Author: Parker King-Fournier



# Imports
import torch
from echotorch.datasets.MackeyGlassDataset import MackeyGlassDataset
import echotorch.nn as etnn
import echotorch.utils
from torch.autograd import Variable
from torch.utils.data.dataloader import DataLoader
import numpy as np
import mdp
import matplotlib.pyplot as plt

# Dataset params
sample_length = 5000
n_samples = 1
batch_size = 1
spectral_radius = 0.9
leaky_rate = 1.0
input_dim = 1
n_hidden = 100

# Manual seed
mdp.numx.random.seed(1)
np.random.seed(2)
torch.manual_seed(1)

# Mackey glass dataset
mackey_glass_dataset = MackeyGlassDataset(sample_length, n_samples, tau=30)

# Data loader
dataloader = DataLoader(mackey_glass_dataset, batch_size=batch_size, shuffle=False, num_workers=2)

# ESN cell
esn = etnn.esn = etnn.ESNCell(input_dim, n_hidden)

print ""
print "/////////////////////////"
print "////////OUTPUT///////////"
print "/////////////////////////"
print ""

# For each batch
for data in dataloader:

    # Inputs
    inputs      = Variable(data, requires_grad=False)
    outputs     = Variable(data, requires_grad=False)

    print "\nHERE\n data: ", data.shape, "\ninputs: ", inputs.shape , "\noutputs: ", outputs.shape

    # Init hidden
    hidden = esn.init_hidden()

    # Zero grad
    esn.zero_grad()

    # Accumulate xTx and xTy
    esn(inputs, outputs)
# end for
