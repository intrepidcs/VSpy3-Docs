# Script Type Function Block: Script Toolbar

A toolbar at the top of the setup area for script type function blocks allows you to work with steps as you develop your script program. This region is also where Vehicle Spy warns you in real time of any errors that it may currently see with the script as it has been defined thus far (Figure 1).

![Figure 1: On the left, function block script toolbar controls; on the right, the error status reporting area, currently indicating an issue with an If command.](../../../../.gitbook/assets/script\_toolbar.gif)

### Script Toolbar Controls

Table 1 illustrates and explains the script toolbar controls in Figure 1.

**Table 1: Function Block Script Toolbar Controls**



| Button                                    | Icon                                                                                          | Description                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Add Step After<br>(Insert After)</p>   | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/script\_toolbar\_insert\_after.gif)  | Adds a new step to the script after the one currently selected.                                                                                                                                                                                                                                                      |
| <p>Add Step Before<br>(Insert Before)</p> | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/script\_toolbar\_insert\_before.gif) | Adds a new step to the script before the one currently selected.                                                                                                                                                                                                                                                     |
| Delete Step                               | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/script\_toolbar\_delete.gif)         | <p>Deletes the currently-selected script step.<br><br>You can also delete the currently-selected step using the <strong>Delete</strong>key on your keyboard.</p>                                                                                                                                                     |
| Cut Step                                  | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/script\_toolbar\_cut.gif)            | Copies the currently-selected script step to the Windows Clipboard, and then removes it from the script.                                                                                                                                                                                                             |
| Copy Step                                 | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/script\_toolbar\_copy.gif)           | Copies the currently-selected script step to the Windows Clipboard without removing it.                                                                                                                                                                                                                              |
| Paste Step                                | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/script\_toolbar\_paste.gif)          | Pastes before the currently-selected step a script step previously added to the Windows Clipboard via the **Cut**or **Copy** buttons.                                                                                                                                                                                |
| Undo                                      | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/script\_toolbar\_undo.gif)           | Reverses the last **Delete** operation.                                                                                                                                                                                                                                                                              |
| Tracking                                  | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/script\_toolbar\_tracking.gif)       | <p>When enabled, while a script is running, the script grid will scroll to track the current step being executed. This feature can be useful for monitoring scripts that are too large for all of their steps to be displayed on the screen at once.<br><br>This is a toggle control that is enabled by default.</p> |



Several of these commands are also available in a right-click menu. First select the step you want to work with, then right-click, and you will see entries for the **Copy**, **Paste Before**, **Insert After**, **Insert Before** and **Delete** commands (Figure 2). The other entries on this menu, such as **Run To Step**, **Force** and **Modify Variables**, are used for script tracking and debugging.



![Figure 2: The script toolbar control right-click menu.](../../../../.gitbook/assets/script\_context\_menu.gif)

### Error Status

To the right of the script toolbar is a text display that tells you the current error status of your script. If Vehicle Spy detects no problems in the syntax of your script, this area will say <mark style="color:blue;">**No Errors**</mark> in blue.

If an error is found, it will be shown in red as in the example in Figure 1. Note that error-checking is dynamic and immediate, so transient errors may appear here. For example, the error in Figure 1 will appear if you've just added an **If** step but haven't inserted the matching **End If** step yet. Similarly, an error may briefly display after entering a command step but before selecting its parameters. You only need to make sure that there are no errors showing here when the script is complete and ready to run.
