# Basic Operation of Vehicle Spy

### Overview

Vehicle Spy is a vehicle network tool. As such, it can read and transmit messages on a vehicle network. In Vehicle Spy, messages that are received are grouped into the Receive table in [Messages Editor](../vehicle-spy-main-menus/main-menu-spy-networks/message-editor/) view. Messages that are transmitted are called Transmit Messages. These messages are grouped into the Transmit table in Messages Editor view. Transmit messages are also displayed and transmitted from the [Transmit Panel](../vehicle-spy-main-menus/main-menu-spy-networks/transmit-panel/). Messages, whether transmitted or received, are defined as a collection of bytes which encode some type of data (called a signal) and have an identifier.\
\
For the purposes of working with multiple network vehicles, Vehicle Spy can function on more than one network. [Networks](../vehicle-spy-main-menus/main-menu-spy-networks/networks/) can be setup for a specific protocol and attached to a vehicle [Network Hardware interface](../vehicle-network-interface-hardware/).\
\
Each vehicle network contains a collection of nodes or ECUs. ECUs (Electronic Control Units) act as a source or receiver of messages. Vehicle Spy allows you to assign ECU specifications to messages and signals. This lets you analyze your network based on ECUs.\
\
Vehicle Spy offers many ways in which to view vehicle network data. The first is [Messages view](../vehicle-spy-main-menus/main-menu-spy-networks/messages-view/). This view allows you to see the message traffic as it appears on the bus (scrolling mode) or as a stationary list of messages with changing data bytes (static mode).Messages displayed in Messages view are collected in a circular buffer. Vehicle Spy also contains an exciting feature called [Graphical Panels](../vehicle-spy-main-menus/main-menu-measurement/graphical-panels/) view. With Graphical Panels, users can easily create their own virtual instrument panels. These panels can include meters, graphs, LEDs and numerous other elements for visually representing data.\
\
[Function Blocks](../vehicle-spy-main-menus/main-menu-scripting-and-automation/function-blocks/) are another powerful feature found within Vehicle Spy. This feature gives users custom control over Vehicle Spy. Function Blocks support custom scripting, buffer capturing with pre/post triggering, and replaying messages.
