# Part 2 - Create Function Block to Request and Save Data

### 1. Open Function Blocks View:

From the main menu select **Scripting and Automation> Function Blocks**.

### 2. Create a Function Block:

Click the **+ button** and select **Script** to create a new Script type function block. Change the description of the function block to something more descriptive like **Check Codes and Log Them to a File**.

### 3. Write the Script:

Now a script needs to be entered. For this task 4 steps will be needed (Table 1). For **Diag Job Action** double clicking on the **Value** cell will allow selection of the diagnostic job to act on and how to act on it. For more information on this command see the help for the Diag Job Action command.

**Table 1: Script function block steps.**

****

| Step | Command                                                                                          | Value                                               | Reason for Step                                                                                                    |
| ---- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spyfbicodiagJobAct.jpg) Diag Job Action | **Start** Request DTCs from all nodes               | Starts, or launches, the diagnostic service.                                                                       |
| 2    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spyfbicodiagJobAct.jpg) Diag Job Action | **Wait until** Complete Request DTCs from all nodes | Waits at this step until the selected diagnostic service is finished.  When completed, continues to the next step. |
| 3    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spyfbicodiagJobAct.jpg) Diag Job Action | **Save** Request DTCs from all nodes                | Saves the received data and message traffic to a log file.                                                         |
| 4    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/spyfbicostop.jpg) Stop                  | n/a                                                 | Ends this function block.                                                                                          |

### Configure the Start Setting:

On the **Start** tab select **Manual Start**. This allows the Script function block to be started using Graphical Panel controls that will be set up in the next part of this tutorial.
