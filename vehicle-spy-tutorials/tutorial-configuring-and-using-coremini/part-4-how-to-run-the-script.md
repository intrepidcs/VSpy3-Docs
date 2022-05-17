# Part 4 - How to Run the Script

### 1. Running the CoreMini:

If the "Run CoreMini After Download"checkbox was checked, then the script will be running after the send button was clicked. Unless the script created changes the default blinking pattern, the red LED should be blinking. This lets you know that the script is running.

### 2. Controlling the Script:

Scripts can be ran or not ran depending on how the unit is powered. Table 1 shows the connection order and how the device will react to this connection.

**Table 1: Connection Order Effects on Device Mode and LED Pattern**

| Connection Order | Device Mode                                                                                                                          | Default LED Pattern   |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| Power only       | CoreMini Stand-alone mode, Device runs internal script if present.                                                                   | Blinking Red          |
| USB then Power   | PC mode, CoreMini will not be ran.                                                                                                   | Blinking Green        |
| Power then USB   | CoreMini Stand-alone mode, Device runs internal script if present. Device can also be used with the PC to monitor or do other tasks. | Alternating Red Green |



### 3. Get data:

Connect the hardware to vehicle data running the script to collect data.
