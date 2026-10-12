# Transmit Panel

The Tx Panel lists all transmit messages defined in Vehicle Spy. In fact, as you add transmit messages to the Message Editor, they are automatically added to the Tx Panel.

The Tx Panel has two tabs. The **Messages** tab, described on this page, lists transmit messages. The **PDUs** tab transmits PDUs from the network database; see [PDU Transmitters](pdu-transmit-object.md).

The **Protocol** dropdown at the top of the Messages tab shows only the transmit messages of the selected protocol, with the columns that suit that protocol. Select **All** to show every transmit message. While Vehicle Spy is running, press **Disable All Tx** to stop all transmission from Vehicle Spy, including [PDU transmitters](pdu-transmit-object.md), and press it again to resume. The button has no effect while Vehicle Spy is offline.

The Tx Panel is where manual or periodic message transmission is setup. Simply use the dropdowns to the right of the message description (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smOne.gif)) to make selections. A small gray button (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smTwo.gif)) is included to manually send messages.

The right half of the Tx Panel (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smThree.gif)) displays signals associated with each transmit message as defined in the [Messages Editor](../message-editor/messages-editor-overview.md). Select or enter in the desired value for each signal (On/Off, True/False, Park, Reverse, Neutral, 1000, 5053, etc.) and Vehicle Spy will display the proper raw value. The **In** and **Dc** buttons (Figure 1:![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/smFour.gif)) will increment or decrement analog values by the set step size. The **Sg** button applies a predefined waveform to the signal; see [Dynamic Transmit Message Bytes](dynamic-transmit-message-bytes.md). This makes it quick and easy to change values. Send your message and watch Messages view closely. You will see the raw value encoded in the message's data bytes.

![Figure 1: The Transmit Panel.](../../../.gitbook/assets/spytransmitpanel.png)

There is a Fill Up/Down feature on the right click menu while over the left side of the Tx Panel. This feature will fill all selected cells in a column with the same value as the first selected cell. To use the feature, select the cell to copy, then **Shift + left click** to highlight the range of cells to change, then right click and apply the **Fill Up/Down** feature as seen in **Figure 2**.

![Figure 2: Fill Down, from the Fill Up/Down feature.](../../../.gitbook/assets/spytransmitpanel2.png)

Please check the following video for more details.

{% embed url="https://youtu.be/7I4OWfbAfY0?feature=shared" %}

