# Data Analysis

Data Analysis is a powerful tool for graphically displaying and analyzing the data in files collected from vehicle networks. It can be accessed through the Vehicle Spy [Measurement menu](../).\
\
Data can come from a variety of sources, including [buffer files](../../main-menu-spy-networks/messages-view/messages-view-top-toolbar/save-the-buffer.md), [log files](../logging.md), and files obtained from [Capture Type Function Blocks](../../main-menu-scripting-and-automation/function-blocks/function-blocks-types/capture-type-function-block/). These files are all typically found in the current user's Data Directory.

### Data Analysis View and Partitions

An example of the Data Analysis feature in Vehicle Spy can be found in Figure 1, which shows a single plotted signal. The view can be conceptually divided into four areas. On the top is a set of toolbars, and below that are three partitions:

* **Top Left:** Data files and channels are chosen here.
* **Top Right:** Shows plots and values of selected channels.
* **Bottom:** Contains a table listing data points in selected channels.

You can adjust the relative sizes of these partitions by dragging the vertical and horizontal divider bars that separate them, which are shaded in green in Figure 1.

### Data Analysis Toolbars

There are four toolbars, which appear at the top of the Data Analysis display in Figure 1. You may see a different default layout when you first open the feature, and not all toolbars may appear initially; they can be enabled or disabled via the [Show menu](data-analysis-main-menus-and-toolbar.md).\
\
Notice that there are two vertical bars (![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/vertical_bars.gif)) at the left edge of each toolbar. You can click on these bars, then drag and drop the toolbar to a different location.

![Figure 1: Data Analysis view.](../../../.gitbook/assets/data_analysis.gif)

### Data Analysis Areas

Table 1 contains information on the individual areas in the Data Analysis view. Each entry contains a description of the region, a reference to its location in Figure 1, and a clickable link to a page that describes it in detail.

**Table 1: Data Analysis Areas**

| Area                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif) [Main Menus and Toolbar](data-analysis-main-menus-and-toolbar.md)                     | The menus contain most of the options for controlling the Data Analysis feature, such as opening and closing files, showing or hiding areas of the screen, printing, displaying cursor information, and setting plotter labels, configurations, and plotter options. The Main Toolbar buttons are a subset of the controls from the menus. |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif) [Zoom Toolbar](data-analysis-zoom-toolbar.md)                                         | Contains tools for controlling plotter zoom features.                                                                                                                                                                                                                                                                                      |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif) [X-Axis Input Toolbar and Dialog](data-analysis-x-axis-input-toolbar-and-dialog.md) | Provides quick X-axis control of the (S)tarting point and (W)idth for the data (F)ile being plotted.                                                                                                                                                                                                                                       |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFour.gif) [Plotter Setup Toolbar](data-analysis-plotter-setup-toolbar.md)                      | Allows the plotter to be divided into multiple plotter areas, and provides controls for the plot's Y-axis.                                                                                                                                                                                                                                 |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFive.gif) [Tool Dialog](../data-analysis-tool-dialog/)                                         | Allows you to select a data file and channels within that file using checkboxes.The channel selection list includes configurable columns to display various channel statistics. This area also contains a file directory tree.                                                                                                             |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smSix.gif) [Plotter Area](../data-analysis-plotter-area/)                                        | Displays time plot, histogram, or X/Y plots for the selected channels.                                                                                                                                                                                                                                                                     |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smSeven.gif) [Channel Value Pane](../data-analysis-channel-value-pane.md)                        | Displays all available channel statistics for the selected channels.                                                                                                                                                                                                                                                                       |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smEight.gif) [Output Bar](../data-analysis-output-bar.md)                                        | Contains a table showing the entire list of data points for the selected channels.                                                                                                                                                                                                                                                         |
| ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smNine.gif)Status Bar                                                                            | Shows Data Analysis status messages, the current subset file, if any, and the state of the Caps Lock, Num Lock and Scroll Lock keys.                                                                                                                                                                                                       |
