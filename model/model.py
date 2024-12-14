import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


#Loading dataset

def load_descriptor(energy_file,descriptor_filee):
    descriptors = np.load(descriptor_file)
    energies = np.load(energy_file)
    n_samples,n_feature = descritors.shape
    return descriptors,energies,n_samples,n_features



def training_set(n_train,descriptors,energies): #n_train is the size of the training set
    idx = np.linspace(0, len(r_numpy) - 1, n_train).astype(int)
    ds_full_train = descriptors[idx]
    energies_full_train = energies[idx]
    return ds_full_train,energies_full_train



