# Messages Editor: Message Fields

**Table 1** lists all available fields in the Messages Editor. The Network selection determines which of these fields are displayed at any given time. For more detail, please click on each field title.

**Table 1: Available Message Fields in Messages Editor**

| Field              | Network                                                           | Short Description                                                                                                                        |
| ------------------ | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Key                | Any                                                               | Unique number assigned by Vehicle Spy to the message. This field is read only.                                                           |
| Description        | Any                                                               | Text description of the message.                                                                                                         |
| Type               | CAN or LIN                                                        | <p>CAN - Specifies the Arb ID as Standard 11 bit or Extended 29 bit.<br>LIN - Specifies the message as Master, Slave, or Break Only.</p> |
| Arb ID             | CAN                                                               | Arbitration ID for CAN messages.                                                                                                         |
| PT, Trgt, Src      | <p>J1850 VPW 3 byte hdr<br>ISO9141 / Keyword<br>J1850 PWM<br></p> | Priority/Type, Target, & Source bytes for some types of networks.                                                                        |
| ID                 | <p>J1850 VPW 1 byte hdr<br>LIN<br>CGI</p>                         | The one byte message ID for some types of networks.                                                                                      |
| Multi              | CAN                                                               | Determines if the CAN message is multi-frame and follows the ISO15765-2 or J1939 specifications.                                         |
| Checksum           | LIN                                                               | Selects the Classic or Enhanced checksum type for LIN messages.                                                                          |
| DLC / Len          | CAN or LIN                                                        | Expected length of the CAN or LIN message in bytes.                                                                                      |
| Data Bytes B1 - B? | Any                                                               | Data bytes of the message. Number of data bytes depends upon the network.                                                                |
| Src Node           | Any                                                               | Source Node (or ECU) assigned to the message.                                                                                            |
| Tx Message         | Any                                                               | Allows you to associate a receive message to a transmit message for auto response, transmit on change, or signal linking.                |
| Color              | Any                                                               | Determines the color of the message in the Messages view.                                                                                |
