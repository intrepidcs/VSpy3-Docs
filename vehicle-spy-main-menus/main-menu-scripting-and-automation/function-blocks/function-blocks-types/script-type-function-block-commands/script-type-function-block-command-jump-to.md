# Script Type Function Block Command: Jump To

### Command Description

This command unconditionally transfers execution of the current script to another step. It is similar to the **Jump If** command, except that the jump always happens, rather than being based on evaluating a condition.

Note that excessive use of **Jump To** and **Jump If** commands can make a script difficult to understand. Consider using an [If / Else / Else If / End If](script-type-function-block-commands-if-else-else-if-end-if.md) structure if possible, which can accomplish the same task while resulting in more readable code.

### Value Field Parameters

This command has a special interface that appears upon double-clicking the **Value** column, to make it easier for you to select a particular command to jump to. The current step number is shown in the field, and the selected step's number and description are also highlighted in a magenta box.

You can change the jump target in several ways:

* Type a new number into the field.
* Press the up or down arrows to increment or decrement the value.
* Use the up or down keys on your keyboard to increment or decrement the value.

As you change the value, the magenta box will move accordingly. Press the **Enter** key to finalize your selection.

![Figure 1: Selecting a destination step for the Jump To command.](../../../../../.gitbook/assets/fb\_jump\_to.gif)
