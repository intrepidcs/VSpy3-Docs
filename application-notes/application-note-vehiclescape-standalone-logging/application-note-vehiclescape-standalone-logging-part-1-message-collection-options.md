# Application Note: VehicleScape Standalone Logging - Part 1: Message Collection Options

### 1. Open Vehicle Spy:

The first step, as with any Vehicle Spy project, is to open Vehicle Spy and Log in.

### 2. Open VehicleScape:

VehicleScape DAQ is located under **Measurement**. This Application note skips the platform and Signal selection steps.  For help on this part, see the VehicleScape help here.

### 3. Open Standalone Logging:

From VehicleScape select the **Standalone Logging** tab. This is the view that will be used for the majority of this tutorial.

### Choosing what to log:

"Message Collection Options" gives the option of logging all of the bus traffic (Figure 1: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)) or logging just the messages that you select (Figure 1: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)). If Selected Messages is chosen, make sure to select the signals that need to be logged in the channels tab. Decimation is available when logging selected messages through the Advanced Options button (Figure 1: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)). Decimation will force the logger to only log the last received message at a certain rate.  Enabling decimation will increase the amount of time that you can log, at the expense of data resolution. This is done by sampling the received messages at a set rate rather than logging every message.  The "Force a single decimation rate" uses the rate option to the right, while the "Enable Decimation" option uses the request Priority value to determine when a value is logged.\
\
Note also the text entry box at the top, which is the name of the file that will be saved (Figure 1: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFour.gif)). If you are collecting multiple files, be sure to enable "Append Time and Date to file name".  Otherwise, only your last file will be saved.

![Figure 1: Message Collection Options
](../../.gitbook/assets/VehscapeMessagecollopt.gif)

### Collection Start Options:

There are a number of options for starting data collection (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)).  Your choice in this section will affect some of the following setup menus, so make sure to remember what you chose at this menu. The most simple method is to start Immediately. This option simply starts recording the messages selected from "Figure 1: Message Collection Options" as soon as the logger is plugged in. Selecting "When Expression is True" will allow you to specify a certain expression that must be true before the logging will start. Figure 2 shows that the trigger signal must be greater than 20 before the data collection will commence (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)). With a Pre/Post Trigger you will choose how many messages you would like to collect before and after the trigger event. This is useful for seeing what may have caused the expression to become true. The checkbox labeled, "Always DAQ", will configure the CoreMini in such a way that, it will make diagnostic requests even if the collection has not been triggered. If your trigger is a DAQ item, or if you are using a Pre/Post trigger that is logging diagnostics, you should enable this checkbox (Figure 2: ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)).

![Figure 2: Collection Start Options
](../../.gitbook/assets/Collstartopt.gif)
