
Volumes - basic
====================

Get the dataset
^^^^^^^^^^^^^^^

The dataset is based off Gala tutorials for a stellar stream. [1]_

You can access all the materials for this tutorial at the Google Drive link below (carnegiescience.edu account required):

https://drive.google.com/drive/folders/1v5mUzmIXssltbZ5YfNYQL9JK7ly6AFdH?usp=sharing

The starting dataset is called 'pointcloud-basic.npz'. It contains a set of stellar stream positions obtained from a MockStreamGenerator run in Gala, along with the magnitude of the velocity for each star in the stream.

Process such that it is compatible
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can run the Python script pointcloud-basic-preprocess.py to convert the npy file into a valid HDF5 file. All it does it retrieve the datasets in the npy file and store them as HDF5 datasets with appropriate names! 

Load in the software
^^^^^^^^^^^^^^^^^^^^

Once you've got the converted HDF5 file, put it on the VizLab, start up the software and use the 'Load from disk' option on the radial menu to load it in. You'll want to assign each dataset in the menu as shown below: 


.. image:: /images/simplePointCloudMenu.png
   :target: /images/simplePointCloudMenu.png
   :alt: image


Once you hit load, the data will initially look like this under the default 'binary' colormap:


.. image:: /images/simplePointCloudGray.png
   :target: /images/simplePointCloudGray.png
   :alt: image


You can change the colormap to 'hot' to make the difference in the magnitude velocity scalar more obvious:


.. image:: /images/simplePointCloudHot.png
   :target: /images/simplePointCloudHot.png
   :alt: image


References
^^^^^^^^^^

.. [1] https://gala.adrian.pw/en/latest/dynamics/mockstreams.html
