import numpy as np
import h5py

disk_size_min = 0.02
disk_size_max = 0.7

f = h5py.File("pointcloud-advanced.h5", 'r')

# get number of frames in the data
numFrames = len(f['Outputs'].keys())

# get max number of points in the data 
# (this is contained in the first frame as points exit the sim as it runs)
numPoints = (f['Outputs']['Output1']['nodeData']['positionOrbitalX'].shape)[0]

# prep arrays for each dataset
positions = np.zeros((numFrames, 3, numPoints))
masses = np.zeros((numFrames, numPoints))
radii = np.zeros((numFrames, numPoints))
luminosities = np.zeros((numFrames, numPoints))

# loop through each Output folder and concatenate data fields
for i in range(numFrames):
    groupName = "Output" + str(i+1)
    dset = f['Outputs'][groupName]['nodeData']

    # exact name of luminosity/radii dataset varies for each output
    # so use the prefix to identify the right one
    luminosityName = ""
    radiusName = ""

    for name in dset.keys():
        if name.startswith("diskLuminositiesStellar:DES_g:observed:z"):
            luminosityName = name
        if name.startswith("halfLightRadiusDES_g:observed:z"):
            radiusName = name

    # retrieve x y and z datasets
    x = np.empty((numPoints))
    x[:] = np.nan
    x_data = dset['positionOrbitalX']
    x[0:len(x_data)] = x_data

    y = np.empty((numPoints))
    y[:] = np.nan
    y_data = dset['positionOrbitalY']
    y[0:len(y_data)] = y_data

    z = np.empty((numPoints))
    z[:] = np.nan
    z_data = dset['positionOrbitalZ']
    z[0:len(z_data)] = z_data

    # get the log mass each frame
    mass = np.empty((numPoints))
    mass[:] = np.nan
    mass_data = dset['basicMass']
    mass[0:len(mass_data)] = np.log(mass_data, where=(mass_data!=np.nan and mass_data!=0.0))
    mass[mass==-1*np.inf]=0.0

    # get the log luminosity each frame
    luminosity = np.empty((numPoints))
    luminosity[:] = np.nan
    luminosity_data = dset[luminosityName]
    luminosity[0:len(luminosity_data)] = np.log(luminosity_data, where=(luminosity_data!=np.nan and luminosity_data!=0.0))
    luminosity[luminosity==-1*np.inf]=0.0

    # get the halo radius each frame
    radius = np.empty((numPoints))
    radius[:] = np.nan
    radius_data = dset[radiusName]
    radius[0:len(radius_data)] = np.array(radius_data)*1000

    positions[i] = np.vstack((x,y,z))
    masses[i] = mass
    radii[i] = radius
    luminosities[i] = luminosity

f.close()

# manipulate the radii to fit within ideal min and max disk bounds
radii = (radii / 15)*(disk_size_max-disk_size_min) + disk_size_min

g = h5py.File("pointcloud-advanced-converted.h5", 'w')

g.create_dataset("haloPositions", data=positions)
g.create_dataset("scaledHalfRadii", data=radii, dtype='float32')
g.create_dataset("logLuminosities", data=luminosities, dtype='float32')
g.create_dataset("logBasicMasses", data=masses, dtype='float32')

g.close()