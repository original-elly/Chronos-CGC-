\- Chronos (CGC) -



Chronos Guidance Computer

===========================================================================

Chronos v.1 is an Assembly interpreter project to make games with my own Assembly language. This is done 

before learning about the right way to make an Assembly language. This project is only a test to see what I can

do with my knowledge in Assembly and Python. Hence, this will use a proto-Assembly and Pygame to make

an interface.



Chronos v.2 will be made after this one and will be an actual Assembly interpreter with a better interface.



The name CGC is a reference to the AGC (Apollo Guidance Computer).





Instructions and registers

===========================================================================

\- A:

&nbsp;   Permanent register

&nbsp;   Mathematical operations are done on this register

&nbsp;   

&nbsp;   Ex.:

&nbsp;       LOAD 5 (A <= 5)

&nbsp;       # A = 5

&nbsp;       ADD 5 (A <= A + 5)

&nbsp;       # A = 10

&nbsp;       SUB 10 (A <= A - 10)

&nbsp;       # A = 0

\- Q:

&nbsp;   Temporary register

&nbsp;   Used for all MEM instructions

&nbsp;   Will be reset the line after it is called

&nbsp;   

&nbsp;   Ex.:

&nbsp;       READ 1 (Q <= 1)

&nbsp;       # Q = 1

&nbsp;       LOAD MEM (A <= Q, Q <= 0)

&nbsp;       # A = 1, Q = 0

&nbsp;       LOAD MEM (A <= Q, Q <= 0)

&nbsp;       # A = 0, Q = 0

&nbsp;   

\- C:

&nbsp;   Incremental register

&nbsp;   Used to follow the lines of the code

&nbsp;   JUMP, OVCHK, and XINPUT can affect this register

&nbsp;   

&nbsp;   Ex.:

&nbsp;            # C = 0

&nbsp;       0    NOOP

&nbsp;            # C = 1

&nbsp;       1    NOOP

&nbsp;            # C = 2

&nbsp;       2    NOOP

&nbsp;            # C = 3

&nbsp;       3    NOOP

&nbsp;            # C = 4

&nbsp;       4    JUMP 3

&nbsp;            # C = 3 (loop)

&nbsp;   



\- LOAD X / LOAD MEM:

&nbsp;   Puts argument in A

&nbsp;   A <= X

&nbsp;   or

&nbsp;   A <= RAM\[Q] (MEM)



\- READ X / LOAD MEM:

&nbsp;   Puts argument in Q

&nbsp;   Q <= X

&nbsp;   or

&nbsp;   q <= RAM\[Q] (MEM)



\- STORE X / STORE MEM:

&nbsp;   Puts element in A in RAM according to argument

&nbsp;   RAM\[X] <= A

&nbsp;   or

&nbsp;   RAM\[Q] <= A (MEM)



\- ADD X / ADD MEM:

&nbsp;   Adds argument to element in A

&nbsp;   A <= A + X

&nbsp;   or

&nbsp;   A <= A + RAM\[Q] (MEM)



\- SUB X / SUB MEM:

&nbsp;   Substracts argument to element in A

&nbsp;   A <= A - X

&nbsp;   or

&nbsp;   A <= A - RAM\[Q] (MEM)



\- JUMP X / JUMP MEM:

&nbsp;   Jumps to the line in argument; Puts the argument in C

&nbsp;   C <= X

&nbsp;   or

&nbsp;   C <= RAM\[Q] (MEM)



\- JZERO X / JZERO MEM:

&nbsp;   Jumps to the line in argument if A is equal to 0

&nbsp;   if A == 0:

&nbsp;       C <= X

&nbsp;       or

&nbsp;       C <= RAM\[Q] (MEM)

&nbsp;   else:

&nbsp;       C <= C + 1



\- JNEG X / JNEG MEM:

&nbsp;   Jumps to the line in argument if A lesser than 0

&nbsp;   if A < 0:

&nbsp;       C <= X

&nbsp;       or

&nbsp;       C <= RAM\[Q] (MEM)

&nbsp;   else:

&nbsp;       C <= C + 1



\- OVCHK:

&nbsp;   If previous operation caused an overflow in A, skips a line

&nbsp;   When an overflow occurs, OVCHK is True for one operation

&nbsp;   Doesn't take arguments

&nbsp;   

&nbsp;   if OVCHK:

&nbsp;       C <= C + 2

&nbsp;   

&nbsp;   if not OVCHK:

&nbsp;       C <= C + 1



\- DRAW X / DRAW MEM:

&nbsp;   

&nbsp;   \[ON HOLD]



\- XINPUT X / XINPUT MEM:

&nbsp;   Jumps a line if the input in argument is equal to 1, 3bits for 8 inputs

&nbsp;   

&nbsp;   if XINPUT 0:

&nbsp;       C <= C + 2

&nbsp;   else:

&nbsp;       C <= C + 1

&nbsp;       

&nbsp;   or 

&nbsp;   

&nbsp;   if XINPUT RAM\[Q]: (MEM)

&nbsp;       C <= C + 1

&nbsp;   else:

&nbsp;       C <= C + 1



\- NOOP:

&nbsp;   Does nothing for one line

&nbsp;   Doesn't take arguments

&nbsp;   C <= C + 1





Other information will follow

===========================================================================

