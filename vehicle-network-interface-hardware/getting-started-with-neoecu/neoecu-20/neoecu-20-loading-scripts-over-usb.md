# neoECU 20: Loading Scripts Over USB

Loading scripts into a neoECU device can be done in a few different ways. If your device supports USB, like a neoECU 20, you can simply connect the device directly to the PC and load the script like any CoreMini compatible device, like a neoVI **FIRE**.

### 1. CoreMini Console:

The first step to transferring a CoreMini to a neoECU device is to open the [CoreMini Console](../../../vehicle-spy-main-menus/main-menu-tools/utilities-coremini-console/). [CoreMini Console](../../../vehicle-spy-main-menus/main-menu-tools/utilities-coremini-console/) is found under Tools --> Utilities then CoreMini Console. Here, scripts can be loaded or removed from the hardware.

![Figure 1: Location of the CoreMini Console.](../../../.gitbook/assets/CoreMiniConsoleMenu.gif)

### 2. Using CoreMini Console:

The CoreMini Console contains information regarding the setup that is to be transferred. Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif) shows the output list. This list will notify you of any errors or warnings. If problems exist in the script, a red dot will be next to that item to warn you that something is wrong. The section at the bottom labeled "Device Configuration and Download" lets you chose what type of CoreMini Device you are trying to access. For USB devices select "neoVI (USB)".\
\
Select a device to load the script to (Figure 2:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)). The "Run CoreMini After Download" checkbox (Figure 2:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)) tells the hardware if it should run the script after it is loaded. If this is unchecked, the script will not run until the unit is re-powered. The Send button (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFour.gif)) will send the script to the hardware. Scripts can be removed from the hardware by using the Clear button (Figure 2:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFive.gif)). Once a script has been removed from the hardware, the script must be sent to the hardware again in order to run it.

![Figure 2: The CoreMini Console.](<../../../.gitbook/assets/CoreMiniConsole (1).gif>)
