# C Code Interface: Object Names, Debugging, and Common Mistakes

### The Importance of an Object Name in a C Code Project

After your project is built you can run it over and over.  The project from that point, just like C, references every object in Vehicle Spy by name. So, if you change the name or delete an object in your Vehicle Spy setup that you use in a C project you will need to open Visual Studio and rebuild the project. This also means the C code projects can be reused across Vehicle Spy setups if you manage to keep the names the same for the objects you use.

![Figure 1: Vehicle Spy attempts to find the objects you used in Vehicle Spy using object names but if it cannot you will get an error.](../../../.gitbook/assets/name\_lookup\_error.png)

### Debugging Your C Code

Visual Studio supports debugging two ways.  First, is it will launch Vehicle Spy every time you press run.  Another allows you to connect to a running copy of Vehicle Spy (called attach to process) Vehicle Spy will allow you to build and connect to it when Vehicle Spy is not online. Therefore, the most productive way is attaching to an existing Vehicle Spy. Only Visual Studio standard edition or better supports attaching to an existing Vehicle Spy.\
\
You cannot build your project when Vehicle Spy has the C code loaded. Therefore, you must go offline in Vehicle Spy in order to fully build your project.

![Figure 2: Attach to process allows you to connect to an already running copy of Vehicle Spy for debugging.](../../../.gitbook/assets/attach\_to\_process.gif)

![Figure 3: Step 2 of attach to process - select vspy3.exe - make sure Vehicle Spy is offline!
](../../../.gitbook/assets/attach\_to\_process2.gif)

![Figure 4: The Visual Studio debugger in operation.](../../../.gitbook/assets/debugger.png)

### Common Mistakes for Building your project

1\) You created an event function, but did not implement it in SpyCCode.c. This causes a linker error. Make sure to copy the C function from the Event Code tab in the edit dialog for the C code module.

![Figure 5: A linker error will occur if you setup an event but don't implement the function in SpyCCode.C.](../../../.gitbook/assets/troubleshooting\_linkererror.gif)

2\) You try to build the project while Vehicle Spy is online. The project is loaded. Go Offline in Vehicle Spy and then build the project.

![Figure 6: A linker error will occur if you build and Vehicle Spy is online.](../../../.gitbook/assets/troubleshooting\_loaded.gif)
