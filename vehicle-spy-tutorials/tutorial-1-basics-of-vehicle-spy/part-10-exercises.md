# Part 10 - Exercises

This concludes all of the basic features in Vehicle Spy. Just to recap, the following subjects were covered:

* Loading a setup file with the Logon dialog
* Viewing message traffic, both scrolling and static
* Specifying a message through the Message Editor view
* Viewing messages in Messages view
* Setting up custom filters
* Filtering using column filters
* Turning filters on/off and switching between include and exclude
* Absolute/Relative timestamps
* Pausing data
* Saving collected data to disk
* Clearing the Messages buffer

Before moving on to more complicated topics, take some time to complete the following exercises. Putting new skills into practice immediately helps to reinforce learning.



### Exercises

1\. Using the Filter bar, set up each of the following filter combinations. Describe their effect on your message traffic.

a. HS CAN included

b. HS CAN and J1850 VPW included

c. Network included and HS CAN excluded (Network is found under the Data Types heading in the Filter Panel.)

_\* Included = checkmark; Excluded = X_

2\. Do both of the following:

&#x20;a. Setup a message specification in the Message Editor.\
It must be a J1850 VPW message with Hex bytes **FF 40 60 03**.\
FF is Priority Type\
40 is Target\
60 is Source\
03 is Byte 1

b. Build a custom filter to include this message. Show only this message in Messages view.

3\.  Use column filters to filter for all CAN messages with **Arb ID 123** and **J1850** messages with header **FF**.\
**Hint:** Use a comma!

Great job! Take a short break if and then continue on to **Tutorial 2: Transmitting Messages with Vehicle Spy**.
