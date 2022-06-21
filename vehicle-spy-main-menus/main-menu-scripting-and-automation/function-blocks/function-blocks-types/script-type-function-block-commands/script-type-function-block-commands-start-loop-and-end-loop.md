# Script Type Function Block Commands: Start Loop and End Loop

### Overview

The **Start Loop** and **End Loop** commands are used to create loops, which are blocks of commands that are executed a specified number of times. The repetition count can either be a constant value, or one computed from an expression based on signal values and other data.

These commands must be entered in matched pairs, one **End Loop** for every **Start Loop**.

### Start Loop Command

Each loop begins with a **Start Loop** command. The **Value**field for this command specifies the number of times the loop will be repeated:

* **Constant Loop Counter:** After the **Start Loop**command is selected, a default value of **1** will appear in its **Value**column field. Change this to the number of times you want the loop to run.
* **Dynamic Loop Counter:** Edit the **Value** cell, then press the **=** key twice to launch the Expression Builder. Enter an expression, and the loop will run a number of times equal to the value that the expression returns.

When the script is run, the loop counter will be shown updating in real time in the **Value** cell of the **Start Loop** command; it decrements from the start value down to **1** as the loop proceeds. This progression may or may not be visible, depending on how quickly the loop executes.

**Note:** After selecting the **Start Loop** command, Vehicle Spy will display it in the script as **Start a loop**. These are equivalent.

### End Loop Command

The **End Loop** command marks the end of the loop. It has no parameters.

**Note:** After selecting the **End Loop** command, Vehicle Spy will display it in the script as **End the last loop**. These are equivalent.

### Examples

Here are two examples showing typical uses of loops.

### Loop with Constant Loop Counter

The example in Figure 1 shows a simple script that transmits a message exactly 7 times each time it runs.

![Figure 1: A simple loop with a constant loop counter.](../../../../../.gitbook/assets/fb\_loop\_1.gif)

### Loop with Expression-Derived Loop Counter

Figure 2 shows a script that waits for the receipt of a message called**CAN Control Message 1**. This message contains a signal, **Number of Transmissions**, which dictates how often the loop runs, and thus how often **CAN Message A** is transmitted.

![Figure 1: A loop with repetitions based on a signal value.](../../../../../.gitbook/assets/fb\_loop\_2.gif)
