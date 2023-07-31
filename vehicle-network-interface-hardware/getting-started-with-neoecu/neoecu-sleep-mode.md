# neoECU Sleep Mode

neoECU devices also have a sleep mode.  Sleep mode can be enabled in [Function Block](../../vehicle-spy-main-menus/main-menu-scripting-and-automation/function-blocks/) scripts using the [Sleep](../../vehicle-spy-main-menus/main-menu-scripting-and-automation/function-blocks/function-blocks-types/script-type-function-block-commands/script-type-function-block-command-sleep.md) step command. Table 1 gives an example [Function Block](../../vehicle-spy-main-menus/main-menu-scripting-and-automation/function-blocks/) script to enable sleep mode. This script works by checking the present status of a message. If the message is not received when it is expected, the device will go to sleep.  When normal traffic is received again, the neoECU will wakeup again.

**Table 1: Example Function Block for enabling sleep mode**

<table><thead><tr><th width="150">Step</th><th width="150"></th><th width="150">Description</th><th width="150">Value</th><th>Comment</th></tr></thead><tbody><tr><td>1</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallSetValue.gif" alt=""></td><td>Set Value</td><td>Message Present = 0</td><td>Clear the Present flag of a Periodic message normally on the bus</td></tr><tr><td>2</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallWaitFor.gif" alt=""></td><td>Wait for</td><td>2 Second</td><td>Wait twice as long as normal periodic duration of the message</td></tr><tr><td>3</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallJump.gif" alt=""></td><td>Jump If</td><td>Message Present  To Step 1</td><td>Jump to Step 1 if the message is present</td></tr><tr><td>4</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallSleep.gif" alt=""></td><td>Sleep</td><td> </td><td>If not present, go into sleep mode</td></tr><tr><td>5</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/smallJump.gif" alt=""></td><td>Jump to</td><td>Step 1</td><td>When device wakes up, go to step 1</td></tr></tbody></table>

For more information on Function Block scripts see Vehicle Spy 3's help documentation. Sleep mode examples are included in the examples section for each neoECU device.

* [neoECU 10](neoecu-10/neoecu-10-examples.md)
* [neoECU 20](neoecu-20/neoecu-20-examples.md)
