# PLASMA / ION Setup

The ICS loggers neoVI PLASMA and neoVI ION have an Android operating system running an application written by ICS called "WiVI 3" that has settings required for wireless operations.

The buttons and touch screen on neoVI PLASMA can open and change WiVI 3 settings directly, but neoVI ION does not have buttons or a screen; so what to do?

### Vehicle Spy's PLASMA / ION Setup

The answer for neoVI ION is to make WiVI 3 changes using Vehicle Spy's PLASMA / ION Setup opened from the [Tools](./) menu.This feature will also work for neoVI PLASMA, but it is recommended to use the PLASMA buttons and touch screen instead because they are simpler to use.

Use a PC to open the Android home screen on an ICS wireless logger by following these steps:

1. Connect the logger to DC power.
2. Connect the logger PC USB port to the PC.
3. On the PC, open Vehicle Spy, Tools > PLASMA / ION Setup then select the logger.

An Android TightVNC Viewer window should open showing the logger home screen similar to Figure 1.

![Figure 1: Use Vehicle Spy's PLASMA / ION Setup to access the Android home screen on the device.](../../.gitbook/assets/PLASIONSetupTightVNCViewerHomeScreen.gif)

The TightVNC Viewer window has peculiar navigation methods which are listed here for clarity:

**Table 1: TightVNC Viewer Commands**

| PC Input             | Android Command  | Result in TightVNC Viewer                           |
| -------------------- | ---------------- | --------------------------------------------------- |
| Left mouse button    | Select           | Selects item behind the mouse cursor.               |
| Right mouse button   | Back             | Returns to previous screen or menu.                 |
| Page Up key          | Menu             | Shows menu options, if available.                   |
| Up / Down arrow keys | Scroll Up / Down | Moves cursor up / down within a menu list of items. |
| Home key             | Home             | Returns to main home screen from anywhere.          |

### Changing Wireless Settings on an ICS Logger

Open WiVI 3 by left clicking on its icon in the TightVNC Viewer window. (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)) If the icon is not shown on the home screen, then click on the applications manager (white checkerboard to the right) (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)) and open WiVI 3 from there instead.

The WiVI 3 home screen (Figure 2) has various features not covered in this Vehicle Spy help documentation, but there are two **Settings** (Figure 2:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)) mentioned here that are critical to get an ICS wireless logger up and running.

**Server Connection Host & Port** (Figure 2:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)) settings must be correct for the logger to connect to a Wireless neoVI server and website. Contact the local Wireless neoVI administrator or Intrepid Control Systems to get the correct values.

**Wi-Fi Hotspot** (Figure 2:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)) must be enabled if using Vehicle Spy for Android on a tablet as an added display device.

![Figure 2: Open WiVI 3 / Settings to make changes to wireless logging parameters.](../../.gitbook/assets/PLASIONSetupWNAPKScreenTransitionFromHomeToSettings.gif)

### Status Bar Icons

Near the top of the TightVNC Viewer screen (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)) are icons to indicate new or ongoing events. Table 1 lists many of the icons and what they mean.

**Table 1: ICS Logger Status Bar Icons**

|                                       Icon                                       | Description                                                               |
| :------------------------------------------------------------------------------: | ------------------------------------------------------------------------- |
| <img src="../../.gitbook/assets/3GActiveIcon22.gif" alt="" data-size="original"> | 3G network - alternating arrows means data is transferring.               |
|                 ![](../../.gitbook/assets/BatteryFullIcon22.gif)                 | Battery status full. (VNET connected to DC power)                         |
|                  ![](../../.gitbook/assets/GPSLockedIcon22.gif)                  | GPS enabled and locked in.                                                |
|                 ![](../../.gitbook/assets/GPSUnlockedIcon22.gif)                 | GPS enabled, but not locked in. (blinking circle means trying to lock in) |
|            ![](../../.gitbook/assets/CellSignalStrengthFullIcon22.gif)           | Cellular signal - full strength.                                          |
|          ![](../../.gitbook/assets/CellSignalStrengthPartialIcon22.gif)          | Cellular signal - some strength.                                          |
|            ![](../../.gitbook/assets/CellSignalStrengthNoneIcon22.gif)           | Cellular signal - no signal.                                              |
|                ![](../../.gitbook/assets/SIMCardMissingIcon22.gif)               | SIM card not detected.                                                    |
|                  ![](../../.gitbook/assets/SoundMutedIcon22.gif)                 | Sound is muted.                                                           |
|                   ![](../../.gitbook/assets/HotSpotIcon22.gif)                   | Tethering or hotspot is active.                                           |
|              ![](../../.gitbook/assets/TightVNCConnectedIcon22.gif)              | TightVNC is connected.                                                    |
|            ![](../../.gitbook/assets/WFISignalStrengthFullIcon22.gif)            | WIFI signal - full strength.                                              |
|            ![](../../.gitbook/assets/WFISignalStrength2barsIcon22.gif)           | WIFI signal - some strength.                                              |
|            ![](../../.gitbook/assets/WFISignalStrengthNoneIcon22.gif)            | WIFI signal - no signal.                                                  |
|                    ![](../../.gitbook/assets/WNappIcon22.gif)                    | WirelessNeoVI service is enabled and server is online.                    |
|                ![](../../.gitbook/assets/WNappDisabledIcon22.gif)                | WirelessNeoVI service is disabled or server is offline.                   |
