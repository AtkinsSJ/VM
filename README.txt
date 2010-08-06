*So-Far Unnamed Thingy* is a simple command interpreter I wrote for
fun using Python. Programs are text files, with a single instruction on 
each line. Some instructions take an argument, which comes after the
instruction name, separated by a space. Whitespace at the beginning of
lines has no effect.

======== Storage =========

There are two storage areas - the memory, and the accumulator. The
memory is a theoretically-infinite set of integers, addressable using
integers. The accumulator is where calculations are carried out. All 
integers are potentially infinite in length.

======== Input/Output ==========

Values can be read-in from the user using GET and GETC, for getting
integers and characters respectively. PRINT and PRINTC output a given
variable as an integer or character. PRINTSTRING outputs the given
string, but this output is not currently alterable during runtime.

================================
======= Command Listing ========
================================
ADD: Add value from address
ADDVAL: Add value
AND: Performs a bitwise AND on the accumulator and the given address
DEBUG: Outputs all memory, and accumulator values
END: Ends the program
GET: Get a value from the user and store it at the address
GETC: Get a character from the user and store the ascii value at the address
GOTO: Go straight to the given line of the program (Files start line 1)
IFNEG: Only executes next instruction if the value of the accumulator is < 0
IFPOS: Only executes next instruction if the value of the accumulator is > 0
LOAD: Load value from address
LOADVAL: Load given value
NOT: Doews a binary-invert on the accumulator
OR: Performs a bitwise OR on the accumulator and the given address
PRINT: Output value from address
PRINTC: Outputs value from address, as ASCII character
PRINTSTRING: Outputs the remainder of the line to the user
SKIP: Jump over the given number of lines.
STORE: Save current value to address
XOR: Performs a bitwise XOR on the accumulator and the given address

REM is used to denote a comment.
