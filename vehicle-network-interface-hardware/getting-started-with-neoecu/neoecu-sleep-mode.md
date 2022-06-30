# neoECU Sleep Mode

neoECU devices also have a sleep mode.  Sleep mode can be enabled in [Function Block](../../vehicle-spy-main-menus/main-menu-scripting-and-automation/function-blocks/) scripts using the [Sleep](../../vehicle-spy-main-menus/main-menu-scripting-and-automation/function-blocks/function-blocks-types/script-type-function-block-commands/script-type-function-block-command-sleep.md) step command. Table 1 gives an example [Function Block](../../vehicle-spy-main-menus/main-menu-scripting-and-automation/function-blocks/) script to enable sleep mode. This script works by checking the present status of a message. If the message is not received when it is expected, the device will go to sleep.  When normal traffic is received again, the neoECU will wakeup again.

**Table 1: Example Function Block for enabling sleep mode**

| Step |                                                                             | Description | Value                      | Comment                                                          |
| ---- | --------------------------------------------------------------------------- | ----------- | -------------------------- | ---------------------------------------------------------------- |
| 1    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallSetValue.gif) | Set Value   | Message Present = 0        | Clear the Present flag of a Periodic message normally on the bus |
| 2    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallWaitFor.gif)  | Wait for    | 2 Second                   | Wait twice as long as normal periodic duration of the message    |
| 3    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallJump.gif)     | Jump If     | Message Present  To Step 1 | Jump to Step 1 if the message is present                         |
| 4    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallSleep.gif)    | Sleep       |                            | If not present, go into sleep mode                               |
| 5    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallJump.gif)     | Jump to     | Step 1                     | When device wakes up, go to step 1                               |

For more information on Function Block scripts see Vehicle Spy 3's help documentation. Sleep mode examples are included in the examples section for each neoECU device.

* [neoECU 10](neoecu-10/neoecu-10-examples.md)
* [neoECU 20](neoecu-20/neoecu-20-examples.md)
