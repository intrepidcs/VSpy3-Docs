# Vehicle Spy Text API: ECU Object

### Objective

ECU specific functionality is accessed via the ecu object.  The syntax is as follows:\
ecu.sim.simulatetransmitmessages 0  ;simulate the receive messages for those in the ECU collection

## ECU Object

| **Command Name** | **Description**             | **Example**                                         |
| ---------------- | --------------------------- | --------------------------------------------------- |
| sim              | Accesses the ECU simulator. | <p>ecu.sim.compile  <br> ;compile the simulator</p> |

***

**ecu.sim Object**

| **Command Name**         | **Description**                                                                                                                                              | **Example**        |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| compile                  | Compiles the changes made to the ECUs collection.  It will regenerate the tx message collection. and copy the signals from the signal collect.               |                    |
| defaultsignaltype        | This is an enumerated constant indicated for signals not accounted for in the signals collection or the replay data file.                                    |                    |
| ec                       | Accesses the collection of Simulator ECUs for simulation.                                                                                                    |                    |
| isrunning                | Indicates if the simulator is running or not.                                                                                                                | ecu.sim.isrunning? |
| manualstart              | Set/Returns if the simulator starts when Vehicle Spy starts.                                                                                                 |                    |
| replaydatafile           | Set/Returns if the name of the vehicle spy log file used for replay.                                                                                         |                    |
| repeatreplay             | Set/Returns if the replay should automatically restart when the file completes.                                                                              |                    |
| start                    | Starts the simulator.                                                                                                                                        |                    |
| stop                     | Stops the simulator.                                                                                                                                         |                    |
| simulatenormal           | Returns/Sets if the ECUs should simulate normal messaging.                                                                                                   |                    |
| simulatediagnostics      | Returns/Sets if the ECUs should simulate diagnostics messaging.                                                                                              |                    |
| simulatetransmitmessages | <p>1 = tx message list is generated from the tx list of each ECU.<br><br>0 = tx message list is generated from the rx list of each ECU.</p>                  |                    |
| sg                       | A [collection of signals](./) which will be copied to the transmit message upon compilation.                                                                 |                    |
| tx                       | This is the [collection of transmit messages](./) sent by the simulator.  It is dynamically created by the compile method.                                   |                    |
| replaystart              | This starts the replay data file at the first value if the simulator is running.                                                                             |                    |
| replaystop               | This stops file replay if it is running.                                                                                                                     |                    |
| generatehvwakeup         | If 1 the simulator will generate a single wire CAN high voltage wakeup when started.                                                                         |                    |
| mg                       | Accesses the collection of Messages for simulation.  Messages are only present if they apply some custom properties such as default message bytes or period. | <p><br></p>        |
| GenerateVNMF             | If 1 the simulator will generate a VNMF for the single wire CAN ECUs involved in the simulation.                                                             |                    |
| VNMFID                   | This indicates the CAN ID of the VNMF used by the simulator                                                                                                  |                    |



#### ecu.sim.ec Object

| **Command Name**        | **Description**                                                                                                                   | **Example** |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| ecuname                 | The ECU short name.                                                                                                               |             |
| enablenetworkmanagement | If 1 the simulator uses VN (virtual network) states to determine which messages should be sent.  Otherwise, they are always sent. |             |
| key                     |                                                                                                                                   |             |
| networkname             | The network name according to the uef file "hsCAN" or "swCAN".                                                                    |             |

#### ecu.sim.mg Object

|  Command Name  | Description                                                                                                                | Example |
| :------------: | -------------------------------------------------------------------------------------------------------------------------- | ------- |
|  databytes{X}  | This allows default databytes to be entered for databytes0 through databytes7.                                             |         |
|   description  | <p>The description of the message.  This includes the ECU name followed by a backslash.</p><p>"SDM\Airbag Indications"</p> |         |
| disablemessage | This disables this message if 1.                                                                                           |         |
| overrideperiod | This will override the period of the message.                                                                              |         |
|     period     | The modified message period if "overrideperiod" is 1.                                                                      |         |

\
