# Application Note: XCP Driver Example - Part 3: ECU Simulation and Porting XCP Driver

### Example ECU Simulation

The XCP driver DAQ configuration has 3 STATIC DAQ Lists all of which have configurable EVENT associations. This means that the user of Vehicle Spy can dynamically configure the rate of any of the DAQ Lists. Inside the Vspy\_Main() function is an infinite loop that provides 3 separate rates for EVENTs:

EVENT\_0 = 10ms\
EVENT\_1 = 100ms\
EVENT\_2 = 500ms\
\
The XCP packets sent back to Vehicle Spy do have Timestamps. Vehicle Spy timestamps the data based on when the CAN frames are received by the hardware.

### Porting the XCP Driver to an ECU

The example XCP driver source code is used not only as ECU code but also an XCP ECU simulation that runs on the PC in Vehicle Spy's C Code interface. Therefore, there are some hooks in this example driver that need to be removed for an actual implementation of the driver in an ECU. Throughout the C code there are references to the comment "\[ECU CODE CHANGE NOTE]".This comment indicates a place where you will need to consider changing the code for your ECU.
