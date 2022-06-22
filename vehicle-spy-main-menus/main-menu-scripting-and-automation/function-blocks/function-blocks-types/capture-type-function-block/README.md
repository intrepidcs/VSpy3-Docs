# Capture Type Function Block

### Overview

Capture type function blocks (commonly refered to as _capture blocks_) allow the ability to catch data as it comes over the network and save it to a buffer file for future analysis. A host of options and parameters split across multiple tabs allow the function block to be tailored to any use case. These blocks allow anything from a simple manual capture of a small amount of data, to sophisticated setups that record precise message sets based on custom filtering and trigger logic.

### Applications

Table 1 describes just a few of the many ways that capture blocks can be used. In each case the application is described and a brief summary is provided of the capture block settings that might be used in a setup; these are presented in the same order that capture block tabs appear. Of course these are only samples and settings can be combined in almost any way that is required.

**Table 1: Sample applications of capture type function blocks**

****

| Application Description                                                                                  | Buffer                 | Start Type           | Stop and Trigger Options                                                                       | Storage                          |
| -------------------------------------------------------------------------------------------------------- | ---------------------- | -------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------- |
| Save current data in a large, unfiltered buffer, possibly triggered by a hotkey.                         | No filtering           | Start Immediately    | Collect in a circular buffer, with large buffer                                                | Manual save                      |
| Save a new buffer file at a periodic rate. (Warning: This can fill up storage if set up incorrectly!)    | No filtering           | Start Immediately    | Collect in a circular buffer, with very large buffer                                           | Save when expression is true     |
| Create a small, filtered buffer file, triggered by a joystick button.                                    | Filtering              | Manual Start         | Collect in a one-shot buffer, with small buffer                                                | Automatically save when complete |
| Capture data before and after a hotkey click.                                                            | Filtering              | Start Immediately    | Collect before and after a manual trigger, with small buffer and large post-trigger buffer     | Automatically save when complete |
| Store a large amount of data before an event that occurs very quickly.                                   | No filtering           | Start Immediately    | Collect before and after a trigger expression, with large buffer and small post-trigger buffer | Automatically save when complete |
| Capture data that occurs between two events.                                                             | Filtering              | Use Start Expression | Collect in a circular buffer, with large buffer                                                | Save when expression is true     |
| Capture data filtered using a script, with start, trigger and save expressions for ultimate flexibility. | Filtering using script | Use Start Expression | Collect before and after a trigger expression, with mid-sized buffer and post-trigger buffer   | Save when expression is true     |

### Creating a Capture Block

Create a new capture block by clicking the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_add.gif) button on the far left of the function block toolbar and then select **Capture** from the popup menu. Vehicle Spy will create a default capture block as shown in Figure 1, with the **Filter Tab** selected.

![Figure 1: Default capture block setup.](../../../../../.gitbook/assets/capture\_block\_default.png)

### Renaming a Capture Block

Like all function blocks, a new capture block will appear in the function block list near the top of the function block pane. The function blocks can be renamed by double-clicking on the default name (**Function Block 1**) and entering a more descriptive name.

The name entered in the function block list also appears in blue in the function block setup area for greater clarity.

### Capture Block Tabs

As shown in Figure 1, capture type function blocks have their parameters divided into five tabs. The following is a brief description of these tabs with links to pages covering each in more detail:

* Filter Tab: Allows you to specify filters to restrict which messages are captured by the block.
* Start Tab: This tab is common to all function block types and allows you to specify the block's Start Type and related options.
* Stop and Trigger: In this tab you tell Vehicle Spy how much data to capture and how to capture it.
* Storage: Here you decide when to save the captured data and what formats and options to use.
* Data: This is a read-only tab where you can view messages as they are being captured.
