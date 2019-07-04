Overview

This is a Python/Tkinter application that can read a file, shift all alphabetic letters by a user-specified amount,
and output the shifted value to a file.  The program can also reverse encrypted information from one file, shifting it back by a
specific amount, and writing it to a file.


Usage

All files needed for this application to run are in the caesarShift folder.  To run, open a terminal or command prompt, 
and navigate to where ever you have stored the caesarShift folder.  Once inside, run the "main.py" file, by calling
the python interpreter like so: "py main.py" on windows, or "python3 main.py" on linux.  
The actual interface is pretty straight forward.  Choose an option, whether to decode, or encode, and enter a value to shift by.
The program gets it's input from the "decoded.txt" and "encoded.txt" files included in the main folder.  If you want to encrypt,
type your plain text into the decoded.txt file, select the encode option, and enter a value to shift by.  The encrypted
text will be written to the encoded.txt file.  To decrypt, simply enter your encrypted text in the encoded.txt file,
select the decode option, and enter the shift value to decrypt by.  The decrypted text will be written to the decoded.txt file.


Requirements
You will simply need python 3.6 or greater to run this app.
