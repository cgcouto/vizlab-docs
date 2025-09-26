User guide
==========

Goals and guiding philosophies
------------------------------

The goal for this project is to build a platform for scientific research and outreach within astrophysics where different sources of data can be mixed together. To accomplish this, we need to support a wide variety of relevant data types and formats. Currently, we support density datacubes (relevant for hydro sims and radio data cubes), 3d scatterplots (relevant for stellar streams), CAD models (relevant for scientific instruments), 360° images (relevant for outreach) and spectral datacubes (relevant for MaNGA/LVM data among other sources). We also need proper tools for visualizing and analyzing the data, along with an intuitive and accessible UI to string everything together. Consider this page a snapshot of current progress, as development is ongoing!

First steps
-----------

Starting the software
^^^^^^^^^^^^^^^^^^^^^

On the VizLab, `the quick-start guide <QUICKSTART.md>`_ is what you need to get up and running!

Control scheme
^^^^^^^^^^^^^^

Please consult the diagram below for the current control scheme on the VizLab. 


.. image:: /images/controlScheme.png
   :target: /images/controlScheme.png
   :alt: image


UI overview
^^^^^^^^^^^

The UI is designed to take use of specialty features of the VizLab, more important of which being the tracked gamepad. Most key settings are on a radial menu which you can bring up by holding the blue button.


.. image:: /images/radialMenuOpen.png
   :target: /images/radialMenuOpen.png
   :alt: image


While holding the button, you can move the tracked controller to align the blue simulated wand with a wedge. Once a wedge is selected, releasing the blue button will bring up the menu.


.. image:: /images/radialMenuSelect.png
   :target: /images/radialMenuSelect.png
   :alt: image


Aside from the radial menu, you can interact with all menu elements using the green button on the controller. 

Data overview
-------------

There are currently five supported visualization object types supported in the software. The table below summarizes the key information for mapping a data source to one of the visualization objects. Each object type is discussed in more detail farther down.

.. list-table::
   :header-rows: 1

   * - Object type
     - Supported formats
     - Supported datatypes
   * - Density datacubes (x,y,z)
     - .hdf5 nd-arrays and .fits images
     - All numerical formats (int, float, etc.)
   * - Point clouds
     - .hdf5 nd-arrays and .fits images
     - All numerical formats (int, float, etc.)
   * - CAD models
     - .stl and .stp/.step
     - N/A
   * - 360° images
     - .jpg and .png
     - N/A
   * - Spectral datacubes (x,y,wavelength)
     - .hdf5 nd-arrays and .fits images
     - All numerical formats (int, float, etc.)


Density datacubes
^^^^^^^^^^^^^^^^^


.. image:: /images/volumeExample.png
   :target: /images/volumeExample.png
   :alt: image


.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Supported dimensionality
   * - ignore
     - System will ignore this data source.
     - Any
   * - density
     - 3D array of density values.
     - 3D


Point clouds
^^^^^^^^^^^^


.. image:: /images/pointCloudsExample.png
   :target: /images/pointCloudsExample.png
   :alt: image


.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Supported dimensionality
   * - ignore
     - System will ignore this data source.
     - Any
   * - positions
     - Either a static or animated set of 3D positions.
     - 2D-3D
   * - scalar
     - Either a static or animated set of relevant values for each position.
     - 1D-2D
   * - scale
     - Disk size for each position
     - 1D-2D
   * - color
     - RGB color data for each position.
     - 2D-3D


CAD models
^^^^^^^^^^


.. image:: /images/CADModelExample.png
   :target: /images/CADModelExample.png
   :alt: image


No data field specification needed - just provide the CAD file!

360° images
^^^^^^^^^^^


.. image:: /images/photosphereExample.png
   :target: /images/photosphereExample.png
   :alt: image


No data field specification needed - just provide the image file!

Spectral datacubes
^^^^^^^^^^^^^^^^^^


.. image:: /images/spectralExample.png
   :target: /images/spectralExample.png
   :alt: image


.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Supported dimensionality
   * - ignore
     - System will ignore this data source.
     - Any
   * - spectral
     - 3D array of spectral values.
     - 3D


Importing your data
-------------------

In-editor
^^^^^^^^^

If you want to add visualization objects to the Unity scene before building and running the VizLab software, you can currently do that for density datacubes. Look for Volume Rendering -> Load dataset -> Load HDF5 dataset in the toolbar of the Unity editor as shown below.


.. image:: /images/loadVolumeInEditor.png
   :target: /images/loadVolumeInEditor.png
   :alt: image


This will bring up a menu that is similar, if more limited, compared to that found at runtime.


.. image:: /images/loadVolumeInEditorMenu.png
   :target: /images/loadVolumeInEditorMenu.png
   :alt: image


In-editor import for other object types is coming soon.

In-system
^^^^^^^^^

To load an object in on the fly, use the radial menu and choose the 'Load file' option. This will bring up a standard-looking file browser. Select the relevant data file to proceed.


.. image:: /images/fileBrowser.png
   :target: /images/fileBrowser.png
   :alt: image


Once you select the file and hit 'Load' in the botton right, the file browser will go away. For certain object types (CAD models) the object will immediately start loading, but for others a new menu will pop up. This is necessary for parsing the input file to pull out relevant data fields. The menu won't let you load the object unless all necessary pieces are assigned.


