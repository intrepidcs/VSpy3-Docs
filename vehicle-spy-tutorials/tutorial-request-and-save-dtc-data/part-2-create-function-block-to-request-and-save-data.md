# Part 2 - Create Function Block to Request and Save Data

### 1. Open Function Blocks View:

From the main menu select **Scripting and Automation> Function Blocks**.

### 2. Create a Function Block:

Click the **+ button** and select **Script** to create a new Script type function block. Change the description of the function block to something more descriptive like **Check Codes and Log Them to a File**.

### 3. Write the Script:

Now a script needs to be entered. For this task 4 steps will be needed (Table 1). For **Diag Job Action** double clicking on the **Value** cell will allow selection of the diagnostic job to act on and how to act on it. For more information on this command see the help for the [Diag Job Action command](../../vehicle-spy-main-menus/main-menu-scripting-and-automation/function-blocks/function-blocks-types/script-type-function-block-commands/script-type-function-block-command-diag-job-action.md).

**Table 1: Script function block steps.**



<table><thead><tr><th width="150">Step</th><th width="150">Command</th><th>Value</th><th>Reason for Step</th></tr></thead><tbody><tr><td>1</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/spyfbicodiagJobAct.jpg" alt=""> Diag Job Action</td><td><strong>Start</strong> Request DTCs from all nodes</td><td>Starts, or launches, the diagnostic service.</td></tr><tr><td>2</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/spyfbicodiagJobAct.jpg" alt=""> Diag Job Action</td><td><strong>Wait until</strong> Complete Request DTCs from all nodes</td><td>Waits at this step until the selected diagnostic service is finished.  When completed, continues to the next step.</td></tr><tr><td>3</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/spyfbicodiagJobAct.jpg" alt=""> Diag Job Action</td><td><strong>Save</strong> Request DTCs from all nodes</td><td>Saves the received data and message traffic to a log file.</td></tr><tr><td>4</td><td><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/spyfbicostop.jpg" alt=""> Stop</td><td>n/a</td><td>Ends this function block.</td></tr></tbody></table>

### Configure the Start Setting:

On the **Start** tab select **Manual Start**. This allows the Script function block to be started using Graphical Panel controls that will be set up in the next part of this tutorial.
