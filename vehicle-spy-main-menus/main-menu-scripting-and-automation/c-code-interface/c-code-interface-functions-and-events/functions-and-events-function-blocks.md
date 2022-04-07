# Functions and Events: Function Blocks

The C Code Interface provides functions for interacting with Vehicle Spy Function Blocks.  Function blocks can capture message data to a file, replay messages or execute a script. Therefore your C code has high level control over this powerful part of Vehicle Spy. You can start, stop, trigger or save data related to function blocks directly from C.\
\
All function block related functions begin with the prefix "FB\_". The function then contains the function block name and finishes with the API name. For example, if a function block was named "Test", the function to start it would be "FB\_Test\_Start()". See the table and picture below for more details.

**Table 1: Function Block APIs Available**

| API            | Description                                                     |
| -------------- | --------------------------------------------------------------- |
| IsRunning()    | Returns 1 if the function block is running.                     |
| IsTriggered()  | Returns 1 if the function block is triggered.                   |
| NumCollected() | Returns the number of messages collected by the function block. |
| Save()         | Saves the function block data.                                  |
| Start()        | Starts the function block.                                      |
| Stop()         | Stops the function block.                                       |
| Trigger()      | Triggers the function block.                                    |

![Figure 1: The C code project has full control of Vehicle Spy's function blocks - just type "FB\_".](../../../../.gitbook/assets/fblock\_control.gif)
