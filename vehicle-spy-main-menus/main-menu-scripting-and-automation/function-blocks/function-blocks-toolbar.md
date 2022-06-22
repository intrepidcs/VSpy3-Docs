# Function Blocks Toolbar

A number of essential tools are included in a row of buttons along the top of the [Function Blocks](./) area (Figure 1). These tools allow you to add function blocks, remove them, and perform other important operations.

![Figure 1: Function Block Toolbar buttons.](../../../.gitbook/assets/function\_block\_toolbar.gif)

### Function Block Controls

Table 1 illustrates and explains the toolbar controls seen in Figure 1.

**Table 1: Function Block Toolbar Controls**

| Button         | Icon                                                                                                    | Description                                                                                                                                                                                                                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add Block      | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_add.gif)             | Displays a submenu that allows you to add a new function block to the current setup. See below for details.                                                                                                                                                                                       |
| Delete Block   | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_delete.gif)          | <p>Deletes the function block currently selected in the <a href="function-block-list.md">Function Block List</a>. Vehicle Spy must be offline to delete a block.<br><br><strong>Note:</strong> Be sure you remember to choose the block you want to delete before pressing the delete button.</p> |
| Cut Block      | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_cut.gif)             | Copies the currently-selected function block to the Windows Clipboard, and then removes it from the list. Vehicle Spy must be offline to cut a block.                                                                                                                                             |
| Copy Block     | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_copy.gif)            | Copies the currently-selected function block to the Windows Clipboard without removing it.                                                                                                                                                                                                        |
| Paste Block    | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_paste.gif)           | Pastes a new copy of a function block previously added to the Windows Clipboard via the **Cut** or **Copy** buttons.                                                                                                                                                                              |
| Undo           | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_undo.gif)            | Reverses the last **Cut** or **Delete** operation.                                                                                                                                                                                                                                                |
| Disable Filter | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_disable\_filter.gif) | Clears any filters that have been entered into various columns in the [Function Block List](function-block-list.md).                                                                                                                                                                              |
| New Form       | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_new\_form.gif)       | Allows you to create a new Function Blocks window.                                                                                                                                                                                                                                                |
| Import         | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_import.gif)          | Opens a file selection dialog box where you can select a previously-saved function block to import into the current setup.                                                                                                                                                                        |
| Export         | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_export.gif)          | Allows you to save a function block using a **.vs3fb** extension so it can later be imported into Vehicle Spy.                                                                                                                                                                                    |
| Find           | ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_find.gif)            | Opens a small window that you can use to search within the contents of function blocks (see below).                                                                                                                                                                                               |

**Note:** The **Add**, **Delete**, **Cut**, **Copy**, **Paste** and **Undo** commands are also available in a right-click menu in the [Function Block List](function-block-list.md).

### Adding Function Blocks

To add a new function block, click the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_add.gif) button at the far left of the toolbar. A small submenu will appear, as shown in Figure 2. Select the type of function block you want to add, and it will be added to the function block list with a default name (which you can customize).

![Figure 2: Add Function Block submenu.](../../../.gitbook/assets/function\_blocks\_add\_submenu.gif)

### Searching Function Blocks

If you click the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_find.gif) button, Vehicle Spy will pop up a small dialog box to allow you to search for arbitrary text in any of your defined function blocks. At first, this dialog will only have a text box where you can enter the string to be found, with a blue arrow button you can click to start the search. Each press of the search button will display the next occurrence of the search string.\
\
Press the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/fb\_toolbar\_+.gif) button next to the word **Options** to expand the box,revealing more options as shown in Figure 3.

![Figure 3: Search Function Blocks dialog box.](../../../.gitbook/assets/function\_blocks\_search.gif)

The options are fairly self-explanatory, especially to anyone who has experience using a word processor:

* **Search Selected Block:** Vehicle Spy will only search the highlighted function block, as opposed to looking through all of them.
* **Case Sensitive:** Vehicle Spy will perform a case-sensitive search on the selected string.
* **Whole Word Only:** When checked, only whole words matching the string will be found; otherwise, partial matches will be included.
* **Direction:** Determines whether the search is done up or down through the function blocks.

Press the ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/fb\_toolbar\_-.gif) button to hide these options, or click ![](https://cdn.intrepidcs.net/support/VehicleSpy/assets/function\_block\_toolbar\_find.gif) again to hide the entire search box.
