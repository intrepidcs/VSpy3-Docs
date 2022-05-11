# Graphical Panel Controls: Common Control Properties

Table 1 contains descriptions of the common properties found in most Graphical Panel controls.

**Table 1: Common Control Properties**

| Property    | Function and Options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Width       | Sets the width of the control in pixels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Top         | Sets the distance of the control, in pixels, from the top edge of the panel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Left        | Sets the distance of the control, in pixels, from the left edge of the panel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Height      | Sets the height of the control, in pixels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ForeColor   | Sets the foreground color of the control.  For most controls, this is equal to the text color.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| BackColor   | Specifies the background color of the control.  To change this color, make sure the **Transparent** property is set to "Opaque".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Transparent | <p>Specifies whether the control should use the <strong>BackColor</strong> property or the form's background color:</p><ul><li><strong>0-Opaque:</strong> Use <strong>BackColor</strong> property.</li><li><strong>1-Transparent:</strong> Show the panel's background color.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| BorderStyle | <p>Sets the type of border around the control:</p><ul><li><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/gpLLEDNone.gif" alt=""> <strong>0-None</strong></li><li><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/gpLLEDSunk.gif" alt=""> <strong>1-Sunken</strong></li><li><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/gpLLEDRaised.gif" alt=""> <strong>2-Raised</strong></li><li><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/gpLLEDRim.gif" alt=""> <strong>3-Rimmed</strong></li><li><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/gpLLEDEmbos.gif" alt=""> <strong>4-Embossed</strong></li><li><img src="https://cdn.intrepidcs.net/support/VehicleSpy/assets/gpLLEDSimple.gif" alt=""> <strong>6-Simple</strong></li></ul><p>(An additional value, <strong>5-GroupBox</strong>, is defined for the Text Display control.)</p> |
| Font        | Sets the font family, style and size for the control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Tag         | Sets an identifier for advanced scripts.  In most cases this can be left blank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Enabled     | <p>Specifies whether or not the control can be interacted with on the panel:</p><ul><li><strong>0-No</strong></li><li><strong>1-Yes</strong></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Caption     | Text to display for the control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ShowCaption | <p>Specifies whether or not the caption is visible.</p><ul><li><strong>0-No</strong></li><li><strong>1-Yes</strong></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Alignment   | <p>Sets the horizontal alignment of text or caption in a control:</p><ul><li><strong>0-Left</strong></li><li><strong>1-Right</strong></li><li><strong>2-Center</strong></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Signal      | When double-clicked, the Expression Builder is displayed so a signal can be associated with the control. (This property is present for most controls, though not all.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Minimum     | Sets the smallest value the control will accept as input or display as output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Maximum     | Sets the largest value the control will accept as input or display as output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |