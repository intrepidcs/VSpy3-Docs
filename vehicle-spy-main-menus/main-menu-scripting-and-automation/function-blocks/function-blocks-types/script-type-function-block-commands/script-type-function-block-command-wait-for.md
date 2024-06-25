# Script Type Function Block Command: Wait For

### Command Description

This command causes the function block script to wait for a period of time before continuing to the next step.

### Value Field Parameters

The **Value** field indicates how long the script should wait, in seconds. It can be specified in two ways:

* **Static Wait Time:** After the **Wait For** command is selected, a default value of 0.001 seconds (1 millisecond) will appear by default in the **Value** column field. Double-click the field and change the figure to however long you want the script to wait.
* **Dynamic Wait Time:** Double-click the **Value** cell, then press the **=** key twice to launch the [Expression Builder](../../../../../shared-features-in-vehicle-spy/shared-features-expression-builder.md). The script will wait for a number of seconds equal to the value returned by the defined expression.

### Example

Figure 1 shows an example of a function block script using a dynamic **Wait For**command (and a [Wait Until](script-type-function-block-command-wait-until.md) command as well). The script waits for receipt of an incoming message, then uses the value in a signal it contains to dictate how long to wait before sending an outgoing message. The script then repeats the process the next time the incoming message arrives.

![Figure 1: Example using the Wait For and Wait Until commands.](../../../../../.gitbook/assets/fb\_wait\_for.gif)
