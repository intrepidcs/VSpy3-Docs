# Vehicle Spy Text API

### Objective

The purpose of the Text API is to provide a simple text based command set for Vehicle Spy 3 to allow third party applications to take advantage of the power of Vehicle Spy without rewriting much code.\
The Text API command set is text based so it can be easily used over many interfaces such as RS232, USB, Ethernet, or Wireless. It is also independent of the operating system or development environment of the host. The command set is similar to what may be found in a programmable instrument consisting of commands and responses.\
You can easily write an object or function wrapper around the Text API. This will allow a more convenient use in professional languages such as C#,  Visual Basic, LabVIEW, or C/C++. The Text API could also exist as a simple macro language itself.

### Tips for Learning

The best way to learn the Text API is to experiment. The Text API terminal in Vehicle Spy 3 is a great tool for this purpose. Also, because most of the commands are based on the XML tags, you can just open the vs3 file in a text editor to see what properties can be manipulated via this extremely flexible API.

### Summary of Rules

* All commands start with the default root object.
* Commands are separated by a \<CR>,\<LF> or \<CR>\<LF> combination.
* Commands are case insensitive. Arguments can be case sensitive if they are text based such as Description properties.
* All objects and properties have the same text as their XML element names. Properties can be changed by calling out the property and supplying an argument. Property values can be returned by using a question mark ? to query the property.

### The following rules are not yet supported

* There is special encoding to support non ASCII, extended characters, the % escape character, and the ; comment character. Where % will be followed with the Text number in four digit hex form. For example, %000D would equal CR, %000A would be \<LF>. The four digit Text allows Unicode support for text arguments such as descriptions.
* The comment character is the semicolon. After the semicolon all characters are ignored until the next command.
* The Text API is available as UNICODE via the Vehicle Spy 3 DLL.

### Command and Queries

The basic communication consists of commands and queries. Commands set a property or execute a method. Queries request a property.\
\
Commands and Queries will return one of two of possible responses: ok or er. "ok" means that the command completed successfully. "er" means there was a problem with the command. The ok will have text following the command that indicates what command completed and any return values.\
\
Events can be either asked for with a method or can appear asynchronously in the receive stream. You also must specify, or "register", which events you wish to receive.

**Table 1: Syntax of Commands, Queries, and Events**

|   Type  |     Syntax of Command    |  Syntax of Successful Response  |
| :-----: | :----------------------: | :-----------------------------: |
| Command | _methodname_ {arguments} |         ok _methodname_         |
| Queries |       _methodname_?      | ok _methodname_ {propertyvalue} |

### Examples:

_A successful start command_\
\
Host: Start\
Vehicle Spy 3:ok start\
\
_A unsuccessful root command_\
\
Host: Startasdf\
Vehicle Spy 3: er command not found:startasdf\
\
_A successful query_\
\
Host: AutoDetectHardware?\
Vehicle Spy 3: ok autodetecthardware 1\
\
example: LoadFile Method\
\
This command starts with root object and ends with a carriage return.\
\
Host: loadfile text.vs3\<CR>\
Vehicle Spy 3: ok loadfile

### neoVI PRO Text API

The neoVI PRO supports two APIs, first is the Text API and the second is the neoVI RAW API. The Text API is the default API on the USB, COM, and Ethernet (via TCP) ports; therefore, all of the Text API commands here work with the Vehicle Spy 3 code running in the neoVI PRO.

### Using the Text API

The following table indicates how you can interact with the Text API.



| Application   | Source                                 | Comment                                                                            |
| ------------- | -------------------------------------- | ---------------------------------------------------------------------------------- |
| Vehicle Spy 3 | Text API Terminal                      | Allows you to manually type in Text API commands and see their responses.          |
| Vehicle Spy 3 | Function Blocks                        | Allows you to send and receive Text API commands.                                  |
| Vehicle Spy 3 | Via COM or TCP port                    | Vehicle Spy 3 can act as a COM or TCP server. Setup via Tools/Options.             |
| neoVI PRO     | neoVI PRO setup                        | The neoVI PRO setup allows you to send commands to neoVI PRO on the control panel. |
| neoVI PRO     | via USB, COM and TCP ports             |                                                                                    |
| DLL           | The TextAPI method of the icsneo40.dll | Not yet supported.                                                                 |



