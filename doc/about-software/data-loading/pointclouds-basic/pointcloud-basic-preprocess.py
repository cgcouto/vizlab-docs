import numpy as np
import h5py

# load sample dataset (containing two data arrays)
dset = np.load("pointcloud-basic.npz")

# create and allocate HDF5 file
f = h5py.File("pointcloud-basic-converted.h5", 'w')
f.create_dataset("positions", data=dset['pos'])
f.create_dataset("mag_vel", data=dset['mag_vel'])

# save and close
f.close()