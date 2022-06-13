# Message Capture Method: Stop Options: One Shot Report

When using the [Message Capture](../collections-and-methods-message-capture-method/) method for [Standalone Logging](../../) within VehicleScape DAQ, selecting **Using Trigger Expression** for the [Collection Start Option](../collections-and-methods-message-capture-method/message-capture-method-start-options.md) causes the [Collection Configuration](./) to consist of two options: [Pre/Post Collection](message-capture-method-stop-options-pre-post-collection.md) and One-shot Report (described here). The One-shot Report is also used for the [Bus Query](../collections-and-methods-bus-query-method.md) method.

Figure 1 shows the appearance of the Stop Options subsection of the Standalone Logging tab when **One-shot Report** is selected.

![Figure 1: The One-shot Report Collection Configuration.](../../../../../../.gitbook/assets/spyvssalcollectconfigoneshot.gif)

### After trigger delay

This entry specifies how long the logger should wait after the trigger event to log the data snapshot. If set to 0, the one-shot report occurs immediately.

### Record time

How much time the logger should spend capturing bus messages.
