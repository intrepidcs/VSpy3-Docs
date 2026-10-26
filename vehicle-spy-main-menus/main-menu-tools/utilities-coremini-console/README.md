# Utilities: CoreMini Console

The CoreMini Console is a tool for loading CoreMini Scripts into supported hardware. Some applications for CoreMini Scripts could be ECU simulation, Data Logging, Hardware acceleration, and Gateways all ran without a PC.\
\
CoreMini Scripts start as Vehicle Spy 3 files. The CoreMini Console converts and loads the file into the supported hardware. The CoreMini Console is found under Tools -> Utilities -> CoreMini Console (figure 1)

![Figure 1: CoreMini Console can be found in the Utilities menu under Tools](../../../.gitbook/assets/CoreMiniConsoleMenu.gif)

The CoreMini Console itself is shown in figure 2. When this dialog opens, it compiles the Vehicle Spy file. The notes section (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)) reports any errors or warnings when trying to compile the file. Errors and warnings will be noted by a Red dot. Items compiled successfully will have a green dot. The "Send To USB Device" section holds the settings for selecting a neoVI **FIRE**, neoVI RED, ValueCAN 3, or other supported CoreMini Hardware.\
\
The Device drop down (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)) lets you chose the hardware to use while the Storage drop down selects where in the hardware to store the script. The "Run CoreMini After Download" check box (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)) gives the option of running the script once it is downloaded to the hardware. If this is unchecked, the hardware has to be re-powered to run the script. The "Send..." button (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFour.gif)) will send the script to the selected destination.\
\
If the "Run CoreMini After Download" box is checked, the script will start to run. To remove a script from the selected hardware, the "Clear" button (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFive.gif)) is used. The Advanced settings checkbox (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smSix.gif)) reveals a few extra options:

* **Enable RTC Sync** updates the real-time clock in the device when the CoreMini is downloaded. It is on by default.
* **Skip FW Version Check** skips the firmware version check when downloading. It is off by default.
* **Keep & Show** helps you check a setup that uses the [XCP STIM](../../main-menu-scripting-and-automation/function-blocks/function-blocks-types/script-type-function-block-commands/script-type-function-block-command-xcp-stim.md) command. To build a CoreMini, Vehicle Spy generates function blocks that set up the ECU and send its STIM. Check this box, then click **Compile** while Vehicle Spy is offline. If the compile succeeds, those function blocks stay in the setup, set to run on the PC. The CoreMini Console closes, and the Function Blocks view opens to show them. Reload the setup to remove them, and do not save it. Do not send the CoreMini to a device while the setup runs these function blocks on the PC. The box is off by default, and turns itself off once the function blocks are kept.

![Figure 2: CoreMini Console](../../../.gitbook/assets/CoreMiniConsole.gif)

Some hardware devices support loading CoreMini Scripts over CAN, neoVI ECU would be an example. CoreMini scripts are sent to these types of devices using the "neoECU (CAN)" (Figure 3: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smSeven.gif)) option. The supported networks are listed in the "Network" drop down (Figure 3: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smEight.gif))is sent to the device using the "Send..." button.

![Figure 3: CoreMini Console neoECU (CAN) Tab](../../../.gitbook/assets/CoreMiniConsole2.gif)

**IMPORTANT:** It is very important that the firmware in CoreMini capable device match what the software expects. If you try to load a CoreMini to a device with incorrect firmware a warning should be displayed at the bottom (Figure 4). This can be fixed by connecting to neoVI 3G Explorer or in Vehicle Spy 3 if "Enable Auto updates" is turned on under [Tools -> Options](../tools-options/options-spy-networks-tab/). You can also use the Manual Reflash button in neoVI 3G Explorer. It is recommended to leave Enable Auto Update enabled.

![Figure 4: Old firmware warning](../../../.gitbook/assets/CoreMiniLoadOldFirmware.gif)