### Root Objects

| Command Name                                        | Description                                                                                                                                                                                   | Example                                                                                                                |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Root Objects for Application Signals**                |                                                                                                                                                                                               |                                                                                                                        |
| all?                                                | returns all application signals that are not remote signals in a key=value comma separated string. This is used to efficiently read all app signals over a slower network.                    | `all?`                                                                                                                   |
| allsetup?                                           | returns all application signals that are not remote signals in a key=description comma separated string. This is used to efficiently read all app signals descriptions over a slower network. |                                                                                                                        |
| apprestore                                          | Restores application signals from disk.                                                                                                                                                       |                                                                                                                        |
| appsave                                             | <p>Saves application signals to disk. Application Signals must be enabled for saving. Signals are saved in a file in the same path as the vs3 file.<br><br>{vs3 file name}.appini</p>         |                                                                                                                        |
| as                                                  | Accesses the collection of Application Signals. See the topic on [Collection Objects](./#collection-objects).                                                                                 |                                                                                                                        |
| as(index or key)                                    | Accesses a specific application signal by an index or a key. Set the topic on [Signal](./#signal-objects) objects.                                                                            |                                                                                                                        |
| **Root Objects for Diagnostic Jobs**                    |                                                                                                                                                                                               |                                                                                                                        |
| dg                                                  | Accesses a specific diagnostic jobs by an index or a key.                                                                                                                                     | `dg(0).start ; starts a diag job.`                                                                                        |
| **Root Objects for Files and Paths**                    |                                                                                                                                                                                               |                                                                                                                        |
| copyfile                                            | Copies a file in the data directory to another in the data directory. Source and target are separated by a comma. Make sure the file is accessible and not in use.                            | `copyfile MyTestfile.vs3,CopyOfMyTest.vs3`                                                                               |
| deletefile                                          | Removes a file in the data directory. Make sure the file is accessible and not in use.                                                                                                        | `deletefile FileToDelete.vs3`                                                                                            |
| dir                                                 | Returns the files in the root of the compact flash card or the Vehicle Spy data directory. A filter spec determines which files to return.                                                    | `dir? \*.\*`                                                                                                             |
| diskspace                                           | returns the amount of diskspace both available and total in kilobytes.                                                                                                                        | `diskspace?`                                                                                                             |
| filedetails                                         | Returns information size, time/date on a file in the data directory/neoVI PRO compact flash card.                                                                                             | `filedetails? test.vs3`                                                                                                  |
| loadfile                                            | Loads a setup file from the data directory. This command should not be called from the same instance of Vehicle spy.                                                                          | `loadfile test.vs3`                                                                                                      |
| renamefile                                          | Renames a file in the data directory. The input and output files names are separated by a comma. Make sure the file is accessible and not in use.                                             | `renamefile FileName.vs3,NewNameForFile.vs3`                                                                             |
| status                                              | Returns the loaded file and whether the file is running.                                                                                                                                      | `status?`                                                                                                                |
| **Root Objects for Function Blocks**                    |                                                                                                                                                                                               |                                                                                                                        |
| fb                                                  | Accesses the collection of Function Blocks. See the topic on [Collection Objects](./#summary-of-rules).                                                                                       | `fb.count? ;asks for the number of function blocks`                                                                      |
| fb(index or key)                                    | Accesses a specific function block by an index or a key. Set the topic on [function block](./#function-block-objects) objects.                                                                | <p>`fb(1).start ;starts the first function block.`<br><br>`fb(tst2).stop ;stops the function block with key tst2.`</p>     |
| **Objects for GPS or Joystick**                         |                                                                                                                                                                                               |                                                                                                                        |
| gps                                                 | Accesses the GPS object.                                                                                                                                                                      | <p>`gps.latitude?`<br>`gps.longitude?`<br>`gps.altitude?`<br>`gps.speed?`<br>`gps.isvalid?`</p>                                  |
| JoystickEnabled                                     | Indicates whether the joystick is enabled or not.                                                                                                                                             |                                                                                                                        |
| JoystickSelected                                    | Indicates which joystick is used.                                                                                                                                                             |                                                                                                                        |
| **Root Objects for Graphical Panels or User Interface** |                                                                                                                                                                                               |                                                                                                                        |
| gp(index or key)                                    | Graphical Panel objects.                                                                                                                                                                      |                                                                                                                        |
| gp(index or key).all?                               | returns all graphical panel control values in a key=value comma separated string. This is used to efficiently read all graphical panel data over a slower network.                            | `gp(dia1).all?`                                                                                                          |
| gp(index or key).allsetup?                          | returns the graphical panel as an XML string.                                                                                                                                                 |                                                                                                                        |
| gpallsetup?                                         | returns all graphical panels in a key=description comma separated string. This is used to efficiently read all panel descriptions over a slower network.                                      |                                                                                                                        |
| ui                                                  | Controls the user interface of neoVI PRO. Described in a [separate topic](vehicle-spy-text-api-ecu-object.md).                                                                                |                                                                                                                        |
| **Root Objects for Hardware**                           |                                                                                                                                                                                               |                                                                                                                        |
| ao                                                  | Accesses a specific analog outputs by an index or a key. See the topic on transmit message objects.                                                                                           | `ao(0).value 3.42`                                                                                                       |
| id                                                  | Returns the current neoVI PRO firmware ID.                                                                                                                                                    | `id? ;get the neoVI PRO ID.`                                                                                             |
| io0isoutput or io1isoutput                          | Returns/Sets whether MISC1 pin is an output or input.                                                                                                                                         | `io0isoutput 1 ;make MISC1 and output`                                                                                   |
| io0value                                            | Returns/Sets the value of the MISC 1 pin on neoVI PRO on the DB15 connector.                                                                                                                  | `io0value?`                                                                                                              |
| io1value                                            | Returns/Sets the value of the MISC 2 pin on neoVI PRO on the DB15 connector.                                                                                                                  | `io1value 1`                                                                                                             |
| ixcbusenabled                                       | Returns/Sets whether the ixcbus is enabled.                                                                                                                                                   |                                                                                                                        |
| ixcbusnetwork                                       | Returns/Sets the network where the IXCBus protocol is used.                                                                                                                                   |                                                                                                                        |
| **Root Objects for J1939**                              |                                                                                                                                                                                               |                                                                                                                        |
| j1939dm1srcall                                      | Returns a comma separated list of SRC addresses that have active DTC's                                                                                                                        | `j1939dm1srcall?`                                                                                                        |
| J1939dm1src(address)                                | [J1939 Object](./#j1939-objects); also returns list of DTCs for specified address                                                                                                             | `j1939dm1src(0)?`                                                                                                        |
| **Root Objects for Messages**                           |                                                                                                                                                                                               |                                                                                                                        |
| db                                                  | Accesses the collection of database messages. See the topic on [Collection Objects](./#collection-objects).                                                                                            |                                                                                                                        |
| db(index or key)                                    | Accesses a specific [message object](./#message-objects) by an index or a key. See the topic on message objects.                                                                              | `db(0).description? ; retrieve the name `                                                                        |
| mg                                                  | Accesses the collection of Messages. See the topic on [Collection Objects](./#collection-objects).                                                                                            |                                                                                                                        |
| mg(index or key)                                    | Accesses a specific [message object](./#message-objects) by an index or a key. See the topic on message objects.                                                                              | `mg(0).clearstats ;clears the stats of first msg`                                                                        |
| tx                                                  | Accesses the collection of Transmit Messages. See the topic on [Collection Objects](./#collection-objects).                                                                                   | `tx.additem ;adds a message at the end of the collection`                                                                |
| tx(index or key)                                    | Accesses a specific transmit message by an index or a key. See the topic on transmit message objects.                                                                                         | `tx(1).Arbid 234 ;sets the arb id in hex`                                                                                |
| **Root Objects for Simulation**                         |                                                                                                                                                                                               |                                                                                                                        |
| ecu                                                 | Accesses the ecu subobject. This is discussed in a [separate topic](vehicle-spy-text-api-ecu-object.md).                                                                                      |                                                                                                                        |
| SimulationEnabled                                   | Sets/Returns whether simulation is used or you are connecting to hardware.                                                                                                                    |                                                                                                                        |
| SimulationPath                                      | Sets/Returns the path of the file used for simulation mode.                                                                                                                                   |                                                                                                                        |
| **Root Objects for Vehicle Spy**                        |                                                                                                                                                                                               |                                                                                                                        |
| AutoDetectHardware                                  | Sets whether Vehicle Spy will detect hardware or not.                                                                                                                                         | <p>`AutoDetectHardware 1 ;sets hardware to autodetect.`<br><br>`AutoDetectHardware? ;asks for the autodetect setting.`</p> |
| isrunning                                           | Returns whether if Vehicle Spy is running or not.                                                                                                                                             | `isrunning?`                                                                                                             |
| Start                                               | Starts Vehicle Spy.                                                                                                                                                                           |                                                                                                                        |
| Stop                                                | Stops Vehicle Spy.                                                                                                                                                                            |                                                                                                                        |
| timedate                                            | Returns/Sets the time date of the clock.                                                                                                                                                      | `timedate?`                                                                                                              |

### Analog Output Objects

| Command Name           | Description                                                                                                                                                           | Example                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| calculatefromsignal    | Returns/Sets whether analog outputs are automatically calculated using busdecoder mode or can be set via the Text API. The power default is automatically calculated. | `ao(0).calculatefromsignal 0 ; allow manual control`       |
| EnableCalibratedValues | Returns/Sets whether analog outputs are scaled according to the calibration scaling. Disable this feature to perform calibration.                                     | `ao(0).EnableCalibratedValues 0 ; disable for calibration` |
| messagekey             | Returns/Sets the key of the message attached to this analog output.                                                                                                   |                                                         |
| signalkey              | Returns/Sets the key of the signal attached to this analog output. This is used in conjunction with signal key.                                                       |                                                         |
| value                  | Returns/Sets the value of the output. This is only valid if calculatefromsignal is false.                                                                             | `ao(0).value 3.21 ; sets output to 3.21V`                  |

### Collection Objects

| Command Name       | Description                                                                                   | Example                                                   |
| ------------------ | --------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Additem            | Adds an item to the end of the collection.                                                    | `fb.additem ;adds an item to the end of the collection.`    |
| Count              | Indicates how many items in the collection. Read only.                                        | `tx.count? ;how many tx messages are defined?`              |
| DeleteAllObjects   | Removes all items from the collection.                                                        | `as.deleteallobjects ;remove all of the app signals.`       |
| KeyExists          | Determines if the specified key exists in the collection.                                     | `tx.keyexists out0 ;does this key exist in the collection?` |
| ReturnIndexFromKey | Finds the key in the collection and returns the index. If the key is not found it returns -1. | `tx.returnindexfromkey out0`                                |



### Function Block Objects



| Command Name | Description                    | Example                                       |
| ------------ | ------------------------------ | --------------------------------------------- |
| save         | Saves the function block data. |                                               |
| start        | Starts the function block.     | `fb(0).start ;starts the first function block.` |
| stop         | Stops the function block.      |                                               |
| trigger      | Triggers the function block.   |                                               |



### J1939 Objects

| Command Name  | Description                                                  | Example                    |
| ------------- | ------------------------------------------------------------ | -------------------------- |
| dtc(code).spn | Returns the SPN number for requested DTC (specified by code) | `j1939dm1src(0).dtc(0).spn?` |
| dtc(code).FMI | Returns the FMI number for requested DTC (specified by code) | `j1939dm1src(0).dtc(0).fmi?` |
| dtc(code).oc  | Returns the OC number for requested DTC (specified by code)  | `j1939dm1src(0).dtc(0).co?`  |

### Message Objects

| Command Name                                       | Description                                                                                                    | Example                                                                                                       |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| ByteStringX                                        | Sets the filter bytes for a network in hex.                                                                    | `mg(0).ByteString0 110`                                                                                         |
| CFTimeOutsMs                                       | Specifies the Consecutive Frame timeout in milliseconds.                                                       |                                                                                                               |
| ClearStats                                         | Clears all statistical information associated with the message. Does not clear signal stats.                   | `mg(0).ClearStats`                                                                                              |
| Compile                                            | Compiles filter bytes and equations and then makes changes activate.                                           |                                                                                                               |
| Description {Text Description}                     | Sets the description for a message.                                                                            | <p>Set the description for message number 4 as Engine Data:<br><br>`mg(3).description Engine Data`</p> |
| DisplayColor                                       | Sets/Returns the color the message is displayed with.                                                          | `mg(0).DisplayColor 0 ;display black`                                                                           |
| EnableISO15765                                     | This enables long messaging on CAN based off of ISO15765.                                                      |                                                                                                               |
| EnRxEvent {Return Msg, Return Value, Return Stats} |                                                                                                                | `sg(in3433).EnRxEvent`                                                                                         |
| ExpectedLength                                     | Sets the expected length of a specific message.                                                                |                                                                                                               |
| FlowCArbID                                         | Sets/Returns CAN id used for the flow control frame in iso15765 messaging.                                     |                                                                                                               |
| FlowCBlockSize                                     | Sets/Returns the block sized used in long can messaging.                                                       |                                                                                                               |
| FlowCSTmin                                         | Sets/Returns the flow control STMin.                                                                           |                                                                                                               |
| refresh                                            | Updates message table. This is useful when making changes to messages via text API                             | `mg.refresh`                                                                                                    |
| sg                                                 | Accesses the collection of Signals. See the topic on [collection objects](./#collection-objects).              |                                                                                                               |
| sg(index or key)                                   | Accesses a specific [Signal object](./#signal-objects) by an index or a key. See the topic on message objects. | `sg(0).value? ;Asks for the Value of the first signal`                                                          |

### Signal Objects

| Command Name                   | Description                                                                             | Example                                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| value                          | Sets/Gets the value.                                                                    |                                                                                                                                 |
| Description {Text Description} | Sets the description for a signal.                                                      | <p>Set the description for signal number 4 as throttle position:<br><br>`mg(0).sig(3).description Throttle Position`</p> |
| DisplayColor                   | Sets/Returns the color the message is displayed.                                        | `mg(0).DisplayColor 0 ;display black`                                                                                             |
| Equation                       | Gets/Sets the equation.                                                                 |                                                                                                                                 |
| Format                         | Get/Sets the equation format.                                                           |                                                                                                                                 |
| refresh                        | Updates signal information. This is useful when making changes to signals via text API. |                                                                                                                                 |

### ASCII Chart

```
    0   1   2   3   4   5   6   7   8   9   A   B   C   D   E   F
0  NUL SOH STX ETX EOT ENQ ACK BEL BS  HT  LF  VT  FF  CR  SO  SI
1  DLE DC1 DC2 DC3 DC4 NAK SYN ETB CAN EM  SUB ESC FS  GS  RS  US
2   SP  !   "   #   $   %   &   '   (   )   *   +   ,   -   .   /
3   0   1   2   3   4   5   6   7   8   9   :   ;   <   =   >   ?
4   @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O
5   P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _
6   `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o
7   p   q   r   s   t   u   v   w   x   y   z   {   |   }   ~ DEL
```
