"""
Project: Chronos (CGC)

@author: original-elly
"""

import pygame as py

# Version 1


"""
*******************************************************************************
Registers and instructions:

- A:
    Permanent register
    Mathematical operations are done on this register
    
    Ex.:
        LOAD 5 (A <= 5)
        # A = 5
        ADD 5 (A <= A + 5)
        # A = 10
        SUB 10 (A <= A - 10)
        # A = 0
- Q:
    Temporary register
    Used for all MEM instructions
    Will be reset the line after it is called
    
    Ex.:
        READ 1 (Q <= 1)
        # Q = 1
        LOAD MEM (A <= Q, Q <= 0)
        # A = 1, Q = 0
        LOAD MEM (A <= Q, Q <= 0)
        # A = 0, Q = 0
    
- C:
    Incremental register
    Used to follow the lines of the code
    JUMP, OVCHK, and XINPUT can affect this register
    
    Ex.:
             # C = 0
        0    NOOP
             # C = 1
        1    NOOP
             # C = 2
        2    NOOP
             # C = 3
        3    NOOP
             # C = 4
        4    JUMP 3
             # C = 3 (loop)
    

- LOAD X / LOAD MEM:
    Puts argument in A
    A <= X
    or
    A <= RAM[Q] (MEM)

- READ X / LOAD MEM:
    Puts argument in Q
    Q <= X
    or
    q <= RAM[Q] (MEM)

- STORE X / STORE MEM:
    Puts element in A in RAM according to argument
    RAM[X] <= A
    or
    RAM[Q] <= A (MEM)

- ADD X / ADD MEM:
    Adds argument to element in A
    A <= A + X
    or
    A <= A + RAM[Q] (MEM)

- SUB X / SUB MEM:
    Substracts argument to element in A
    A <= A - X
    or
    A <= A - RAM[Q] (MEM)

- JUMP X / JUMP MEM:
    Jumps to the line in argument; Puts the argument in C
    C <= X
    or
    C <= RAM[Q] (MEM)

- JZERO X / JZERO MEM:
    Jumps to the line in argument if A is equal to 0
    if A == 0:
        C <= X
        or
        C <= RAM[Q] (MEM)
    else:
        C <= C + 1

- JNEG X / JNEG MEM:
    Jumps to the line in argument if A lesser than 0
    if A < 0:
        C <= X
        or
        C <= RAM[Q] (MEM)
    else:
        C <= C + 1

- OVCHK:
    If previous operation caused an overflow in A, skips a line
    When an overflow occurs, OVCHK is True for one operation
    Doesn't take arguments
    
    if OVCHK:
        C <= C + 2
    
    if not OVCHK:
        C <= C + 1

- DRAW X / DRAW MEM:
    
    [ON HOLD]

- XINPUT X / XINPUT MEM:
    Jumps a line if the input in argument is equal to 1, 3bits for 8 inputs
    
    if XINPUT 0:
        C <= C + 2
    else:
        C <= C + 1
        
    or 
    
    if XINPUT RAM[Q]: (MEM)
        C <= C + 1
    else:
        C <= C + 1

- NOOP:
    Does nothing for one line
    Doesn't take arguments
    C <= C + 1
    
*******************************************************************************
"""


# Instructions
instruc = ["LOAD", "READ", "STORE", "ADD", "SUB", "JUMP", "JZERO", "JNEG", "OVCHK", "DRAW", "XINPUT", "NOOP"]

# Registers
A = 0
Q = 0
C = 0
ovchk = False
max_val = 1

# RAM
RAM = [0 for _ in range(16)]

# Inputs
input_list = ["up", "down", "left", "right", "a", "b", "start", "select"]


error_list = ["TypeError", "NameError", "IndexError"]


# Instruction functions

def op(op, x):
    global A, Q, C, RAM, max_val, ovchk
    try:
        if x == "MEM": 
            x = RAM[Q]
        if x is not str or x is not int:
            return "TypeError"
        if op == "LOAD":
            A = x
            C += 1
        elif op == "READ":
            Q = x
            C += 1
        elif op == "STORE":
            RAM[x] = A
            C += 1
        elif op == "ADD":
            A += x
            if A > max_val:
                ovchk = True
            C += 1
        elif op == "SUB":
            A -= x
            C += 1
        elif op == "DRAW": # pygame ###########################################
            pass
        elif op == "XINPUT": # pygame #########################################
            if x > 7:
                return "IndexError"
            pass
        elif op == "JUMP":
            C = x
        elif op == "JZERO":
            C = x if A == 0 else C + 1
        elif op == "JNEG":
            C = x if A < 0 else C + 1
        elif op == "OVCHK":
            C += 2 if ovchk else 1
        elif op == "NOOP":
            C += 1
        else:
            return "NameError"
        return None
    except IndexError:
        return "IndexError"

op("LOAD", [1,2,3])


def read_instructions(file):
    pass