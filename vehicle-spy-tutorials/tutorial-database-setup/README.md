# Tutorial: Database Setup

### Overview

As seen in the previous tutorials, Vehicle Spy 3 can bring in raw message data. Using the [Receive table](../../vehicle-spy-main-menus/main-menu-spy-networks/message-editor/messages-editor-receive-transmit-and-database-tables.md) of the [Messages Editor](../../vehicle-spy-main-menus/main-menu-spy-networks/message-editor/messages-editor-receive-transmit-and-database-tables.md), message decoding tables can be created. If a database is available, this information can be imported saving time by not requiring this information typed in by a user. In this tutorial, platform creation and database loading will be covered.

### Parts of Vehicle Spy used

[Network Database View](../../vehicle-spy-main-menus/main-menu-setup/network-databases.md)\
[ECU Diagnostic Database View](../../vehicle-spy-main-menus/main-menu-setup/ecus-view/)

### Hardware needed

**neoVI FIRE 2, ValueCAN 4 family, RAD-Gigastar, RAD-Mars etc.** Please note that this feature is currently not supported on **neoVI FIRE 3** and **neoVI RED2**; however, a future update will include support for these devices.

### Files for this example

[MadeUpDatabase.dbc](https://cdn.intrepidcs.net/support/VehicleSpy/MadeUpDatabase.dbc) - Made up database file for use with "All Bus Traffic.csv" replay file that can be used with this tutorial.\
[MadeUpDiagnosticFile.odx](https://cdn.intrepidcs.net/support/VehicleSpy/MadeUpDiagnosticFile.odx) - Made up diagnostic database that can be used with this tutorial.
