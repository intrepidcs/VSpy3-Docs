# Message Signal Type State Encoded

Setup a state encoded signal by setting the [Signal Type](https://cdn.intrepidcs.net/support/VehicleSpy/spyInValType.htm) pulldown to **State Encoded** in the Edit Signal dialog (Figure 1).

![Figure 1: Use the Edit Signal dialog to equate states with signal values.](../../../../.gitbook/assets/spyindecodestates.gif)

Specifying the Raw Value is the same as the analog signal setup. Please see the [analog signal](https://cdn.intrepidcs.net/support/VehicleSpy/spyInDecodeAnalog.htm) help topic for an explanation of how to do this.

Use the state table area to enter a State Description and the decimal Raw Value it represents. Click the **Add** button to add the state definition to the States list. Additional state definitions can be entered quickly by just typing new State Descriptions and tapping the keyboard Enter key. Vehicle Spy will automatically increment the Raw Value field by 1 to help speed things up. Edit the Raw Value field at any time if some values need to be skipped.

To delete a state definition from the list, click the state name then click the **Remove** button.

Any raw values without state definitions are considered to be unused states. Vehicle Spy normally shows unused states with the text **Invalid State**. To show unused states as numerical values, click the **Treat unused states as analog data** checkbox. This will activate the Scaling tab and the Format, Min, Max, and Units fields just like the setup for analog signals. These settings will be applied to any unused values and displayed accordingly.

------------------------
![Figure 2: Use the Add Linear Formula to recalculate the range values.](../../../../.gitbook/assets/addlinearformula.gif)

By clicking the "Equation" button, you can open the Add Linear Formula menu. In this window, it is also possible to define a range and set the calculation to be performed using the equation applied to that range.

For example, you can map the signal value of 0 ~ 200 to 1.0 ~ 5.0 by setting (a) Start Raw Value 0, (b) End Raw Value, (c) m (scaling factor) 0.02, (d) b (scaling offset) 1.0.  When the data is received, it is calculated as `"Raw Value" * m + b`.  <br>
As in the example above, when applied with m = 0.02 and d = 1.0, signal data values of 0, 10, 50, and 100 are translated into 1, 1.2, 2, and 3, respectively.