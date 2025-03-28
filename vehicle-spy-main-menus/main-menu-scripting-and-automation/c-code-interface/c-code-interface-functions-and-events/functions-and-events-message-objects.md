# Functions and Events: Message Objects

All message objects in the [Receive, Transmit, and Database](../../../main-menu-spy-networks/message-editor/messages-editor-receive-transmit-and-database-tables.md) tables are represented by message structures. Since this is C the structures are empty by default. To use them you must initialize them by calling an init function. All of these functions and structs are defined in the vspy.c/.h files. For event messages the generated C code calls the init function and passes you a pointer to the structure already filled.\
\
The names of the message structures are the same as the message names with a prefix. For database messages, the prefix is "DB\_". This prefix helps to quickly find the message you want with the intellisense features of Visual C++. Receive messages defined in the message editor have the prefix "MG\_". Transmit messages defined in the messages editor have the prefix "TX\_".\
\
All functions related to the structure have the same name as the struct except they have a description of the function appended to them. Currently, there are 3 functions: Init, ClearStats and Transmit. Init sets up the structure and Transmit sends it out on the bus. ClearStats clears the statistics associated with the message.\
\
&#xNAN;**\_Init** - Fill the message with the current values including statistics.\
\
&#xNAN;**\_Transmit** - Transmits the message. (will return 0 if there was no room in the transmit buffer - otherwise returns one)\
\
&#xNAN;**\_ClearStats** - Clears the statistics associated with the message.\
\
For Transmit messages defined in the transmit table, there is an additional transmit API called **\_TransmitFast()**. This API transmits the message as defined in the transmit table - you do not have to declare a message struct to do so. Finally, the events for the transmit message when the message has been sent successfully (this means the message you transmitted was received back from the hardware).\
\
The generic message is a message that is not defined by the database. You can use this structure to generate a message not defined in the messages editor or database. A description of each part of the struct appears in Table 1. All messages have these properties - database messages also have these properties too. The **GenericMessageTransmit()** function allows you to transmit any generic message.\
\
Database, Transmit and Receive messages all contain a Statistics structure. This structure is filled in during event functions or when you call the \_Init() function. These stats can be cleared using the ClearStats api. These stats are very useful for certain types of tests such as message presence or jitter.\
\
If a message is associated with a transport layer (ISO15765 or J1939) the event for the message will be called when the entire data packet is received. Messages which are associated with a transport layer have a larger data section than the GenericMessage. Transmission of long messages is only supported for messages defined in the transmit spreadsheet.

![Figure 1: The generic message structure.](../../../../.gitbook/assets/generic_message.gif)

**Table 1: Generic Message Properties**

<table><thead><tr><th width="150">Property Name</th><th>Description</th></tr></thead><tbody><tr><td>iNetwork</td><td>Index indicating the network for the message.</td></tr><tr><td>iID</td><td>ID of the message.</td></tr><tr><td>iTimeStampNanoSecondsHW</td><td>Timestamp of the hardware in nanoseconds.<br>(only valid if hardware is used)</td></tr><tr><td>iTimeStampMillisecondsOS</td><td>Timestamp of the message in milliseconds.<br>(OS timestamp timeGetTime() API)</td></tr><tr><td>iNumDataBytes</td><td>Number of data bytes in the message. (DLC)</td></tr><tr><td>iBitField</td><td><p>This integer bitfield indicates message attributes.<br><br><em><strong>For All Received Messages</strong></em>...</p><table><thead><tr><th>Attribute</th><th>BitValue</th></tr></thead><tbody><tr><td>This message was sent by the attached hardware.</td><td>ATTR_ALL_RX_TRANSMIT</td></tr><tr><td>There was some error related to this message.</td><td>ATTR_ALL_RX_ERROR</td></tr></tbody></table><p><br><br><em><strong>For Messages Received/Transmitted with the CAN Protocol...</strong></em></p><table><thead><tr><th>Attribute</th><th>BitValue</th></tr></thead><tbody><tr><td>CAN Message has a 29 Bit Extended ID. (versus a standard 11 bit ID)</td><td>ATTR_CAN_29BIT_ID_FRAME</td></tr><tr><td>CAN Remote Frame.</td><td>ATTR_CAN_REMOTE_FRAME</td></tr><tr><td>CAN High Voltage. (tx only)</td><td>ATTR_CAN_TX_HIGH_VOLTAGE</td></tr></tbody></table></td></tr><tr><td>btData</td><td>Data array of message data.</td></tr><tr><td>iDefaultPeriodMilliseconds</td><td>The default period for the message if there is one.</td></tr></tbody></table>

**Table 2: Message Statistics with Transmit, Database, or Message Objects**

| Statistic Name       | Data Type     | Description                                                            |
| -------------------- | ------------- | ---------------------------------------------------------------------- |
| btPresent            | unsigned char | If the message was received once this will be one.                     |
| btPresentToggle      | unsigned char | Toggles from zero to one every time message is received.               |
| btMultiFrameComplete | unsigned char | This is one if the multiframe sequence has happened and is complete.   |
| dUpdateRateRel       | double        | The periodic update rate in seconds.                                   |
| dUpdateRateAbs       | double        | The absolute update rate in seconds.                                   |
| iPerSecond           | int           | How many messages per second are coming out.                           |
| iCount               | int           | Count of how many messages have come out.                              |
| iChangeCount         | int           | Count of how many times a message changed.                             |
| dStartTime           | double        | The time difference between the first two times this message was sent. |
| dMsgMinTime          | double        | The minimum time difference between two consecutive messages.          |
| dMaxTime             | double        | The maximum time difference between two consecutive messages.          |
| dMeanTime            | double        | The average time difference between all messages.                      |

![Figure 2: Very useful for testing - Message Statistics are part of every received message.](../../../../.gitbook/assets/msg_stats.png)

![Figure 3: The message events are created on the "Message Events" tab.](../../../../.gitbook/assets/message_event.gif)

![Figure 4: The message event passes a pointer to the message structure all filled in.](../../../../.gitbook/assets/message_event_code.gif)

![Figure 5: In Visual Studio, the intellisense of the IDE generates a list box allowing you to pick message signals or generic properties.](../../../../.gitbook/assets/message_event_visualc.gif)

![Figure 6: Here we have a code snippet that transmits a generic message.](../../../../.gitbook/assets/generic_message_tx.gif)
