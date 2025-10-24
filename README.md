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
Registers:
A - Accumulator
Q - Adress
R - Return line
C - Program-counter

Basic
- LOAD
- READ
- STORE

Arithmetic
- ADD
- SUB

Jumps
- JUMP
- JZERO
- JNEG
- OVCHK
- SWTO
- RETURN

i/o
- XINPUT
- DRAW


# LOAD X/ MEM
Puts argument in A
A <= X/ RAM[Q]

# READ X/ MEM
Pus argument in Q
Q <= X/ RAM[Q]

# STORE X/ MEM
Puts value in A into argument of RAM
RAM[X/ RAM[Q]] <= A

# ADD X/ MEM
Basic addition of argument on A
A <= A + X/ RAM[Q]

# SUB X/ MEM
Basic subtraction of argument on A
A <= A - X/ RAM[Q]

# JUMP X/ MEM
Jump to line in argument, put in C
C <= X/ RAM[Q]

# JZERO X/ MEM
Jumps to line in argument if A==0, put in C, continues otherwise
C <= X/ RAM[Q] if A==0 else C+1

# JNEG X/ MEM
Jumps to line in argument if A<0, put in C, continues otherwise
C <= X/ RAM[Q] if A<0 else C+1

# OVCHK
Skips one line if previous operation on A caused an overflow, continues otherwise
C <= C+2 if OVCHK else C+1

# SWTO X
Switches to another Assembly file, must be a name in argument, only one switch can be done at a time
R <= C
C <= 0
file = X

# RETURN
Once the switch file has been completed, go back to main file at line in R
file = main
C <= R

# XINPUT X/ MEM
Check if input in argument is pressed, if True: skip one line, else continue, argument is [0,8]
