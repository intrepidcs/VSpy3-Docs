# Tutorial: Sort Messages by ECU

### Overview

Vehicle networks are made up of many different ECUs. Sometimes, it is useful to record the data from a single ECU and then play it back through Vehicle Spy at a later time. This task can be accomplished by using function blocks and individual buffers for single or multiple ECUs.\
\
This tutorial will show how to record buffers from single modules and play them back in any combination.\
\
To achieve this goal, Tutorial 4 will guide you through the steps listed below.

1. Enter ECU message filters in Messages Editor
2. Create filtered Capture function blocks to sort incoming messages by ECU
3. Separate incoming messages by ECU
4. Setup trigger messages for Playback function blocks
5. Create Playback function blocks for each ECU
6. Create Script function blocks to trigger Playback blocks
7. Create a Graphical Panel
8. Run newly created application
