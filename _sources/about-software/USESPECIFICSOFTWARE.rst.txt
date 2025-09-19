Running system-specific software
--------------------------------

The VizLab also has system-specific software that takes full advantage of its capabilities. To get that running, read on!

These steps involve getting a series of different applications running on the system. For convenience, you can find all of the applications you'll need on the desktop (on the leftmost monitor on the desk).

.. image:: /images/allAppsOnDesktop.PNG
   :target: /images/allAppsOnDesktop.PNG
   :alt: image


(1) Start getReal3D for Unity daemon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We'll start by running the getReal3D daemon, which is the first application in the set from above. Double-click to open it; you should see a window open and then close, as it will minimize itself to run silently in the system tray.

.. image:: /images/daemonOnDesktop.PNG
   :target: /images/daemonOnDesktop.PNG
   :alt: image


Once you see it running in the tray (as shown below, in the bottom left of the leftmost monitor on the desk), you can move on to the next step!


.. image:: /images/daemonInTray.PNG
   :target: /images/daemonInTray.PNG
   :alt: image


(2) Start DTrack3 and connect controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now we need to get the tracking software up and running. To do that, launch the DTrack3 application (the second in our set).

.. image:: /images/DTrackOnDesktop.PNG
   :target: /images/DTrackOnDesktop.PNG
   :alt: image


You'll need to connect to the tracking controller to open the application proper. You should just need to press 'Connect'; if that button is greyed out :doc:`check out the troubleshooting guide to fix that. </about-hardware/TRACKINGISSUES>`.


.. image:: /images/DTrack3Connect.PNG
   :target: /images/DTrack3Connect.PNG
   :alt: image


If the tracking isn't running (shown by two bodies and the 'Start' button replaced with 'Stop' as in the second image) you might need to press 'Start' at the top of the window so the tracking camera can see within the space.


.. image:: /images/DTrack3NotRunning.PNG
   :target: /images/DTrack3NotRunning.PNG
   :alt: image


.. image:: /images/DTrack3Running.PNG
   :target: /images/DTrack3Running.PNG
   :alt: image


(3) Start trackd middleware
^^^^^^^^^^^^^^^^^^^^^^^^^^^

DTrack3 does the actual tracking, but to pass this information along with controller button presses, you need to be running trackd as well and connect the controller to it. Like DTrack3, you can find this on the desktop (the third in our set).

.. image:: /images/trackdOnDesktop.PNG
   :target: /images/trackdOnDesktop.PNG
   :alt: image

It might prompt you to connect the controller, as shown below: to connect it, just press any of the colored buttons on its front and it should pair automatically.

.. image:: /images/trackdWaitingForInput.PNG
   :target: /images/trackdWaitingForInput.PNG
   :alt: image

If the controller is connected and DTrack3 is running, dtrack should start printing state for both the glasses and the controller. To verify that controller inputs are coming in properly, press and hold one of the buttons and you should see that information update in dtrack in real time.

.. image:: /images/trackdReceivedInput.PNG
   :target: /images/trackdReceivedInput.PNG
   :alt: image

This software can be persnickety sometimes, if you're pressing controller buttons and it's not connecting often times closing and reopening it is what it takes!

(4) Start Unity app launcher and run application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The last step is using the getReal3D for Unity launcher to launch your Unity app of choice! This is the fourth and final relevant application on the desktop:


.. image:: /images/launcherOnDesktop.PNG
   :target: /images/launcherOnDesktop.PNG
   :alt: image


Once it's open, you should see a list of VizLab applications that you can run. If not, check what tab you're on at the top. You should be on the 'Recent Games List' tab, all others are irrelevant.


.. image:: /images/launcherOverview.PNG
   :target: /images/launcherOverview.PNG
   :alt: image

.. image:: /images/launcherTopTabs.PNG
   :target: /images/launcherTopTabs.PNG
   :alt: image


Select an app by clicking on its name in the list. When you're ready to run it, just press launch at the bottom right. It will only work if you've followed all the instructions though, so look out for these errors and warnings in the bottom left:


.. image:: /images/launcherNoDaemon.PNG
   :target: /images/launcherNoDaemon.PNG
   :alt: image


Check that the daemon is running if you're getting this error!


.. image:: /images/launcherNoTrackd.PNG
   :target: /images/launcherNoTrackd.PNG
   :alt: image


Make sure you're running trackd if you see this!


.. image:: /images/launcherReady.PNG
   :target: /images/launcherReady.PNG
   :alt: image


This means you're (probably) all good to go! Note that the launcher doesn't throw an error or warning if DTrack3 isn't running, so if the application starts and the tracking isn't working, start there!

Now that you've set up the VizLab, you're ready to run software! Running 'vizlab-core' in the launcher will start up our main visualization package. For a full list of available software, :doc:`check out the software index. </about-software/SOFTWAREINDEX>`

Once you're done with your VizLab software of choice, you can use the launcher to stop it from running and taking up the main display.

.. image:: /images/launcherStopButton.PNG
   :target: /images/launcherStopButton.PNG
   :alt: image
