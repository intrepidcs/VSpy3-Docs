# Function Block Start Tab

The settings for [Function Blocks](./) are arranged into tabs that appear in the bottom half of the window. Each type of capture block has a different tab configuration, but they all include a **Start Tab**, which determines when the function block starts and contains related settings.

The typical appearance of this area is shown in Figure 1.

![Figure 1: Function Block Start Tab.](../../../.gitbook/assets/function\_block\_start\_tab.gif)

### Start Types

The main drop-down box in the Start Tab selects the **Start Type** for the block; there are four options. Whatever choice is made here will also be shown under the **Start Type** column in the [Function Block List](function-block-list.md).

### Start Immediately

The default option, this causes the block to begin running as soon as Vehicle Spy goes online. If the block is running in a compiled CoreMini, it starts when the device is powered up.

### Manual Start

The function block will not run until it is started, either by the user or under program control. Typical methods for starting a block include:

* Pressing the play button for the block in the [Function Block List](function-block-list.md).
* Using a [Function Block Button](../../main-menu-measurement/graphical-panels/graphical-panels-tools/graphical-panel-controls-function-block-button.md) on a [Graphical Panel](../../main-menu-measurement/graphical-panels/).
* Having a [Function Block Script start](function-blocks-types/script-type-function-block.md) the block using a [Function Block Action](function-blocks-types/script-type-function-block-commands/script-type-function-block-command-function-block-action.md).
* Pressing a defined hotkey (see below).

### Use Start Expression

The function block starts when the specified expression evaluates to **True**. When this option is selected, a **Start Expression** box will appear on the screen, as shown in Figure 1. Press the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/Functionbutton.gif) button to launch the [Expression Editor](../../../shared-features-in-vehicle-spy/shared-features-expression-builder.md) to build the expression.

The expression is evaluated every poll cycle, the rate of which is based on the Vehicle Spy [Core Loop time](../../main-menu-tools/tools-options/options-performance-settings.md) setting.

### Start Immediately Embedded Only

If compiled into a CoreMini, the block runs as soon as its hardware powers up. If run within Vehicle Spy, this is equivalent to manual start mode.

### Start Options

Below the **Start Type** drop-down box are a number of other options that you can use to adjust the behavior of a function block script.

### Start/Stop Hotkey

Click the drop-down box to assign a [hotkey](function-blocks-types/function-blocks-hotkeys.md) to this function block, allowing it to be started or stopped with the keyboard.

Vehicle Spy also has a feature that automatically assigns hotkeys to start function blocks. Press the [predefined function key](../../../shared-features-in-vehicle-spy/shared-features-predefined-function-keys.md) **F3** to bring up the **General Hotkeys** list, then press **B** followed by the number next to the function block you want to start.

### Event Sound

This option appears if you select the **Use Start Expression** start type. Click the **Browse...** button, select an audio (**.wav**) file, and Vehicle Spy will play it when the function block starts.

### Automatically Restart when Complete

When enabled, the function block will restart by itself when it has finished. Note that this is the default for [Script Type Function Blocks](function-blocks-types/script-type-function-block.md).

### Timing Precision

Determines how quickly the function block is polled. The default setting, **Automatic**, is best for most uses, but you can also select **Milliseconds** or **Microseconds** for slower or faster polling, respectively.

### Enable Hardware Acceleration

Turning on [Hardware Acceleration](../../main-menu-tools/tools-utilities/utilities-hardware-acceleration.md) can increase the efficiency of [CoreMini](../../main-menu-tools/utilities-coremini-console/) operation.

### Start on Logger Wake Up / Start on Logger Sleep

Check either or both boxes to control how the function block behaves when it is running in a logger.
