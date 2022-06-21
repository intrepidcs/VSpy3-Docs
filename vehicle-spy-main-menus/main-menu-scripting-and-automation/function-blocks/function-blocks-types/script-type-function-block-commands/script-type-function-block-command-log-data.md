# Script Type Function Block Command: Log Data

### Command Description

This command allows data to be logged to a file or device from within a function block script.

### Value Field Parameters

Double-click in the **Value** field to launch the dialog box where data logging settings can be entered (Figure 1).

![Figure 1: Parameter setup for the Load Message Datacommand.](../../../../../.gitbook/assets/fb\_log\_data.gif)

### Insert Date/Time at start of line

When checked, prepends the logged data with a timestamp.

### Text To Log

The text to be logged, which is specified as an expression using the Expression Builder. Examples include a static text string entered as an expression (with **Evaluate as text** checked in the Expression Builder) or a string from a signal.

### Log Type

The type of log to create:

* **Text File:** A plain text file.
* **HTML File:** A file encoded using standard HTML.
* **neoECU RS232 Port**
* **neoECU LCD**
* **neoECU Network**
* **Host PC**
* **neoVI MOTE Screen**

### Use File Name / Dynamic File name

Choose one of these radio buttons to determine where the file's name comes from:

* **Use File Name:** Enter a static filename in the adjacent box.
* **Dynamic File Name:** Select an application signal in the setup that contains the name of the file. This allows you to change the name of the file on the fly by using Set Value or other commands to adjust the name stored in that application signal.

### Overwrite File if it exists

When selected, existing files are overwritten rather than creating new ones, to prevent filling the data directory with many log files.

### Make logged data persistent

When selected, written data persists in storage.
