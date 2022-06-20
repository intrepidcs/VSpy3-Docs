# Script Type Function Block

### Overview

Script type function blocks (also commonly called _function block scripts_) allow you to create custom programs in Vehicle Spy. The script is a list of steps for Vehicle Spy to perform; you can think of it as being like a recipe, listing what you want to happen, in a specific sequence, with specific "ingredients" (parameters).

You choose from a set of commands for each step, including commands to transmit messages, wait for events such as the receipt of messages, change internal variables, and control the operation of the script itself.

To help with more complex scripts, Vehicle Spy provides debugging features to help you find and eliminate problems.

### Applications

Potential uses for script function blocks include simulation, diagnostics and automated testing.

### Creating a Function Block Script

Scripts are created in the Function Blocks view by clicking the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_add.gif) button on the far left of the function block toolbar, and then choosing **Script** from the popup menu. Vehicle Spy will create a default function block script for you as shown in Figure 1.

![Figure 1: Default function block script setup.](../../../../.gitbook/assets/script\_default.gif)

### Renaming a Function Block Script

Creating a function block script will cause it to appear in the function block list near the top of the function blocks area (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)). You can rename the function block by double-clicking on the default (**Function Block 1** here) and adding a more descriptive name. This is especially important in complex setups that use multiple function blocks.

The name entered in the function block list also appears in blue in the function block setup area for greater clarity (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)).

### Script Tab

Script commands, parameters and descriptions are entered in the **Script Tab**, which is shown by default. A script type function block also has a Start Tab, like all function blocks (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)).

Below the tabs is a toolbar that contains commands for working with scripts (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFour.gif)). The toolbar also shows an indicator of the error status of the script (saying at present **No Errors**).

### Script Grid

Most of the setup area for a script type function block consists of a spreadsheet-like grid where command steps are entered (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFive.gif)).

Each new script begins with ten steps, one of which contains a default prompt comment, with the others blank. You can make larger scripts by adding new script steps using the toolbar. There is no predefined limit to the size of a script.

Blank steps are skipped with no effect, but you can remove them for clarity if you wish. The toolbar will also let you rearrange steps in the grid if necessary.

### Script Grid Columns

There are four columns in the setup area for a function block script (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smSix.gif)):

* **Step:** The step number for the command. Steps are always shown in numerical order.
* **Description:** The description of the command, which is actually a code word for the command itself. Double-click in this column for a particular step to choose from the available script commands.
* **Value:** Parameters for the selected command. Double-clicking here allows the selection of parameters for the command, which will be shown in the field after they are chosen. The entry in the **Value** column depends on the command, and may be blank if no parameters are required.
* **Comment:** Documentation of the step's function or purpose. This is only for reference and does not impact script operation.

You can drag the dividers between the columns to change their size.

Note that there is also an additional column to the left of **Step**that is used for monitoring and debugging scripts.

### Script Operation and Example

When Vehicle Spy goes online, it will begin running the script based on the Start Type selected for it. Normally each step will be executed in sequence, but certain commands (such as theIf / Else / Else If / End If complex, or Jump To) can alter the flow of the script, possibly based on message or signal values.

Scripts loop automatically by default; when the last step is executed, the script will begin running again. If this behavior is not desired, a script can be terminated using the Stop command.

If you have defined multiple function block scripts, each runs independently of the other, with the status of each script shown in the Function Block List.

A thin colored line to the left of the step numbers (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smSeven.gif)) indicates which steps have been edited (green) or have been run (red).

As an example, Figure 2 shows a script that waits for a certain signal value, transmits a message, clears stats, and then repeats.

![Figure 2: Simple example of a script type function block.](../../../../.gitbook/assets/script\_example.gif)
