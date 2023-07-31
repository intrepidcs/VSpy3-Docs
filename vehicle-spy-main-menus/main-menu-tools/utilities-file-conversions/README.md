# Utilities: File Conversions

Vehicle Spy contains a few tools for converting file formats. To use them, select [Tools](../) -> [Utilities](../tools-utilities/) -> File Conversions then select the conversion you want to perform (Figure 1). A window will pop up asking for a Vehicle Spy buffer file (CSV or VSB). Find the file and click Open. Another window will open for saving the converted file. Give the file a name and click Save.

![Figure 1: Data file converters are found on the Tools : Utilities : File Conversions menu.](../../../.gitbook/assets/dataFileConv.gif)

Note that none of these file converters will change the original file. All of these converters work with a copy of the original file and leave the original untouched.

**Table 1: File Conversion Selections**

<table><thead><tr><th width="150">File Conversion Selection</th><th>Description</th></tr></thead><tbody><tr><td>Text Bus Capture to Signal Log<br>(.csv->.csv)</td><td>Converts a Vehicle Spy message+signal buffer file into a signal-only log file.<br><br>For example, use <a href="../../main-menu-spy-networks/messages-view/messages-view-top-toolbar/save-the-buffer.md">Messages view "Save"</a> (with Save Signals enabled!) to capture a message+signal CSV file. Use this conversion utility on that file and it becomes a CSV log file with only signal values in it, just like <a href="../../main-menu-measurement/logging.md">Logging view</a> would generate.</td></tr><tr><td>Binary Bus Capture to Text Bus Capture<br>(.vsb->.csv)</td><td>Converts a Vehicle Spy binary buffer file into a Vehicle Spy CSV buffer file. (no signals)<br><br>For example, this can convert a VSB file captured from standalone logging into a CSV file for use in other programs.</td></tr><tr><td>Bus Capture to Vector Bus Capture<br>(.csv/.vsb->.asc)</td><td>Converts a Vehicle Spy message buffer file into a Vector? log file.</td></tr><tr><td>Bus Capture to OptoLyzer Bus Capture<br>(.csv/.vsb->.img)</td><td>Converts a Vehicle Spy message buffer file into an OptoLyzer? bus capture (img) file.</td></tr><tr><td>Bus Capture to Vector BLF Bus Capture<br>(.csv/.vsb->.blf)</td><td>Converts a Vehicle Spy message buffer file into a Vector? bus capture (blf) file.</td></tr></tbody></table>

Though it is not on the File Conversions menu, the **CSV2KML** converter takes GPS position information from a Vehicle Spy log file and converts it into a KML file for Google Earth.\
\
The various file converters are necessary because Vehicle Spy can save buffer files in three formats. Each file format has these unique qualities that are useful in different situations:

### Bus Capture CSV buffer file

* always has message data
* can include OR not include decoded signal data as set by the user (database might be required)
* readable by many applications
* larger size than Signal Log or VSB files

### Signal Log CSV file

* never has message data
* always has decoded signal data (database not required)
* readable by many applications
* basic table of signals vs time

### Bus Capture VSB (binary) buffer file

* always has message data
* never has decoded signal data (database required)
* readable only by Vehicle Spy
* smaller size than CSV files
