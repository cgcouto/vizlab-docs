
Pre-built scenes
================

Aside from the main VizLab software, we have a few pre-built scenes that have been constructed for scientific outreach. Here you can find important details for running and interacting with the scenes, along with some relevant scientific information.

Stellar streams
---------------


.. image:: /images/subhalosScreenshot.jpg
   :target: /images/subhalosScreenshot.jpg
   :alt: image


How to run
^^^^^^^^^^

First off, you'll want to follow `the quick-start guide <QUICKSTART.md>`_ to prep the various pieces of the VizLab system to run properly. Once you've followed those instructions, launch the *Subhalos_MilkyWay* scene with the runner.


.. image:: /images/subhalosRunner.PNG
   :target: /images/subhalosRunner.PNG
   :alt: image


How to control
^^^^^^^^^^^^^^

Consult the diagram below for some details on how to control the scene:


.. image:: /images/prebuiltScenesControlScheme.png
   :target: /images/prebuiltScenesControlScheme.png
   :alt: image


One extra quirk worth mentioning is that you'll see a wand projected into the simulated space from wherever the tracked controller is in real life. When you move the perspective with the left stick, you move in the direction of the wand. So if you want to go up in the scene, you can tilt the controller up and press forward on the stick. Similarly, you go down by tilting down and pressing forward.

The science
^^^^^^^^^^^

This scene depicts stars in the Milky Way disk along with simulated stellar streams (around the disk in blue) and simulated dark matter (throughout the scene in gray). The blue on the stellar streams directly relates to the velocity kick that each star in the stream is experiencing. The data and visualization was done by Ana Bonaca! 

There are a few smaller details in the scene worth mentioning. You might notice a dot that's larger than the others; it represents the Large Magellanic Cloud.There's also a fun scientific Easter egg in this scene: you can actually find the Sun in the Milky Way disk. Look for a special red dot on the underside of the disk; that's the Sun!

Hubble deep field galaxies
--------------------------


.. image:: /images/galaxiesScreenshot.jpg
   :target: /images/galaxiesScreenshot.jpg
   :alt: image


How to run
^^^^^^^^^^

As with the stellar streams scene, follow `the quick-start guide <QUICKSTART.md>`_ to get everything ready to go. Once you've done that, launch the scene titled *Galaxies_HubbleDeepField*.


.. image:: /images/galaxiesRunner.PNG
   :target: /images/galaxiesRunner.PNG
   :alt: image


How to control
^^^^^^^^^^^^^^

The controls are the same as the stellar streams scene:


.. image:: /images/prebuiltScenesControlScheme.png
   :target: /images/prebuiltScenesControlScheme.png
   :alt: image


Because the simulated space is so large though, you'll probably want to go into the menu and set the translation speed and rotation speed sliders to high values. This will give a much better sense of scale!


.. image:: /images/sceneMenu.jpg
   :target: /images/sceneMenu.jpg
   :alt: image


The science
^^^^^^^^^^^

The galaxies shown in the scene come from the `Hubble Ultra Deep Field <https://esahubble.org/images/heic0611b/>`_ taken in 2006 and depicted below.


.. image:: /images/hubbleUltraDeepField.jpg
   :target: /images/hubbleUltraDeepField.jpg
   :alt: image


Here's a relevant passage quoted from the ESA Hubble site linked above:

..

   "This view of nearly 10,000 galaxies is called the Hubble Ultra Deep Field. The snapshot includes galaxies of various ages, sizes, shapes, and colours. The smallest, reddest galaxies, about 100, may be among the most distant known, existing when the universe was just 800 million years old. The nearest galaxies - the larger, brighter, well-defined spirals and ellipticals - thrived about 1 billion years ago, when the cosmos was 13 billion years old."

   "The image required 800 exposures taken over the course of 400 Hubble orbits around Earth. The total amount of exposure time was 11.3 days, taken between Sept. 24, 2003 and Jan. 16, 2004."


This image was processed using Python (scipy and scikit-image specifically), first by getting a binary mask of the non-black regions and then segmenting and cleaning the resulting galaxies. This resulted in about ~400 galaxy sprites, and out of this group the scene places 1 million galaxies randomly in a sufficiently large box.

There are some limitations of this scene worth addressing. Because the galaxies are placed randomly in a box, (1) the scene is less scientifically accurate and more evocative of deep space and (2) you can hit the 'edge of space', so to speak, where no more galaxies are generated outside of the box. You also might notice some artifacts where two or more galaxies are segmented together as one. Due to the basic image processing workflow described previously, if galaxies are overlapping in the image they get segmented together. Perhaps there are some more advanced image processing techniques that could solve this problem!

N-body simulator game
---------------------


.. image:: /images/galaxiesScreenshot.jpg
   :target: /images/galaxiesScreenshot.jpg
   :alt: image


How to run
^^^^^^^^^^

As with the other scens, follow `the quick-start guide <QUICKSTART.md>`_ first. Once you've done that, launch the scene titled *nbody-stellarstreams*. 

One thing to note is that this scene has audio (music and sound effects) -  

How to control
^^^^^^^^^^^^^^

The controls are the same as the stellar streams scene:


.. image:: /images/prebuiltScenesControlScheme.png
   :target: /images/prebuiltScenesControlScheme.png
   :alt: image


Because the simulated space is so large though, you'll probably want to go into the menu and set the translation speed and rotation speed sliders to high values. This will give a much better sense of scale!


.. image:: /images/sceneMenu.jpg
   :target: /images/sceneMenu.jpg
   :alt: image


The science
^^^^^^^^^^^

The galaxies shown in the scene come from the `Hubble Ultra Deep Field <https://esahubble.org/images/heic0611b/>`_ taken in 2006 and depicted below.


.. image:: /images/hubbleUltraDeepField.jpg
   :target: /images/hubbleUltraDeepField.jpg
   :alt: image


Here's a relevant passage quoted from the ESA Hubble site linked above:

..

   "This view of nearly 10,000 galaxies is called the Hubble Ultra Deep Field. The snapshot includes galaxies of various ages, sizes, shapes, and colours. The smallest, reddest galaxies, about 100, may be among the most distant known, existing when the universe was just 800 million years old. The nearest galaxies - the larger, brighter, well-defined spirals and ellipticals - thrived about 1 billion years ago, when the cosmos was 13 billion years old."

   "The image required 800 exposures taken over the course of 400 Hubble orbits around Earth. The total amount of exposure time was 11.3 days, taken between Sept. 24, 2003 and Jan. 16, 2004."


This image was processed using Python (scipy and scikit-image specifically), first by getting a binary mask of the non-black regions and then segmenting and cleaning the resulting galaxies. This resulted in about ~400 galaxy sprites, and out of this group the scene places 1 million galaxies randomly in a sufficiently large box.

There are some limitations of this scene worth addressing. Because the galaxies are placed randomly in a box, (1) the scene is less scientifically accurate and more evocative of deep space and (2) you can hit the 'edge of space', so to speak, where no more galaxies are generated outside of the box. You also might notice some artifacts where two or more galaxies are segmented together as one. Due to the basic image processing workflow described previously, if galaxies are overlapping in the image they get segmented together. Perhaps there are some more advanced image processing techniques that could solve this problem!
