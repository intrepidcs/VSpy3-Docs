# Capture Type Function Block: Storage Tab

### Overview

The **Storage Tab** of a [Capture Type Function Block](./) contains settings that dictate when, where and how the data collected by the capture block will be saved. It provides a number of options to allow you to control the timing of data storage, including allowing you to save data based on an expression. You can also select file names and variations, choose a storage format, and other options.

The primary setting here is the storage method drop-down box. Most of the settings are the same regardless of the choice made here, though one does appear only when the **Save when expression is true** method is selected. Figure 1 shows what the **Storage Tab** looks like with this method chosen, so you can see all of the available settings on the tab.

![Figure 1: Capture Block Storage Tab showing all settings.](../../../../../.gitbook/assets/capture\_block\_storage\_tab.gif)

### Storage Method

The drop-down box at the top of the tab controls when data is saved in a capture block. There are three options:

* **Manual Save:** Data is saved only when a request is made. There are three ways this can be done:
  * Clicking the button under the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_list\_save.gif) icon for the block in the [Function Block List](../../function-block-list.md).
  * Using a [Function Block Action](../script-type-function-block-commands/script-type-function-block-command-function-block-action.md) command within a [function block script](../script-type-function-block.md).
  * Assigning a hotkey to save the data (see below) and then pressing the key.
* **Automatically save when complete:** Vehicle Spy saves the data automatically when the function block finishes. This is the default option.
* **Save when expression is true:** Selecting this option enables the **Save Expression** option, described below. There you can enter an expression, and Vehicle Spy will save the captured data as soon as it evaluates as **True**.

Note that some storage methods have interactions with certain [collection methods](capture-type-function-block-stop-and-trigger-tab.md) that may not be obvious at first. For example, if you choose to collect data in a circular buffer, and also select **Automatically save when complete**, there will not actually be any automatic saving of data, because circular buffers have no means by which collection ever completes. Manual intervention is still necessary to stop the collection of data, at which point it will then be automatically saved.

### Storage File

Enter here the name of the file to contain the saved data (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)). This will form the base file name if the **Append Time and Date to file name** and/or **Append App Signal to the file name** options are selected.

Data files are saved to the [data directory](../../../../main-menu-file/data-directory.md) of the currently [logged on](../../../../main-menu-file/the-logon-screen.md) user.

### Storage Options

In the middle of the tab you will find a number of options that provide more control and flexibility over how data is stored (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)). These are mostly independent of each other, and so are enabled or disabled using checkmark boxes:

* **Append Time and Data to file name:** Adds the date and time that the capture is saved to the end of the name entered under **Storage File**. This ensures that captures don't overwrite each other, allowing you to do many captures without worrying about losing data. It is especially useful for function blocks that save multiple buffers in one run.
* **Append App Signal to the file name:** Adds the value of the [application signal](../../../application-signals/) selected in the adjacent drop-down box to the end of the file name. This allows you to dynamically control how captured files are named by adjusting the value of the application signal, for example by using a [function block script](../script-type-function-block.md).
* **ZIP File:** Compresses the file into a .zip file after it is saved, to conserve space. Selecting this option makes saving capture files take a little more time.
* **Save Signals:** Saves signal information along with messages. Saving signals increases the amount of space required by a capture. This option will not appear if **Save As Binary File** is selected.
* **Save As Binary File:** Data is stored as a binary (**.vsb**) file rather than a conventional text (**.csv**) file. Saving binary files is very fast, and they take less room than text files. One key disadvantage is that signals cannot be saved with the messages, and the **Save Signals** option will disappear if **Save As Binary File**is checked. In addition, **.vsb** files can only be opened with Vehicle Spy, where **.csv** files can be read by other applications.

**Note:** The **Save As Binary File** option must be selected to capture Automotive Ethernet messages; saving this data in **.csv** format is not supported.

### Save Expression

This parameter appears only for the **Save when expression is true** storage method (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFour.gif)). Click the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/Functionbutton.gif) button to launch the [Expression Builder](../../../../../shared-features-in-vehicle-spy/shared-features-expression-builder.md), where you can define the condition that must be **True** for data to be saved.

### Hotkey

You may select a [hotkey](../function-blocks-hotkeys.md) (function key, key combination or joystick button) that, when pressed, will cause the captured data to be saved.
