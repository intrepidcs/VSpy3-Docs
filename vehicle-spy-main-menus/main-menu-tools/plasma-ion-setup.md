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

<table><thead><tr><th width="156.33333333333331">PC Input</th><th>Android Command</th><th>Result in TightVNC Viewer</th></tr></thead><tbody><tr><td>Left mouse button</td><td>Select</td><td>Selects item behind the mouse cursor.</td></tr><tr><td>Right mouse button</td><td>Back</td><td>Returns to previous screen or menu.</td></tr><tr><td>Page Up key</td><td>Menu</td><td>Shows menu options, if available.</td></tr><tr><td>Up / Down arrow keys</td><td>Scroll Up / Down</td><td>Moves cursor up / down within a menu list of items.</td></tr><tr><td>Home key</td><td>Home</td><td>Returns to main home screen from anywhere.</td></tr></tbody></table>

### Changing Wireless Settings on an ICS Logger

Open WiVI 3 by left clicking on its icon in the TightVNC Viewer window. (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)) If the icon is not shown on the home screen, then click on the applications manager (white checkerboard to the right) (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)) and open WiVI 3 from there instead.

The WiVI 3 home screen (Figure 2) has various features not covered in this Vehicle Spy help documentation, but there are two **Settings** (Figure 2:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)) mentioned here that are critical to get an ICS wireless logger up and running.

**Server Connection Host & Port** (Figure 2:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)) settings must be correct for the logger to connect to a Wireless neoVI server and website. Contact the local Wireless neoVI administrator or Intrepid Control Systems to get the correct values.

**Wi-Fi Hotspot** (Figure 2:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)) must be enabled if using Vehicle Spy for Android on a tablet as an added display device.

![Figure 2: Open WiVI 3 / Settings to make changes to wireless logging parameters.](../../.gitbook/assets/PLASIONSetupWNAPKScreenTransitionFromHomeToSettings.gif)

### Status Bar Icons

Near the top of the TightVNC Viewer screen (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)) are icons to indicate new or ongoing events. Table 1 lists many of the icons and what they mean.

**Table 1: ICS Logger Status Bar Icons**

<table><thead><tr><th width="197.57142857142856" align="center">Icon</th><th>Description</th></tr></thead><tbody><tr><td align="center"><img src="../../.gitbook/assets/3GActiveIcon22.gif" alt="" data-size="original"></td><td>3G network - alternating arrows means data is transferring.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/BatteryFullIcon22.gif" alt=""></td><td>Battery status full. (VNET connected to DC power)</td></tr><tr><td align="center"><img src="../../.gitbook/assets/GPSLockedIcon22.gif" alt=""></td><td>GPS enabled and locked in.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/GPSUnlockedIcon22.gif" alt=""></td><td>GPS enabled, but not locked in. (blinking circle means trying to lock in)</td></tr><tr><td align="center"><img src="../../.gitbook/assets/CellSignalStrengthFullIcon22.gif" alt=""></td><td>Cellular signal - full strength.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/CellSignalStrengthPartialIcon22.gif" alt=""></td><td>Cellular signal - some strength.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/CellSignalStrengthNoneIcon22.gif" alt=""></td><td>Cellular signal - no signal.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/SIMCardMissingIcon22.gif" alt=""></td><td>SIM card not detected.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/SoundMutedIcon22.gif" alt=""></td><td>Sound is muted.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/HotSpotIcon22.gif" alt=""></td><td>Tethering or hotspot is active.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/TightVNCConnectedIcon22.gif" alt=""></td><td>TightVNC is connected.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/WFISignalStrengthFullIcon22.gif" alt=""></td><td>WIFI signal - full strength.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/WFISignalStrength2barsIcon22.gif" alt=""></td><td>WIFI signal - some strength.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/WFISignalStrengthNoneIcon22.gif" alt=""></td><td>WIFI signal - no signal.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/WNappIcon22.gif" alt=""></td><td>WirelessNeoVI service is enabled and server is online.</td></tr><tr><td align="center"><img src="../../.gitbook/assets/WNappDisabledIcon22.gif" alt=""></td><td>WirelessNeoVI service is disabled or server is offline.</td></tr></tbody></table>