.. image:: /images/loadFromDiskMenu.png
   :target: /images/loadFromDiskMenu.png
   :alt: image


Consult the data overview section for details on how to assign in your data fields.

Making adjustments
------------------

The object manager (accessible from the radial menu) lets you control all global options for loaded visualization objects. At first glance, you'll see some selection controls on the far left along with the object's name and an icon for its object type.


.. image:: /images/globalOptions.png
   :target: /images/globalOptions.png
   :alt: image


Highlighting the object panel reveals more options to choose from:


.. image:: /images/globalOptionsHighlight.png
   :target: /images/globalOptionsHighlight.png
   :alt: image


The first two options are pretty self-explanatory. The eye icon lets you toggle the object's visibility, while the trash icon lets you delete the object from the scene permanently. The other three are more robust, and will be explained below in separate sections:

Adjusting color
^^^^^^^^^^^^^^^

The paint bucket icon will bring up a separate menu for adjusting object color. Depending on the object, you have three possible options for coloring: by scalar, from disk, and uniform. With the scalar option, you use a provided scalar/density field along with some set colormap. With from disk, some form of saved per-point or per-piece colormap is loaded and used. And as for uniform color, you can use a GUI color picker to choose an RGB value that gets set uniformly across the entire object.

Consult the table below for the coloring options supported by each visualization object:

.. list-table::
   :header-rows: 1

   * - Object type
     - Supported coloring options
   * - Density datacubes (x,y,z)
     - by scalar
   * - Point clouds
     - by scalar, from disk, uniform
   * - CAD models
     - from disk, uniform
   * - Spectral datacubes (x,y,wavelength)
     - by scalar


When coloring by scalar, you are able to set a base Matplotlib colormap with the colormap dropdown. You can also edit the values in more detail, with a control point slider for editing RGB values and an upper canvas for setting the alpha/transparency across the color gradient.


.. image:: /images/scalarValueColor.png
   :target: /images/scalarValueColor.png
   :alt: image


When coloring from disk, you set an already-loaded data field to be the colormap and you are good to go!


.. image:: /images/fromDiskColor.png
   :target: /images/fromDiskColor.png
   :alt: image


When coloring uniformly, just use the color picker to set the desired color. The color swatch will show you the currently selected color without having to open the color picker.


.. image:: /images/uniformColor.png
   :target: /images/uniformColor.png
   :alt: image


Adjusting data
^^^^^^^^^^^^^^

Each visualization object also has a data menu that you can access with the icon that looks like a set of files. Here you can change which data fields the object is currently visualizing. The 'Add New Data' button at the bottom lets you add any number of new data sources to toggle between, so long as they follow the data compatibility rules outlined above. 


.. image:: /images/dataMenu.png
   :target: /images/dataMenu.png
   :alt: image


Adjusting scale
^^^^^^^^^^^^^^^


.. image:: /images/scaleMenu.png
   :target: /images/scaleMenu.png
   :alt: image


Finally, the stretched box icon brings up the scale menu. This lets you adjust the 3D size of the visualization object that was set on import. You can use the sliders to scale all dimensions dependently or independently of each other.

(if animated) Adjusting animation playback
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For animated visualization objects (just point clouds for now) there are additional global options for controlling their playback. It consists of a slider that tracks playback progress, a pause/play button, and additional settings for controlling the animation's frame rate and interpolation.

Object grouping
^^^^^^^^^^^^^^^

One more key feature of the global options menu is object grouping. You can use the grab regions and the toggles on the left of each object panel to group objects together. With these groups, you can then apply certain operations on all the objects together, including cross-sections and animation playback. 

Data analysis
-------------

Here are some brief summaries of the data analysis tools currently available in the VizLab.

Cross-sections
^^^^^^^^^^^^^^


.. image:: /images/crossSectionsExample.png
   :target: /images/crossSectionsExample.png
   :alt: image


Accessible from the global options menu, you are able to create cross-sections objects that present a desired subset of the visualization object(s) they are assigned to. From the global options menu you can choose which of the shapes to spawn (plane, box, or sphere) as well as adjusting their size and axis lock. 

Data querying
^^^^^^^^^^^^^

Also on the global options menu you can find a menu that lets you do SQL-like querying of a visualization object. For example, for a point cloud dataset you are able to look at any loaded data fields to only show points that are above some mass cutoff, below some halo radius, etc!

Emissions
^^^^^^^^^


.. image:: /images/spectralExample.png
   :target: /images/spectralExample.png
   :alt: image


You can use this menu to step through the wavelength slices of a spectral datacube and move the control point to adjust the flux vs. wavelength plot on the right. This graph is interactable, with manual zooming functionality. You can also use the buttons at the bottom of the graph to reset and zoom and control which emission lines are visible. 

Future goals
------------

While development is ongoing, here are some potential future goals for this project:


* Support stronger links to common astronomical databases (including the means the browse and download data in-software), such as ESA's Gaia 
* Build out networking to allow for multiple instances of the software to collaborate in a shared data space
* Expand info-sharing and data labelling systems, allowing for further structuring of visualizations into guided lessons for educational purposes
* Add additional visualization types (ex. vector fields, contour plots, etc.)
* Experiment with new control schemes for the VizLab, including VR inputs (ex. HTC Vive wands) and hand tracking
