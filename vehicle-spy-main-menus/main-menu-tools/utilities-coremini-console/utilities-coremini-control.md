# Utilities: CoreMini Control

How CoreMini scripts run depends on how the device is powered. Table 1 shows the connection order and how the device will start.

**Table 1: CoreMini Console Control**

| Connection Order | Device Mode                                                                                                                         | Default LED Pattern   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Power only       | CoreMini Stand-alone mode, Device runs internal script if present                                                                   | Blinking Red          |
| USB then Power   | PC mode, CoreMini will not be ran                                                                                                   | Blinking Green        |
| Power then USB   | CoreMini Stand-alone mode, Device runs internal script if present. Device can also be used with the PC to monitor or do other tasks | Alternating Red Green |
