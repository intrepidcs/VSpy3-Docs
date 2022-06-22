# Capture Type Function Block: Filter Tab

### Overview

The Filter Tab of a Capture Type Function Block allows you to set up filters that control which messages are captured when the block runs. There are two different ways to define filters for a capture block: either with custom message filters or using script-based filtering.\
\
This tab contains only two elements as shown in Figure 1.

![Figure 1: Capture Block Filter Tab.](../../../../../.gitbook/assets/capture\_block\_filter\_tab.png)

### Custom Message Filtering

To create custom message filters for the data capture, click the **Filters...** button. This will cause the Setup Filter dialog box to appear (the same one used to define custom filters in Messages View). Within the dialog box you can include and exclude messages from the capture. Note that if no message filters are selected, all messages are collected by default.\
\
This feature and script filtering (below) are mutually exclusive: only one may be used.

### Script Filtering

This is an advanced option for power users that provides complete control over exactly which messages are stored in the capture buffer, and under what circumstances. Instead of defining a filter using the standard Setup Filter dialog box, you use a Script Type Function Block in conjunction with a capture block to precisely determine which messages are saved.

### Setting Up Script Filtering

To use script filtering, follow these steps:

1. Check the **Disable Message Filters** box. This disables the standard filtering accessed through the **Filters...** button.
2. Set the rest of the parameters for the capture block the way you want them on the other tabs.
3. Create a script type function block.
4. In the function block script, use a **Set Value** command to instruct Vehicle Spy to save data to the capture block by choosing the correct parameters (see below).
5. Set up the rest of the function block with the correct logic to determine when you want this **Set Value** command executed.

Define the parameters for the **Set Value** command that captures data as follows:

* **Value to Set:** Click **Function Blocks** in the left-hand menu, then select the correct capture type block and double-click the **Script Filter Add Message** property.
* **Expression:** Select an expression that defines the data you want captured. A typical example might be to choose **Rx Messages** in the left-hand menu, select a receive message, then click the **Message Data** property and finally click the **Add to Expression** button.

Make sure the capture block is set to start automatically or include a command to start it via a Function Block Action command in the script, before any **Set Value** commands are executed.

### Script Filtering Examples

For both of these examples we will use a fairly simple capture block with the following major settings:

* **Start Type:** Immediately.
* **Stop and Trigger Options:** Collect in a one-shot buffer, with buffer size of 2,000 messages.
* **Storage:** Automatically save when complete.

The first example, shown in Figure 2, is a simple one showing how you can arbitrarily set conditions under which data is captured. It is designed to run a simulation containing **Engine and Vehicle Speed** messages. The function block script loops continuously since it has no Stop command. Each time, the loop waits for a new message, then checks the value of the **Engine Speed** signal; if it is over 1,000, it executes the **Set Value** statement in step 4 to save the message to the capture block. Once the capture block has received a total of 2,000 messages, it will automatically stop and save its data to the disk.\
\
Of course this is a very simple condition: we are just checking for a single signal value. You have complete flexibility to make the script as complex as required.

![Figure 2: Script Filtering example: saving only certain messages.](../../../../../.gitbook/assets/capture\_block\_script\_filtering\_1.gif)

The second example (Figure 3) shows how you can use script filtering to do sampling of incoming data. We have defined two application signals; **Number of Samples** and **Sample Rate**, both of which are pretty self-explanatory. The function block script runs in a loop controlled by the value of **Number of Samples**. It saves one message to the capture block, then waits for a number of milliseconds dictated by **Sample Rate** before looping. When the loop is done, the capture block data is saved and both blocks are stopped using script commands.

![Figure 3: Script Filtering example: sampling a message simulation stream.](../../../../../.gitbook/assets/capture\_block\_script\_filtering\_2.gif)
