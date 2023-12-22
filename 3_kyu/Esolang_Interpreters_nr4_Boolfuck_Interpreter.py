# Esolang Interpreters #4 - Boolfuck Interpreter

# Topic:

'''
# Task: 
--------
DESCRIPTION:
Esolang Interpreters #4 - Boolfuck Interpreter
About this Kata Series
"Esolang Interpreters" is a Kata Series that originally began as three separate, independent esolang interpreter Kata authored by @donaldsebleung which all shared a similar format and were all somewhat inter-related. Under the influence of a fellow Codewarrior, these three high-level inter-related Kata gradually evolved into what is known today as the "Esolang Interpreters" series.

This series is a high-level Kata Series designed to challenge the minds of bright and daring programmers by implementing interpreters for various esoteric programming languages/Esolangs, mainly Brainfuck derivatives but not limited to them, given a certain specification for a certain Esolang. Perhaps the only exception to this rule is the very first Kata in this Series which is intended as an introduction/taster to the world of esoteric programming languages and writing interpreters for them.

The Language
Boolfuck is an esoteric programming language (Esolang) based on the famous Brainfuck (also an Esolang) which was invented in 2004 or 2005 according to the official website. It is very similar to Brainfuck except for a few key differences:

Boolfuck works with bits as opposed to bytes
The tape for Brainfuck contains exactly 30,000 cells with the pointer starting from the very left; Boolfuck contains an infinitely long tape with the pointer starting at the "middle" (since the tape can be extended indefinitely either direction)
Each cell in Boolfuck can only contain the values 0 or 1 (i.e. bits not bytes) as opposed to Brainfuck which has cells containing values ranging from 0 to 255 inclusive.
The output command in Boolfuck is ; NOT .
The - command does not exist in Boolfuck since either + or - would flip a bit anyway
Anyway, here is a list of commands and their descriptions:

+ - Flips the value of the bit under the pointer
, - Reads a bit from the input stream, storing it under the pointer. The end-user types information using characters, though. Bytes are read in little-endian order—the first bit read from the character a, for instance, is 1, followed by 0, 0, 0, 0, 1, 1, and finally 0. If the end-of-file has been reached, outputs a zero to the bit under the pointer.
; - Outputs the bit under the pointer to the output stream. The bits get output in little-endian order, the same order in which they would be input. If the total number of bits output is not a multiple of eight at the end of the program, the last character of output gets padded with zeros on the more significant end.
< - Moves the pointer left by 1 bit
> - Moves the pointer right by 1 bit
[ - If the value under the pointer is 0 then skip to the corresponding ]
] - Jumps back to the matching [ character, if the value under the pointer is 1
If you haven't written an interpreter for Brainfuck yet I recommend you to complete this Kata first.

The Task
Write a Boolfuck interpreter which accepts up to two arguments. The first (required) argument is the Boolfuck code in the form of a string. The second (optional) argument is the input passed in by the end-user (i.e. as actual characters not bits) which should default to "" if not provided. Your interpreter should return the output as actual characters (not bits!) as a string.

def boolfuck(code, input)
Preloaded for you is a function brainfuckToBoolfuck()/brainfuck_to_boolfuck()/BrainfuckToBoolfuck() which accepts 1 required argument (the Brainfuck code) and returns its Boolfuck equivalent should you find it useful.

Please note that your interpreter should simply ignore any non-command characters. This will be tested in the test cases.

If in doubt, feel free to refer to the official website (link at top).

Good luck :D

Kata in this Series
Esolang Interpreters #1 - Introduction to Esolangs and My First Interpreter (MiniStringFuck)
Esolang Interpreters #2 - Custom Smallfuck Interpreter
Esolang Interpreters #3 - Custom Paintfuck Interpreter
Esolang Interpreters #4 - Boolfuck Interpreter

# Sample Tests:
---------------
import codewars_test as test
from solution import boolfuck
from preloaded import brainfuck_to_boolfuck

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Empty Test Cases')
    def basic_test_cases():
        test.assert_equals(boolfuck("", ""), "")
        test.assert_equals(boolfuck(brainfuck_to_boolfuck(""), ""), "")

    @test.it("Single command tests")
    def basic_test_cases():
        test.assert_equals(boolfuck("<"), "")
        test.assert_equals(boolfuck(">"), "")
        test.assert_equals(boolfuck("+"), "")
        test.assert_equals(boolfuck("."), "")
        test.assert_equals(boolfuck(";"), "\u0000")

    @test.it("I/O tests")
    def basic_test_cases():
        test.assert_equals(boolfuck(brainfuck_to_boolfuck(",."), "*"), "*")

    @test.it("Hello World test")
    def basic_test_cases():
        test.assert_equals(boolfuck(";;;+;+;;+;+;+;+;+;+;;+;;+;;;+;;+;+;;+;;;+;;+;+;;+;+;;;;+;+;;+;;;+;;+;+;+;;;;;;;+;+;;+;;;+;+;;;+;+;;;;+;+;;+;;+;+;;+;;;+;;;+;;+;+;;+;;;+;+;;+;;+;+;+;;;;+;+;;;+;+;+;", ""), "Hello, world!\n")

    @test.it("Basic tests")
    def basic_test_cases():
        test.assert_equals(boolfuck(">,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<;>;>;>;>;>;>;>;<<<<<<<,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]", "Codewars\u00ff"), "Codewars")
        test.assert_equals(boolfuck(">,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>;>;>;>;>;>;>;>;>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]", "Codewars"), "Codewars")
        test.assert_equals(boolfuck(">,>,>,>,>,>,>,>,>>,>,>,>,>,>,>,>,<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]>[>]+<[+<]>>>>>>>>>[+]>[>]+<[+<]>>>>>>>>>[+]<<<<<<<<<<<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>>>>>>>>>>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<<<<<<<<<<<<<<<<<<<[>]+<[+<]>>>>>>>>>[+]>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]<<<<<<<<<<<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>>>>>>>>>>>>>>>>>>>;>;>;>;>;>;>;>;<<<<<<<<", "\u0008\u0009"), "\u0048")


# Code:
--------
 def boolfuck(code, input=""):
    pass

'''
# Solution
def boolfuck(code, input=""):
    # Convert input string to a list of bits in little-endian order
    # Each character is converted to its ASCII value in binary, then reversed
    input_bits = ''.join([f'{ord(c):08b}'[::-1] for c in input])
    input_index = 0  # Index to track the current position in the input bits

    # Initialize the tape (memory) and the pointer
    tape = [0]  # Start with a single cell initialized to 0
    pointer = 0  # Pointer starts at the first cell

    # List to store output bits
    output_bits = []

    # Command pointer to track the current position in the Boolfuck code
    cmd_ptr = 0

    # Main loop to iterate through the Boolfuck code
    while cmd_ptr < len(code):
        cmd = code[cmd_ptr]  # Current command

        # Handle each command according to Boolfuck specifications
        if cmd == '>':
            pointer += 1  # Move pointer to the right
            # Extend the tape if the pointer moves beyond the current length
            if pointer == len(tape):
                tape.append(0)
        elif cmd == '<':
            pointer -= 1  # Move pointer to the left
            # Extend the tape at the beginning if the pointer moves before the first cell
            if pointer < 0:
                tape.insert(0, 0)
                pointer = 0
        elif cmd == '+':
            tape[pointer] ^= 1  # Flip the bit at the current pointer position
        elif cmd == ',':
            # Read a bit from the input and store it at the current pointer position
            if input_index < len(input_bits):
                tape[pointer] = int(input_bits[input_index])
                input_index += 1
            else:
                tape[pointer] = 0  # If no more input, store 0
        elif cmd == ';':
            # Output the bit at the current pointer position
            output_bits.append(str(tape[pointer]))
        elif cmd == '[':
            # Jump past the matching ']' if the bit at the pointer is 0
            if tape[pointer] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    cmd_ptr += 1
                    if code[cmd_ptr] == '[':
                        open_brackets += 1
                    elif code[cmd_ptr] == ']':
                        open_brackets -= 1
        elif cmd == ']':
            # Jump back to the matching '[' if the bit at the pointer is 1
            if tape[pointer] != 0:
                close_brackets = 1
                while close_brackets != 0:
                    cmd_ptr -= 1
                    if code[cmd_ptr] == ']':
                        close_brackets += 1
                    elif code[cmd_ptr] == '[':
                        close_brackets -= 1

        cmd_ptr += 1  # Move to the next command

    # Convert output bits to string
    # Here, we group the output bits into bytes (8 bits each).
    # If the last group has fewer than 8 bits, it's padded with zeros.
    # Each byte is then converted to a character using little-endian order.
    output = ''
    for i in range(0, len(output_bits), 8):
        byte = output_bits[i:i+8]
        # Pad with zeros if necessary to form a complete byte
        byte += ['0'] * (8 - len(byte))
        # Convert the byte (in little-endian order) to a character and add to the output
        output += chr(int(''.join(byte[::-1]), 2))

    return output

# Description:
'''
In this task, I created an interpreter for the esoteric programming language Boolfuck. Boolfuck is a variation of Brainfuck that operates with bits instead of bytes. 
The main challenge was to accurately interpret Boolfuck code, processing its instructions and managing data according to the language's rules.

'''

