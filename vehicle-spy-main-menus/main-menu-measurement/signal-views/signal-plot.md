# Signal Plot

Use the **Signal Plot** (Figure 1) to plot Vehicle Spy signals in real time.

![Figure 1: Plotting signals with the Signal Plot feature.](../../../.gitbook/assets/spySignalsviewLayout.gif)

### Signal Groups

The Signal Plot feature uses _signal groups_, or collections of signals, to plot. New groups can be created by clicking on the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/add\_signal\_group.gif) button, or removed using the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/delete\_signal\_group.gif) button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)). Signal groups are edited by clicking the **Select Signals** button and using the Expression Builder. To choose a different signal group, select it from the drop-down list to display that group in the plot.

Note that the same signal groups are shared between the Signal Plot and Signal List features in Vehicle Spy.

### Signal Plot Controls

The **Plot Signals** button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)) creates another Signal Plot window. The **Logging** button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)) opens the Logging view; logging status is displayed just below the button, as shown in Figure 1.

The Signal Plot tool bar (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFour.gif)) provides various features for displaying and saving data. Table 1 describes each of the Signal Plot toolbar controls. The data plot is seen in the bottom section of the window (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFive.gif)). The plot axes (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smSix.gif)) can be stretched or zoomed by clicked and dragging them.

**Table 1: Signal Plot Toolbar Controls**

| Signal Plot Tool                                                                         | Description                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigplay.gif) Track           | Enabled by default, so the plot scrolls to show the most recent data; press this to resume scrolling after pressing the Pause button.                                                                                                                                                                                                                        |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigPaws.gif) Pause           | Stops scrolling so the display can be reviewed.                                                                                                                                                                                                                                                                                                              |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigUDLR.gif) Scroll Axes     | When selected, dragging the mouse on an axis will scroll the axis in that direction.                                                                                                                                                                                                                                                                         |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigtimesretch.gif) Zoom Axes | When selected, dragging the mouse on an axis will zoom the axis proportionally.                                                                                                                                                                                                                                                                              |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigzoomout.gif) Zoom Out     | Zooms out from the plot.                                                                                                                                                                                                                                                                                                                                     |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigzoomin.gif) Zoom In       | Zooms in on the plot.                                                                                                                                                                                                                                                                                                                                        |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigselect.gif) Zoom Box      | After clicking this button, left-click and drag a box around an area to zoom in, showing only what was surrounded by the box.                                                                                                                                                                                                                                |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigline.gif) Cursor          | This button enables cursors that can be dragged to make measurements from the plot.                                                                                                                                                                                                                                                                          |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigprop.gif) Properties      | <p>This button brings up a dialog to configure the plot.The maximum number of plot points per signal can be changed here; the default is 10,000.<br><br>Note that setting this value too high will create problems if the computer does not have enough memory. As a point of reference, 50,000 plot points with 6 signals will use about 4.8 MB of RAM.</p> |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigcopy.gif) Copy chart      | Copies a bitmap of the plot to the Windows Clipboard so it can be pasted into another application.                                                                                                                                                                                                                                                           |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigsave.gif) Save Chart      | This allow the chart to be saved as a .BMP, .PNG, .EMF, or .JPG file.                                                                                                                                                                                                                                                                                        |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigprint.gif) Print Chart    | Opens a dialog to let you print the plot.                                                                                                                                                                                                                                                                                                                    |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigvaluexy.gif) Cursor Mode  | This drop-down box allows you to select what type of measurement is made with the cursors on the plot.                                                                                                                                                                                                                                                       |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spysigtimspan.gif) Time Span    | This entry controls the number of seconds of data displayed on the graph.                                                                                                                                                                                                                                                                                    |