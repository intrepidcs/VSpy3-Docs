# Application Note: neoVI Logging neoECU DAQ - Part 2: VehicleScape DAQ

### Overview

In this step we are going to setup the Standalone logging settings in VehicleScape and Generate the Logger for CoreMini.

### Process:

1. The first step is to generate a receive message to decode the neoECU's message with the data.  The receive message will match the transmit message that was created before. Make sure to add the signals and proper decoding.
2. Now to make the logger.  Open VehicleScape DAQ from "Measurement-->VehicleScape DAQ"
3. In the channels tab, select the signals that were created.  In the example files they are named Signal 0 - 3.  Add all for channels.  If desired, add any other channels that need to be logged.
4. Configure the [Standalone Logging tab](../../vehicle-spy-main-menus/main-menu-measurement/vehiclescape-daq/vehiclescape-daq-standalone-logging-tab/).   The defaults should work for this example
5. Save the file as (yourname)DecodeECU.vs3.
6. Click the "Generate Logger for CoreMini".
7. [CoreMini Console](../application-note-coremini-partition-logging/)  window will appear.  Remember that this file will go into the neoVI **FIRE** to log data from the neoECU 10.
