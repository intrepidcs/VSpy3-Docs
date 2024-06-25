# Script Type Function Block Command: Load Message Data

### Command Description

This command loads byte data from a file into a [transmit message](../../../../main-menu-spy-networks/message-editor/messages-editor-receive-transmit-and-database-tables.md). You can use it to set the contents of a message before sending it out.

### Value Field Parameters

Double-click in the **Value** field to launch this command's parameter dialog box (Figure 1). There are several settings here.

![Figure 1: Parameter setup for the Load Message Datacommand.](../../../../../.gitbook/assets/fb\_load\_message\_data.gif)

### Start Index

The value of the first byte of data in the file to load. This is specified as an [application signal](../../../application-signals/) (**Message Data Start Value** in our example in Figure 1) that should be declared ahead of time and set to the correct figure.

### Length

The length of the data, in bytes, to load from the file. Again this is specified not directly but rather through an application signal (**Data Length** in Figure 1).

### Filename without extension (\*.msgbin)

This is the name of the actual file from which to load data. The file must have a **.msgbin** extension and be located in the [data directory](../../../../../basic-operation-of-vehicle-spy/data-directory.md) of the current user.

### Fast load data

When this optional setting is checked, data will be stored in flash memory, if possible, instead of RAM. This frees up more RAM for other purposes.

### Transmit Message

The transmit message to receive the data:

* **Message:** The actual transmit message, selected through a drop-down box (this is **Outgoing Data Transmission** in Figure 1).
* **Byte Start Index:** Specifies the first byte of the transmit message into which data should be loaded.
