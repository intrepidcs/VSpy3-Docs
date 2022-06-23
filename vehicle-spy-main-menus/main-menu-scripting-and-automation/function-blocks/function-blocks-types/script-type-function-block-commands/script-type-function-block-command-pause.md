# Script Type Function Block Command: Pause

### Command Description

This command stops the execution of the script and displays a popup window containing a message for the user. After reading the message, the user can choose to continue running the script or stop it.

### Value Field Parameters

Double-click in the **Value** cell for the command to launch the [Expression Builder](../../../../../shared-features-in-vehicle-spy/shared-features-expression-builder.md), which is where the message to be shown to the user is entered. The message must appear in the **Expression** field. Two common options here are:

* **Signal Value:** Choose a message signal or application signal and its value will be shown in the window.
* **Text String:** Enter a text string into the **Expression** field. If you choose this option, be sure to check **Evaluate as text**, located under the **Expression** text entry box.

Note that you can use simple HTML formatting in a text string, such as **\<b>** and **\</b>** to bold text, **\<u>** and **\</u>** to underline it, and **\<i>** and **\</i>** to show it in italics.

### Example

When the script in Figure 1 is run, it causes the window seen in Figure 2 to be displayed to the user. If the **Continue** button is pressed, the script will continue, transmitting **CAN Message A** and then stopping. If **Stop** is pressed, the script stops immediately and the message is not sent.

![Figure 1: Example script using the Pause command.](../../../../../.gitbook/assets/fb\_pause\_1.gif)

![Figure 1: Window displayed by Pause command.](../../../../../.gitbook/assets/fb\_pause\_2.gif)
