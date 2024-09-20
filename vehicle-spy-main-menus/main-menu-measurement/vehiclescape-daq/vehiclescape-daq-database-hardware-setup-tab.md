# VehicleScape DAQ: Database/Hardware Setup Tab

The [VehicleScape DAQ](./) Database/Hardware Tab provides controls to manage hardware settings, select platform databases, and pull data from logger SD cards. These functions can also be accessed from other locations within Vehicle Spy, but this tab puts them all in one convenient place.

The layout of the Database/Hardware Tab can be seen in Figure 1.

![Figure 1: The VehicleScape DAQ Database/Hardware Setup Tab.](../../../.gitbook/assets/spyvscapedaqdatabase.gif)

### DAQ Name

Near the top of this tab you will find the **DAQ Name** field, where you can enter a custom name for the set of VehicleScape DAQ parameters you are defining (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)). This allows you to easily reference the DAQ setup in other places, such as the [Expression Builder](../../../shared-features-in-vehicle-spy/shared-features-expression-builder.md). It also is the means by which you can switch among multiple VehicleScape setups using the drop-down list at the top right of the window (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)). Note that this is also where the Auto Start PC DAQ option is. With the checkbox checked, the VehicleScapeDAQ will start when VSpy goes online (With Transmit, Monitor, or Simulation). If other diagnostics are required, formple, reading Diagnostic Trouble Code (DTCs) it is suggested this box be unchecked. This box should be unchecked if the Function Blocks are to be used to control the DAQ.

### Hardware Setup

The **Edit hardware and network settings** button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)) opens [Hardware Setup](../../main-menu-spy-networks/networks/setup-a-network.md) view to allow you to configure your hardware. Here you can set baud rates, enable networks, and more.

### Platform Setup

Most of this area consists of various options for defining platforms and databases used within VehicleScape DAQ. Any changes made here directly change which signals are available on the Channels tab. The Platform Setup area is broken up into four parts.

### Current Platform

VehicleScape DAQ is very database-dependent, so selecting the correct platform is important. If the database is incorrect or does not exist yet, this section will let you correct it. To change the platforms in the list, click the **Setup Platforms** button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFour.gif)) and use the dialog options.

### Network Databases

This section permits setup of [network databases](../../main-menu-setup/network-databases.md), which are those configured for normal traffic. Click the **Load DBC or VSDB files** button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFive.gif)) to open the [Network Databases](../../main-menu-setup/network-databases.md) view.

### Diagnostic Databases

The diagnostic files for this platform are listed here. Click the **Load ODX, MDX/GDX, or A2L files** button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smSix.gif)) to open [ECUs View](../../main-menu-setup/ecus-view/), where new diagnostic database files can be loaded.

### MEP Databases

Configured A2L files for XCP or CCP are listed here. If any files are missing or require updating, click the **Load A2L files for CCP/XCP** button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smSeven.gif)) to open [MEP Setup](../mep-xcp-ccp-memory-edit-protocol/) view to fix them.

### Extract and Export

The **Extract and Export** button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smEight.gif)) opens the [Extract Export](../../main-menu-tools/utilities-extract-export/) view. Use this to extract VSB message buffer files from logger SD cards, and also to export those files to other formats.
