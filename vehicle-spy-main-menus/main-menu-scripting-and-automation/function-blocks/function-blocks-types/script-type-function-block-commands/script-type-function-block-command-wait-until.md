# Script Type Function Block Command: Wait Until

### Command Description

This command causes the function block script to wait until a specified condition evaluates as **True**, or optionally, until a maximum wait time has been reached.

### Value Field Parameters

Double-click the **Value** field to bring up the dialog box shown in Figure 1.

![Figure 1: Wait Until command parameter dialog box.](../../../../../.gitbook/assets/fb\_wait\_until.gif)

### Expression

Press the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/Functionbutton.gif) button to launch the [Expression Builder](../../../../../shared-features-in-vehicle-spy/shared-features-expression-builder.md), where you can craft the expression to be used for this command.

Any conditional expression can be entered. For example, you can have a script wait until a particular signal value is seen in a specific message. Message properties are also commonly used here, such as the **Present** flag, as we'll see in the example below.

### Timeout in seconds / Use Timeout

In some situations an expression in a **Wait Until** command may never evaluate as **True**, or it may take more time than is desired. To limit how long the script waits in a particular step, you can specify a _timeout_ value in seconds. Vehicle Spy will wait for the selected expression to evaluate as **True**, but only up to a maximum of the specified timeout interval. If that figure is exceeded, then the script will continue despite the expression being **False**.

To use this feature, enter a length of time in the **Timeout in seconds** box, and check the **Use Timeout** box. If the box is not checked, the **Timeout in seconds** value will be ignored, and the script will only continue if the expression evaluates as **True**.

### Example

Figure 1 shows a typical use of the **Wait Until** command: pausing a script until the arrival of a particular message before proceeding, by waiting for its **Present** flag to be set to **True** by Vehicle Spy. Notice that step 2 [resets the Present flag](../script-type-function-block-resetting-the-present-flag.md), which ensures that steps 3 and 4 only occur once for each copy of **Incoming Message** that arrives.

![Figure 1: Example using the Wait Until and Wait For commands.](../../../../../.gitbook/assets/fb\_wait\_for.gif)
