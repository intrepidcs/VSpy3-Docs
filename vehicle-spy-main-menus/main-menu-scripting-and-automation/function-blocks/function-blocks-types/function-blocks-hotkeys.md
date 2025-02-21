# Function Blocks Hotkeys

Hotkeys allow you to more conveniently control certain aspects of the operation of function blocks. A hotkey is a shortcut that allows manual functions to be performed at any time without having to directly access the function block interface, such as the buttons on the [Function Block List](../function-block-list.md).

### Operations that Support Hotkeys

Hotkeys can be defined for the following function block operations:

* **Starting/Stopping:** The **Start/Stop Hotkey** option appears on the [Start Tab](../function-block-start-tab.md), which is present for all function block types. Pressing this hotkey will start the script manually if it is not running, or stop the script if it is.
* **Triggering a Capture Block:** Capture type function blocks can have a hotkey assigned to them on the [Stop and Trigger Tab](capture-type-function-block/capture-type-function-block-stop-and-trigger-tab.md), which when pressed, will trigger the collection of data.
* **Storing Data in a Capture Block:** You can also assign a hotkey on the [Storage Tab](capture-type-function-block/capture-type-function-block-storage-tab.md) of a capture block, which will cause the script's buffer to be saved when the hotkey is pressed.

### Hotkey Types

Each place where a hotkey is supported has a drop-down box where you can select from among these options:

* Function keys F6 through F12 (F1 through F5 are [predefined within Vehicle Spy](../../../../shared-features-in-vehicle-spy/shared-features-predefined-function-keys.md)).
* Ctrl+F1 through Ctrl+F12.
* Ctrl+0 through Ctrl+9.
* Joystick 1 through Joystick 9.

Naturally, using joystick buttons requires a joystick to be set up on the computer where Vehicle Spy is running.

### Automatic Hotkey Combination for Starting Function blocks

In addition to allowing a hotkey to be assigned on the **Start Tab** to start or stop a function block, Vehicle Spy also automatically assigns a special key combination for starting blocks. Press **F3** to bring up the [general hotkeys list](../../../../shared-features-in-vehicle-spy/shared-features-predefined-function-keys.md), then press **B** followed by the number next to the function block you want to start.
