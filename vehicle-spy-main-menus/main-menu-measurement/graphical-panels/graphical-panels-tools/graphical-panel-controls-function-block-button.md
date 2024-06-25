# Graphical Panel Controls: Function Block Button

The Function Block button provides the ability to control [Function Block](../../../main-menu-scripting-and-automation/function-blocks/) scripts from a graphical panel. Function blocks can be started, stopped, triggered ([capture-type function blocks only](../../../../vehicle-spy-tutorials/tutorial-sort-messages-by-ecu/part-3-setup-capture-type-function-blocks.md)), or instructed to save their collected data (again, capture blocks only).

![Figure 1: An example Function Block control.](../../../../.gitbook/assets/gpctrlFBButton.gif)

Table 1 lists the special properties associated with Function Block controls. A list of common properties can be found under [Common Control Properties](graphical-panel-controls-common-control-properties.md).

**Table 1: Function Block Control Properties**

| Property      | Function and Options                                                                                                                                                                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OnText        | The text shown when the button is pushed in or held down (**On** state).                                                                                                                                                                                                    |
| OffText       | The text string shown when the button is up (**Off** state).                                                                                                                                                                                                                |
| FBlockAction  | <p>Sets the action to be taken by the function block when the button is pressed:</p><ul><li><strong>0-Start</strong></li><li><strong>1-Trigger</strong></li><li><strong>2-Stop</strong> (capture block only)</li><li><strong>3-Save</strong> (capture block only)</li></ul> |
| FunctionBlock | The function block associated with this control; clicking in this field will cause a list of all available function blocks in the setup to be presented in a drop-down box.                                                                                                 |
