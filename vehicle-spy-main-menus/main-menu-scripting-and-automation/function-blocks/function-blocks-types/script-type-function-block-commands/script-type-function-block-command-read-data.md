# Script Type Function Block Command: Read Data

### Command Description

The **Read Data** command allows data from a text file to be loaded into one or more application signals within Vehicle Spy.

### Value Field Parameters

The dialog box launched by double-clicking the **Value** field contains three tabs that let you select the file to read from, decide what data to read, and choose where to store it.

### Filename Tab

You will first see the leftmost tab, named **Filename**, which naturally is used to select the file to read data from (Figure 1).

### Dynamic File Name / Use Text File

You have two options to determine the filename:

* **Dynamic File Name:** Select an [application signal](../../../application-signals/) in the setup that contains the name of the file. This allows you to change the name of the file as needed by using other script commands.
* **Use Text File:** Enter a static filename in the adjacent box. This file must be located in the current user's [data directory](../../../../../basic-operation-of-vehicle-spy/data-directory.md). There is no need to enter a path or an extension (**.txt** is assumed).

Figure 1 shows the filename dynamically selected from the **Read Data Filename** application signal.

### Fast Access for CoreMini

When checked, data will be stored in flash memory, if possible, instead of RAM.

![Figure 1: Read Data command parameters - Filename Tab](../../../../../.gitbook/assets/fb\_read\_data\_1.gif)

### File Line to Read Tab

Here you specify which line of the file you want to read, using an expression built with the [Expression Builder](../../../../../shared-features-in-vehicle-spy/shared-features-expression-builder.md). In Figure 2, we are choosing the line number based on the value of the **Data Line** application signal. You can also enter a static line number within the Expression Builder if you prefer.

![Figure 2: Read Data command parameters - File Line to Read Tab](../../../../../.gitbook/assets/fb\_read\_data\_2.gif)



### Storage Signal Tab

In this tab you select one or more application signals into which to store the data that is read from the file.

If one signal is selected, it will be assigned the full contents of the line of data read. If multiple application signals are specified, then if the line of data read has multiple elements separated by commas, the line will be split using the commas as delimiters, with each element assigned sequentially to the application signals in the list. Figure 3 shows three application signals assigned to a **Read Data**command.

There are several buttons here for managing the application signal list, which are mostly self-explanatory:

* **Add:** Adds the selected application signal to the list.
* **Move Up and Move Down:** Move the selected application signal within the list so you can reorder the signals.
* **Remove:** Deletes the selected application signal from the list.
* **Clear:** Removes all signals from the list.

![Figure 3: Read Data command parameters - Storage Signal Tab](../../../../../.gitbook/assets/fb\_read\_data\_3.gif)
