# Part 2 - Create Function Block to Launch Programming Services

### 1. Open Function Blocks View:

The next step is to create a function block to control the diagnostic services created. Open the Function Blocks view selecting **Scripting and Automation> Function Blocks**from the main menu.

### 2. Create a Script Function Block:

Click the **+ button** and select **Script**. Change the description of the function block to something more descriptive like **Program ECUs**.

### 3. Write the Script:

Now a script needs to be entered. For this task 6 steps will be needed. The steps needed and descriptions of what they do are found in the **Table 1**. For the **Diag Job Action**, double clicking on the **Value** cell will allow selection of the diagnostic job to act on and how to act on it. For more information on this command see the help for the [Diag Job Action command](../../vehicle-spy-main-menus/main-menu-scripting-and-automation/function-blocks/function-blocks-types/script-type-function-block-commands/script-type-function-block-command-diag-job-action.md).

**Table 1: Function block parameters**



<table><thead><tr><th width="150">Step</th><th width="150">Command</th><th width="150">Value</th><th>Reason for Step</th></tr></thead><tbody><tr><td>1</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/Disgnosticssm.gif" alt="">Diag Job Action</td><td>Start DW CAN ECU</td><td>Starts, or launches, the diagnostic service.</td></tr><tr><td>2</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/Disgnosticssm.gif" alt="">Diag Job Action</td><td>Wait until Complete DW CAN ECU</td><td>Waits at this step until the selected diagnostic service is finished.  When completed, continues to the next step.</td></tr><tr><td>3</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/WaitClocksm.gif" alt="">Wait For</td><td>5.000 Sec</td><td>Waits for 5 seconds.  This is not needed, but provides a delay so script progress can be monitored by the user.</td></tr><tr><td>4</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/Disgnosticssm.gif" alt="">Diag Job Action</td><td>Start SW CAN ECU</td><td>Starts, or launches, the diagnostic Service.</td></tr><tr><td>5</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/Disgnosticssm.gif" alt="">Diag Job Action</td><td>Wait until Complete SW CAN ECU</td><td>Waits at this step until the selected diagnostic service is finished.  When completed, continues to the next step.</td></tr><tr><td>6</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/Stopsm.gif" alt="">Stop</td><td>n/a</td><td>Ends this function block.</td></tr></tbody></table>



### 4. Configure the Start Setting:

On the **Start** tab select **Manual Start**. This allows the Script function block to be started using Graphical Panel controls that will be set up in the next part of this tutorial.
