# VehicleScape DAQ

VehicleScape DAQ is a signal data acquisition tool that integrates diagnostics with [Logging](../logging.md). VehicleScape DAQ can reduce the time it takes to access common diagnostic signals like DIDs, DPIDs, PIDs, memory locations, and fault codes, because it builds the necessary diagnostic jobs for you. The signals can be viewed in real time, logged, or gated to other networks.

VehicleScape DAQ can create [Standalone Logging](vehiclescape-daq-standalone-logging-tab/) scripts to let hardware from Intrepid Control Systems collect data while disconnected from a computer. Standalone Logging requires ICS hardware that supports an SD card and [CoreMini](../../main-menu-tools/utilities-coremini-console/) scripting.

This feature includes a number of controls and options, which are split across six regions for your convenience. These are accessed via tabs found below the main Vehicle Spy window tabs (Figure 1).

The tabs are generally used in order from left to right. A typical work flow might begin with setting up databases, then selecting channels to log, and then generating a script for hardware to run by itself.

![Figure 1: The six VehicleScape DAQ tabs.](../../../.gitbook/assets/spyvehiclescapedaq.gif)

A description of each of the VehicleScape DAQ tabs, along with links to pages explaining them further, can be found in Table 1.

**Table 1: VehicleScape DAQ Tabs**

| Menu Item                                                                  | Description                                                             |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [Database/Hardware Setup](vehiclescape-daq-database-hardware-setup-tab.md) | Configure your hardware and databases for data acquisition.             |
| [Channels](vehiclescape-daq-channels-tab.md)                               | Select channels (signals) to view, log or gate.                         |
| [PC Logging](vehiclescape-daq-pc-logging-tab.md)                           | Define parameters to allow the PC to view or log signals in real time.  |
| [Standalone Logging](vehiclescape-daq-standalone-logging-tab/)             | Set up and generate a script for ICS hardware to log data without a PC. |
| [Gateway](vehiclescape-daq-gateway.md)                                     | Configure a gateway to transmit signals to another network.             |
| [Online](vehiclescape-daq-online-tab.md)                                   | Go online with Vehicle Spy to use PC Logging or a defined gateway.      |

Multiple VehicleScape DAQ configurations can be created within a Vehicle Spy setup. To add a new DAQ configuration, use the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/daq\_add\_button.gif) button near the top right corner of the window; to remove one, use the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/daq\_delete\_button.gif) button. Select from among the currently-defined configurations using the drop-down list found in the same area (Figure 2).

![Figure 1: Controls for adding, removing and selecting DAQ setups.](../../../.gitbook/assets/daq\_selection.gif)
