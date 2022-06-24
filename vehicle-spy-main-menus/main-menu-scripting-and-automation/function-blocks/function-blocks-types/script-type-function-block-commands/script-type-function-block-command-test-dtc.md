# Script Type Function Block Command: Test DTC

### Command Description

The **Test DTC** command checks the data in a receive message for specified Diagnostic Trouble Codes (DTCs). If DTCs are detected, their data is copied to an [application signal](../../../application-signals/).

This command currently supports only J1939 DTCs.

### Value Field Parameters

A dialog box opens when you double-click in the **Value** field, allowing you to specify the DTCs you want to search for, which message to search, and where to store the results. An example can be seen in Figure 1; a full description of the parameters can be found below.

![Figure 1: Dialog box to set up a Test DTC command.](../../../../../.gitbook/assets/fb\_test\_dtc.gif)

### J1939 DTC Parameters

Enter the following values for a DTC you want to search for:

* **SPN:** The **Suspect Parameter Number** (0 to 524,287).
* **FMI:** The **Failure Mode Indicator** (0 to 31). You can check **Don't Care** next to this value if you want to ignore the FMI.
* **OC:** The **Occurrence Count** (0 to 127). Again there is a **Don't Care** option if this parameter is not relevant.

After making your selection, press the **Add** button next to the SPN box to add the specified DTC to the large box labeled **DTCs to look for in Rx Message**.

If you want to enter more DTCs, repeat the process. You can also use the **Remove** button to delete an entry from the list, or press **Clear All** to delete all entries.

### Send Results to Application Signal

Select the application signal to receive DTC data using the drop-down box here.

### Rx Message

Select the receive message to search for the specified DTCs.
