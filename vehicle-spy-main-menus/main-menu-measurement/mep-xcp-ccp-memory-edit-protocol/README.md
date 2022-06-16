# MEP (XCP/CCP) - Memory Edit Protocol

Vehicle Spy Memory Edit Protocol (MEP) works with ECUs that use CAN Calibration Protocol (CCP) or Universal Calibration Protocol (XCP) for calibration development. MEP features are found in the Measurement -> MEP menu as shown in Figure 1.

![Figure 1: Look under the Measurement main menu to find the MEP menu selections.](../../../.gitbook/assets/measurement\_menu\_mep.gif)

**Table 1: Vehicle Spy MEP Menu**

| MEP Menu Selection                  | Description                                                     |
| ----------------------------------- | --------------------------------------------------------------- |
| [Setup](mep-setup/)                 | Opens setup dialog to work with A2L files and CCP/XCP settings. |
| [Value Editor](mep-value-editor.md) | Opens dialog to view and edit calibration values.               |
| [Curve Editor](mep-curve-editor.md) | Opens dialog to view and edit calibration curves.               |
| [Map Editor](mep-map-editor.md)     | Opens dialog to view and edit calibration maps.                 |

### Overview

With Vehicle Spy MEP you can:

* [View and edit measurement and calibration items from A2L files.](mep-setup/#a2l-file-data-item-tree-refer-to-figure-1)
* [Upload calibrations from or download calibrations to an ECU using CCP/XCP.](mep-setup/mep-setup-properties.md#ecu-upload-download)
* [Perform data acquisition using CCP/XCP.](data-acquisition-with-ccp-xcp.md)
* [Import/Export calibrations from/to a file.](mep-setup/mep-setup-import-export.md)
* [View setup of event based data acquisition.](mep-setup/mep-setup-daq-tables.md)
* [Unlock secured DAQ or calibration areas using Security DLL files.](mep-setup/mep-setup-security.md)

As shown in Figure 2, Vehicle Spy MEP requires an A2L file to translate the CCP/XCP message traffic with the ECU into user friendly displays and dialogs. The A2L file links an ECU memory map to measurements, calibrations, and diagnostic information. An A2L file that follows ASAM specifications can be created with the ICS ASAP2 Editor and a standard format object file that defines the ECU's memory map.

![Figure 2: Overview of how Vehicle Spy MEP supports ECUs that use CCP/XCP.](../../../.gitbook/assets/spyMEPOverview.jpg)

Acronyms from specifications related to Vehicle Spy MEP can be confusing, so here's a short list to help understand them:

* A2L - ASAM MCD-2MC language used in an ECU's A2L file.
* ASAM - Association for Standardization of Automation and Measuring Systems (www.asam.net)
* ASAP2 - from German "Arbeitskreis zur Standardisierung von Applikationssystemen". Old acronym now renamed to ASAM MCD-2MC.
* CCP - CAN Calibration Protocol
* DAQ - Data Acquisition
* MCD - Measurement, Calibration, and Diagnostics
* MEP - Memory Edit Protocol
* ODT - Object Descriptor Table
* XCP - Universal Calibration Protocol
