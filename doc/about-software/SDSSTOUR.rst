SDSS tour
---------

.. image:: /images/SDSSTourWideView.jpg
   :target: /images/SDSSTourWideView.jpg
   :alt: image

How to run
^^^^^^^^^^

You can run this software through the Unity app launcher, its title is *VizLabSDSSTour*. Please consult the :doc:`quick-start guide </about-software/QUICKSTART>` if you are having trouble!

How to control
^^^^^^^^^^^^^^

.. image:: /images/controlSchemeSDSSTour.png
   :target: /images/controlSchemeSDSSTour.png
   :alt: image

The key feature of this software is the ability to press the green button on any galaxy in the dataset and have its image and spectrum brought up. This is accomplished through HTTP requests to SDSS's image cutout and spectrum services.

.. image:: /images/SDSSTourSelection.jpg
   :target: /images/SDSSTourSelection.jpg
   :alt: image

The science
^^^^^^^^^^^

The data in this software comes from SDSS DR17, and involved taking ~600k galaxies from SDSS surveys and use their Monte Carlo Physarum Machine (MCPM) model - inspired by how slime molds grow and develop - to estimate the matter density at each target galaxy. Through this system, the researchers were able to estimate the cosmic web throughout their galactic system.

For more information, please consult `the relevant publication <https://arxiv.org/pdf/2301.02719>`_,  `its VAC landing page <https://www.sdss.org/dr18/data_access/value-added-catalogs/?vac_id=99>`_ and `its data model <https://data.sdss.org/datamodel/files/EBOSS_LSS/mcpm/MCPM_VER/slimeMold_galaxy_catalog.html>`_.

Figure 3 in the paper is useful for contrasting how the data looks in a flat 2D context versus on the VizLab!

