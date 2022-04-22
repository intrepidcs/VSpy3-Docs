# neoECU 20: IO Map

neoECU 20 does not have a pin map. neoECU 20 is configured using neoVI 3G Explorer, in the same way as a neoVI **FIRE** or neoVI Red would be used. Scripts are loaded into the device over USB just like a neoVI device. Table 1 lists the Pin connections for the device. You should also find this on the back of the neoECU20. The networks setup and functions of the neoECU 20 match a neoVI **FIRE** and standalone scripts are compatible between the two devices.



**Table 2 - neoVI ECU 20 Connector Pin Descriptions**

| **Pin** | **Name**            | **Description**                              |
| ------- | ------------------- | -------------------------------------------- |
| 1       | SW CAN              | Single Wire CAN                              |
| 2       | J1850 VPW           | J1850 VPW (Class 2)                          |
| 3       | LSFT CAN H          | Low Speed Fault Tolerant CAN High            |
| 4       | LSFT CAN L          | Low Speed Fault Tolerant CAN Low             |
| 5       | MS CAN H            | Medium Speed CAN High                        |
| 6       | MS CAN L            | Medium Speed CAN Low                         |
| 7       | ISO L               | UART/ISO9141/Keyword Line "L"                |
| 8       | ISO K/LIN 1         | UART/ISO9141/Keyword Bi-directional Line "K" |
| 9       | DBG CLK             | Not Used                                     |
| 10      | MISC 1              | Miscellaneous Signal 1                       |
| 11      | MISC 2              | Miscellaneous Signal 2                       |
| 12      | DBG Data            | Not Used                                     |
| 13      | PWR GND             | Electrical Ground                            |
| 14      | HS CAN H            | High Speed CAN High                          |
| 15      | HS CAN L            | High Speed CAN Low                           |
| 16      | HS CAN 2 H          | High Speed CAN 2 High                        |
| 17      | HS CAN 2 L          | High Speed CAN 2 Low                         |
| 18      | MISC 4              | Miscellaneous Signal 4                       |
| 19      | HS CAN 3 H          | High Speed CAN 3 High                        |
| 20      | HS CAN 3 L          | High Speed CAN 3 Low                         |
| 21      | TSYNC CLK H / CGI H | CGI High                                     |
| 22      | TSYNC CLK L / CGI L | CGI Low                                      |
| 23      | MISC 3              | Miscellaneous Signal 3                       |
| 24      | DBG RESET           | Not Used                                     |
| 25      | VBATT               | Electrical Positive Supply 6-27 VDC          |

