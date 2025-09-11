
System quick-start
==================================

Turning on the system
---------------------

This guide assumes that you're starting from a system reboot where you'll need to start up the entire software stack. If not, you might find some or all of these steps have already been completed!

(1) Turn on the system and log in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generally the system should already be on; press either the keyboard or the mouse and after a few moments the screens on the desktop should turn on. If the system isn't already on, look on the server rack for a red button and press it. 

.. image:: /images/systemOnButton.jpg
   :target: /images/systemOnButton.jpg
   :alt: image

Once it's on, you'll need to log into Windows. For the system password, look for it taped to the keyboard!

(2) Turn on the VizLab screens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the control desk you should find a separate CRESTRON touchscreen to control the displays. Touch the screen to wake it, then press 'On'. You may have to wait a few moments as the screens all flash 'PLANAR' as they boot up. Once they've finished booting, they should be displaying content from the system! 

Using the VizLab as a standard Windows machine
----------------------------------------------

Since the VizLab runs Windows, you can use it just like any other Windows system, just with a very large screen attached! Read on to learn how to do that effectively.

Get your content onto the VizLab screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The VizLab desktop is oriented "above" the large screen, so to move content from the desktop screen to the VizLab screen, drag it down to the bottom of the desktop screen and it will appear on the VizLab screen.

Once you've dragged it onto the big display, use the keyboard shortcut ``Windows key + F11`` to make it go full-screen across the entire display.

As for content to show on the screen, you have two choices: remote content via Zoom or local content that's directly on the system.

Running a Zoom meeting and sharing content remotely via screen share
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest approach for getting content onto the screen is by starting a Zoom session on the VizLab machine, then joining from your personal machine and sharing screen. There's a dedicated zoom room for this purpose, the details of which are found in a sticky note on the system desktop.

When you share screen the window on the VizLab screen will change size. As such, to get everything set up properly follow these instructions:

* Get zoom set up
* Share screen from your laptop
* Move the zoom screen on the VizLab machine onto the big screen
* Resize the zoom screen to be large enough on the VizLab screen with ``Windows key + F11`` or by dragging the corner.

Showing local content (presentations, Chrome, etc.) across the screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For sharing local content, you have multiple options: going through a web browser (with or without signing into a account to do so) or by uploading your content to the VizLab's Google Drive folder, which automatically syncs to the system. 

Then like before, drag it onto the main display and use the ``Windows key + F11`` keyboard shortcut to make it full-screen across the display.

Running system-specific software
--------------------------------

The VizLab also has system-specific software that takes full advantage of its capabilities. To get that running, read on!

These steps involve getting a series of different applications running on the system. For convenience, you can find all of the applications you'll need on the desktop (on the leftmost monitor on the desk). 

.. image:: /images/allAppsOnDesktop.PNG
   :target: /images/allAppsOnDesktop.PNG
   :alt: image


(3) Start getReal3D for Unity daemon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We'll start by running the getReal3D daemon, which is the first application in the set from above. Double-click to open it; you should see a window open and then close, as it will minimize itself to run silently in the system tray.

.. image:: /images/daemonOnDesktop.PNG
   :target: /images/daemonOnDesktop.PNG
   :alt: image


Once you see it running in the tray (as shown below, in the bottom left of the leftmost monitor on the desk), you can move on to the next step!


.. image:: /images/daemonInTray.PNG
   :target: /images/daemonInTray.PNG
   :alt: image


(4) Start DTrack3 and connect controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now we need to get the tracking software up and running. To do that, launch the DTrack3 application (the second in our set).

.. image:: /images/DTrackOnDesktop.PNG
   :target: /images/DTrackOnDesktop.PNG
   :alt: image


You'll need to connect to the tracking controller to open the application proper. You should just need to press 'Connect'; if you have problems connecting check out the `troubleshooting guide <TROUBLESHOOTING.md>`_.


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


(5) Start trackd middleware
^^^^^^^^^^^^^^^^^^^^^^^^^^^

DTrack3 does the actual tracking, but to pass this information along with controller button presses, you need to be running trackd as well. Like DTrack3, you can find this on the desktop (the third in our set).

.. image:: /images/trackdOnDesktop.PNG
   :target: /images/trackdOnDesktop.PNG
   :alt: image

It might prompt you to connect the controller, as shown below: to connect it, just press any of the colored buttons on its front and it should pair automatically.


.. image:: /images/trackdWaitingForInput.PNG
   :target: /images/trackdWaitingForInput.PNG
   :alt: image

 If the controller is connected and DTrack3 is running, dtrack should start printing state for both the glasses and the controller. To verify that controller inputs are coming in properly, press a button or move one of the control sticks and you should see that information update in dtrack in real time.

.. image:: /images/trackdReceivedInput.PNG
   :target: /images/trackdReceivedInput.PNG
   :alt: image


(6) Start launcher and run application!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The last step is using the getReal3D for Unity launcher to launch your Unity app of choice! This is the fourth and final relevant application on the desktop:


.. image:: /images/launcherOnDesktop.PNG
   :target: /images/launcherOnDesktop.PNG
   :alt: image


Once it's open, you'll see a list of VizLab applications that you can run. If you want to add a new application, you can press the plus at the bottom left and navigate to the correct .exe file.


.. image:: /images/launcherOverview.PNG
   :target: /images/launcherOverview.PNG
   :alt: image


When you're ready to start an app, just press launch at the bottom right. It will only work if you've followed all the instructions though, so look out for these errors and warnings in the bottom left:


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

Now that you've set up the VizLab, you're ready to run software! Running 'vizlab-core' in the launcher will start up our main visualization package. For a full list of software available to run, `check out the PREBUILTSCENES page. </about-software/PREBUILTSCENES.md>`_

Once you're done with your VizLab software of choice, you can use the launcher to stop it from running and taking up the main display.

.. image:: /images/launcherStopButton.PNG
   :target: /images/launcherStopButton.PNG
   :alt: image
