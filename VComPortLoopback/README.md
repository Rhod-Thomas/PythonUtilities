Project supporting various kinds of loopback testing. 

Thoughts
-----------------
##
This is not fleshed out in my mind at all yet...
what could potentially be useful?

Open a serial port that has loopback wiring is a given.
What would be useful to do with that?

Test Different bauds? have two parallel Python processes, one sending tonnes of data and one receiving? And time it with different baud rates?
Test Different modes? (parity, stop bits). Is it possible to control these things in much detail?
Test RTC/CTS?
We could test various encryption schemes. Have two separate processes with access to the same keys.
Man in the middle attack testing? Change one bit by the man-in-the middle? Change the header?


