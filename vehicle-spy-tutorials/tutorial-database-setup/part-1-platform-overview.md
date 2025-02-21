# Part 1 - Platform Overview

### 1. What are Database Platforms and why are they helpful?:

The first aspect to look at is what a Database Platform is used for. In Vehicle Spy 3, a Platform is a collection of database files. The main feature that makes a Platform beneficial is keeping all the required database files linked and easy to switch between. For testing, a 2015 platform and a 2016 platform can be created. When a switch is needed, simply select the correct platform from a dropdown list.

### 2. Needed files for a platform:

Building a database platform does require database files. Database files come in a multitude of different file types. For CAN, the most common type is a \*.DBC file. Another common type is a \*.UEF type file. When working with LIN, \*.LDF is the common format. Vehicle Spy 3 also supports \*.VS3 and \*.VSDB files to act as database files. \*.VS3 and \*.VSDB files are a Vehicle Spy specific file format.\
\
Diagnostic decoding databases also come in a number of different formats. Most formats are specific to an OEM. The common format is the \*.ODX file type. In building a platform, a number of different database types can be added. Vehicle Spy takes all the diagnostic database information and stores it into a \*.GMD file. This holds diagnostic information imported from a database and entered in by hand into the [ECU Diagnostic Database View](../../vehicle-spy-main-menus/main-menu-setup/ecus-view/).
