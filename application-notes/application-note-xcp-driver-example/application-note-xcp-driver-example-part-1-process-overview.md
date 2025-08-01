# Application Note: XCP Driver Example - Part 1: Process Overview

### Process Overview

In creating your first application for XCP there are generally several steps that occur. These steps are given below:

1. Implement an XCP driver into your ECU code.
   1. Intrepid provides an example XCP driver in the files SpyCCode.c and SpyCCode.h contained in the Intrepid\_XCP\_Driver.zip file.
   2. The Microsoft Visual Studio Project (CXCPSim.vsproj), contained in the Intrepid\_XCP\_Driver.zip file can be used with Vehicle Spy's C Code interface to allow you to test, understand and modify the XCP driver implementation.
2. \[optional step] Using the compiler and linker for your ECU, generate a supported debugger format to be read into the Intrepid ASAP2 editor. Supported formats include:
   1. IEEE695
   2. ELF / DWARF
   3. MAP file
   4. COFF format for TI Processor\\
3. Load the generated debugger file into the Intrepid ASAP2 editor / creator. If you do not have a debugger file, you can enter all information into the ASAP2 editor / creator manually.
4. Enter information needed for the ASAP2 specification including:
   1. CRO
   2. DTO
   3. Scaling for symbols
   4. Association of symbols to one another
   5. DAQ table event information.
5. Generate an ASAP2 file
6. Load the ASAP2 file into Vehicle Spy
7. Use Vehicle Spy to connect to your ECU and perform the real-time memory monitoring and editing.
