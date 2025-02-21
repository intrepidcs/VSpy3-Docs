# Application Note: XCP Driver Example - Part 2: Example XCP Driver

### Example XCP Driver Overview

The example XCP driver provided by Intrepid is written in ANSI-C and can be ported to any ECU project that supports a C Code compiler. The files, SpyCCode.c and SpyCCode.h contain the example XCP driver. These files are part of the Microsoft Visual Studio project (CXCPSim.vsproj), inside the Intrepid\_XCP\_Driver.zip file. You can use Vehicle Spy along with Visual Studio to single-step debug the drive and example ECU simulation and make any modifications that you like on the PC before porting the code to your embedded application. This way you can learn and understand all aspects of XCP without expensive embedded debuggers and other tools.

### Example XCP Driver configuration

The example XCP driver provided by Intrepid can be used freely at no cost but Intrepid assumes no liability for this example implementation.

Intrepid's driver includes the following command support. If you require different or more functionality than what is provided here, please contract you local Intrepid representative to discuss your needs.

**BASIC MEMORY COMMANDS**\
\
CONNECT\
DISCONNECT\
GET\_STATUS\
SYNC\
GET\_SEED\
UNLOCK\
SET\_MTA\
SHORT\_UPLOAD\
DOWNLOAD\


**DATA ACQUISITION COMMANDS (DAQ)**\
\
CLEAR\_DAQ\_LIST\
SET\_DAQ\_PTR\
WRITE\_DAQ\
SET\_DAQ\_LIST\_MODE\
START\_STOP\_DAQ\_LIST\
START\_STOP\_SYNCH\
GET\_DAQ\_LIST\_INFO
