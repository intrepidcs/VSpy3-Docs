# Functions and Events: Timers

Timers generate events at specific time.  This time can be periodic or a one shot. The timer can be setup in Vehicle Spy totally or you can optionally control it with C functions. The table below shows the properties of the timer you can set in Vehicle Spy. The timer functions include the ability to read and write the current time and the ability to enable the timer.

**Table 1: Timer Properties that can be Configured in Vehicle Spy**

| Timer Property | Description                                      |
| -------------- | ------------------------------------------------ |
| Name           | Name of the timer in C code.                     |
| Description    | Description of what the timer does.              |
| Type           | Periodic or One shot.                            |
| RunAtStart     | Should the timer run when Vehicle Spy Starts.    |
| Initial Period | The period of the timer when Vehicle Spy Starts. |
| Resolution     | Millisecond or Microsecond timer resolution.     |

![Figure 1: Timer Functions to control the timer using C code.](../../../../.gitbook/assets/timer\_functions.gif)

![Figure 2: The Timer Events tab allows you to create a timer event at regular or single shot intervals.](../../../../.gitbook/assets/timer\_event.gif)

![Figure 3: The timer event is a simple function with no arguments that is called when the timer expires.](../../../../.gitbook/assets/timer\_event\_code.gif)
