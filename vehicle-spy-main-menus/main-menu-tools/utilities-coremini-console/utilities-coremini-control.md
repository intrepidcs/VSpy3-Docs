# Utilities: CoreMini Control

How CoreMini scripts run depends on how the device is powered. Table 1 shows the connection order and how the device will start.

**Table 1: CoreMini Console Control**

<table><thead><tr><th width="150">Connection Order</th><th>Device Mode</th><th>Default LED Pattern</th></tr></thead><tbody><tr><td>Power only</td><td>CoreMini Stand-alone mode, Device runs internal script if present</td><td>Blinking Red</td></tr><tr><td>USB then Power</td><td>PC mode, CoreMini will not be ran</td><td>Blinking Green</td></tr><tr><td>Power then USB</td><td>CoreMini Stand-alone mode, Device runs internal script if present. Device can also be used with the PC to monitor or do other tasks</td><td>Alternating Red Green</td></tr></tbody></table>
