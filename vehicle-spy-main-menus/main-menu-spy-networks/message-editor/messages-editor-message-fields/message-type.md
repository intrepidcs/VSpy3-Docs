# Message Type

The message **Type** field in the Messages Editor has different meanings for the CAN versus LIN networks.

### CAN - Arb ID Type

Set this field according to how many bits make up the CAN message Arbitration ID.

The choices are:

* Standard 11 bit (default) - Arb ID will range from $000 to $7FF (3 characters wide).
* Extended 29 bit - Arb ID will range from $00000000 to $1FFFFFFF (8 characters wide).
* Any - any type of Arb ID will be accepted, 11 bit or 29 bit.

### LIN - Message Type

Sets the LIN message type to be Master, Slave, Break Only, or Header only.
