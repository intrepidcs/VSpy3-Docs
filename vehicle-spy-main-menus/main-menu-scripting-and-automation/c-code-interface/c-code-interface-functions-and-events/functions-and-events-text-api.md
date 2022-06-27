# Functions and Events: Text API

Vehicle Spy can be automated with the [Text API](../../../../vehicle-network-interface-hardware/vehicle-spy-text-api/). The Text API is a text based command and control API that allows every part of Vehicle Spy to be changed or queried with text. Please see the IntrepidCS API documentation for more information on the Text API. There are two APIs that give you access to the text API: Spy\_TextAPI() and Spy\_TextAPI\_W(). The difference is that the W uses unicode characters that can be helpful for Japanese, Chinese, Korean, etc.\
\
These functions return a 1 (success) or 0 (failure).  The most common cause for failure is that you have a command that Vehicle Spy cannot understand. Use the Text API Terminal in Vehicle Spy to learn how to use the text api.

![Figure 1: The Text API allows you to control almost every aspect of Vehicle Spy.](../../../../.gitbook/assets/spy\_textapi.gif)
