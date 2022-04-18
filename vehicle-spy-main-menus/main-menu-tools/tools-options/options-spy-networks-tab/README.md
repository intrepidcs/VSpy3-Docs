# Options: Spy Networks Tab

Vehicle Spy interacts with a vehicle network through Vehicle Network Hardware available from ICS. The ability to setup various hardware settings can be found using the "Spy Networks" tab in the Vehicle Spy Setup dialog (Figure 1), found under the Tools -> Options menu.

### Simulation Mode

Vehicle Spy allows simulation of hardware by reading a data file and playing it back into Vehicle Spy as if it was coming directly from the hardware. This is useful for training or setting up VS3 files when it would not be possible to utilize the specific hardware or a network.\
\
To enable hardware simulation, first enable the "Simulation Mode" checkbox and select a data file using the "Browse" button. Now going online with the main Vehicle Spy blue play/stop button will immediately begin simulating the data that was selected. If the simulation files are needed to be changed quickly, use the Run Simulation selection in the pull down list next to the blue play/stop button.\
\
Sample data files are included in the Vehicle Spy 3 directory. The file "All Bus Traffic.csv" is used in the Vehicle Spy tutorials to simulate traffic.

![Figure 1: The Spy Networks tab lets you run in simulation mode or configure your hardware.](../../../../.gitbook/assets/spyHardwareSetup.gif)

### Hardware Setup

If vehicle network hardware is available then use this area to help configure it. If Auto-Detect is not enabled, the hardware connection needs to be specified.

* **Auto-Detect Hardware** - automatically uses the first supported connected device on the system.
* **Multiple Devices** - supports multiple devices that must be manually specified.
* **Enable RTC Sync** - sets the Real Time Clock inside supported hardware to match the PC time.
* **Sync Multiple Devices to PC** - syncs time from the computer
* **Enable Auto Update** - ensures the current firmware in Vehicle Spy is also in the hardware.
* **Enable Bit Rate Sync** - checks for baud rate conflicts between hardware and Network settings.
* **Enable Low Latency** - option to try and read USB data quicker. This option should be disabled in most cases.
* **Discover devices on Ethernet** - discover devices on the PC via ethernet.

### J1850 VPW Mode

This option determines how J1850 VPW header bytes will be treated.

### neoVIServer Settings

"Enable Server" allows neoVI hardware to be used by multiple applications at the same time.\
\
"Enable Device Sharing" controls how Vehicle Spy connects to shared neoVI hardware when BOTH neoVIServer and Autodetect Hardware are enabled. If Device Sharing is enabled then Vehicle Spy connects to the last hardware used or the first one it autodetects, regardless if that hardware is opened by other applications. If Device Sharing is disabled then Vehicle Spy skips over hardware currently opened by other applications.

### Problem Log

When "Show Warnings from Missing A2L Items" is enabled, suppressed warnings will be displayed in the Problem Log. If this is disabled minor warnings will not be displayed.

### OEM Specific Features

This area enables helpful features specific to Original Equipment Manufacturers and their suppliers. These settings can directly affect how other areas in Vehicle Spy will appear and operate.

* GMLAN - GMLAN protocol for General Motors.
* KWP2000 - Keyword 2000 protocol for Chrysler.
* J1939 - SAE J1939 protocol for John Deere.
* GGDS - ISO 14229 protocol for Ford.
* HDLAN - ISO 14229 protocol for Harley Davidson.

### Replay Options

Allows the ability to distinguish an ArbID on the SW network for high voltage while replaying a vsb or csv.

### CoreMini

Enable Hardware Acceleration to use CoreMini to periodically transmit messages as efficiently as possible.

### Messages

* Auto Add J1939 RX messages - Automatically add J1939 messages to the receive table
* Timestamp Nanosecond Precision - Allows nanosecond precision to be applied to messages

### Automotive Ethernet Features

Use the PC ethernet adapter to interface with automotive ethernet.

### Signal Name

Switch from displaying the signal's long name to the short name as defined in a database file.

### C Code Interface

Manually set the default output log size for the C Code interface.
