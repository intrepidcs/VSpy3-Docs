# Data Acquisition with CCP/XCP

Vehicle Spy [MEP](./) supports two methods for collecting data from an ECU using CCP/XCP. Each method has strengths and weaknesses when compared to each other as shown in Table 1.

**Table 1: Comparison of DAQ Methods Using CCP/XCP**

| Category         | Standard DAQ Method                                                                                                          | Event Based DAQ Method                                                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Measurement Rate | User controls how often a measurement is reported.                                                                           | ECU software determines rate based upon a user assigned event.                                                                                  |
| Resource Usage   | Each request triggers only one measurement. This can put more strain on the network and ECU if many measurements are needed. | Only one request is needed to trigger multiple measurements. This can reduce the strain on the network and ECU if many measurements are needed. |
| Synchronization  | Time synchronization is unlikely for a group of measurements.                                                                | Time synchronization occurs for a group of measurements assigned to the same event.                                                             |

### Standard DAQ Method

To perform standard data acquisition over CCP/XCP:\\

1. On MEP/Setup view:
2.
   * [Add an A2L file](mep-setup/#a2l-file-data-item-tree-refer-to-figure-1).
   * Verify the [DAQ Delays](mep-setup/mep-setup-properties.md#daq-delays) on the Properties tab.
3. On [VehicleScape DAQ - Channels tab](../vehiclescape-daq/vehiclescape-daq-channels-tab.md):
4.
   * Add desired A2L file items to the "Selected Channels For Test" area.
   * Double click or use the right mouse menu on A2L items to assign High/Normal/Low priority.
5. Take Vehicle Spy online with the ECU in "[Run with MEP](mep-setup/)" mode.
6. View or store results in many places such as the [Value Editor](mep-value-editor.md), [VehicleScape DAQ - Online tab](../vehiclescape-daq/vehiclescape-daq-online-tab.md), [Signal Plot](../signal-views/signal-plot.md), [Signal List](../signal-views/signal-list.md), or [Graphical Panels](../graphical-panels/).

As shown in Figure 1, the DAQ Delays in MEP determine the update rates of A2L items in VehicleScape DAQ depending on their chosen priorities. Lower delay times will make measurements appear closer to "real time", but also take up more network bandwidth and ECU resources.

![Figure 1: Standard DAQ'ing with CCP/XCP is established with DAQ Delays in MEP being assigned to A2L item priorities in VehicleScape DAQ.](../../../.gitbook/assets/spyMEP_DAQing_Standard.gif)

### Event Based DAQ Method

To perform event based data acquisition over CCP/XCP:

1. On MEP/Setup view:
2.
   * [Add an A2L file](mep-setup/#a2l-file-data-item-tree-refer-to-figure-1).
   * Verify the [CCP Event Setup](mep-setup/mep-setup-properties.md#ccp-event-setup) on the Properties tab.
3. On [VehicleScape DAQ](../vehiclescape-daq/vehiclescape-daq-channels-tab.md) - Channels tab:
4.
   * Add desired A2L file items to the "Selected Channels For Test" area.
   * Double click or use the right mouse menu on A2L items to assign them to CCP Events.
5. Take Vehicle Spy online with the ECU in "[Run with MEP](mep-setup/#a2l-file-data-item-tree-refer-to-figure-1)" mode.
6. View or store results in many places such as the [Value Editor](mep-value-editor.md), [VehicleScape DAQ - Online tab](../vehiclescape-daq/vehiclescape-daq-online-tab.md), [Signal Plot](../signal-views/signal-plot.md), [Signal List](../signal-views/signal-list.md), or [Graphical Panels](../graphical-panels/).

As shown in Figure 2, the ECU software determines the update rate of A2L items in VehicleScape DAQ depending on which event the items are assigned to. Events can help synchronize measurements and reduce resources allocated to DAQ'ing. One event request can trigger multiple measurements instead of using separate DAQ requests for each measurement.

The [MEP Setup - DAQ Tables tab](mep-setup/mep-setup-daq-tables.md) can help show how the A2L items are assigned to the ECU event tables.

![Figure 2: Event based DAQ'ing with CCP/XCP is established with events in MEP being assigned to A2L items in VehicleScape DAQ.](../../../.gitbook/assets/spyMEP_DAQing_Event.gif)
