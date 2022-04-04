# Message Capture Method: Stop Options

When using the Message Capture method for Standalone Logging within VehicleScape DAQ, the choice of Start Option determines the Stop Option choices that appear. Table 1 summarizes the three options, shows the Start Options that each is associated with, and contains links to detailed help pages for all three.

**Table 1: Stop Options for the Message Capture Method**

| Stop Option                                                                    | Description                                                                                                                                               | Associated Start Options                                                                       |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| <p>Finish after collecting # messages<br>or Finish when expression is true</p> | Stop logging after a certain number of messages are logged, or when an expression evaluates as true.                                                      | <p><strong>Start immediately</strong><br>or <strong>Start when expression is true</strong></p> |
| Pre/Post Collection                                                            | Log data before and after the Collection Start trigger. The capture window can be defined using an expression, a length of time, or a number of messages. | **Start using trigger expression**                                                             |
| One-shot Report                                                                | Log a snapshot of data values after waiting a configurable amount of time after the Collection Start trigger.                                             | **Start using trigger expression**                                                             |

**Note:** The **One-shot Report** stop option is also used by the Bus Query method.
