from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Alphabet array - Do NOT modify, unless translating app ;)
ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
    'o','p','q','r','s','t','u','v','w','x','y','z']

# Method to find character's position in alphabet array
def findPos(ch):
    count = 0
    for letter in ALPHABET:
        if letter == ch.lower():
            # Returning position in alphabet array
            # that the character was found at
            return count
        count += 1
    
    # If is non-alphabetic character, simply return -1
    return -1

# Encode/Decode functions
def encode(shift):
    # Encode here...
    
    # Input/Output files for encoding
    inFile = open('decoded.txt', 'r')
    outFile = open('encoded.txt', 'w')

    # Array for holding encoded lines
    lines = []

    # Nested for loops, looping through each line in the file,
    # and each character of each line, and shifting them
    for line in inFile:
        encodedLine = ''
        for ch in line:
            encodedChar = ch
            position = findPos(ch)
            if position > -1: # Character is alphabetic
                encodedPos = position + shift
                if encodedPos >= 26:
                    # Changing encoded position value to shift back to the 
                    # beginning of the alphabet if needed
                    encodedPos -= 26 
                
                # Setting encoded char to letter in alphabet array,
                # based on the encoded position determined
                encodedChar = ALPHABET[encodedPos]
            
            # Adding encoded char to current encoded line
            encodedLine += encodedChar

        # Adding newly encoded line to lines array
        lines.append(encodedLine)

    # Writing encoded message to output file
    for line in lines:
        outFile.write(line)

    # Closing input and output files
    inFile.close()
    outFile.close()

def decode(shift):
    # Decode here...
    inFile = open('encoded.txt', 'r')
    outFile = open('decoded.txt', 'w')

    # Array for holding decoded lines
    lines = []

    # Nested for loops, looping through each line in the file,
    # and each character of each line, and shifting them
    for line in inFile:
        decodedLine = ''
        for ch in line:
            decodedChar = ch
            position = findPos(ch)
            if position > -1: # Character is alphabetic
                decodedPos = position - shift
                if decodedPos <= -1:
                    # Changing encoded position value to shift forward to the 
                    # end of the alphabet if needed
                    decodedPos += 26
                
                # Setting encoded char to letter in alphabet array,
                # based on the encoded position determined
                decodedChar = ALPHABET[decodedPos]
            
            # Adding encoded char to current encoded line
            decodedLine += decodedChar

        # Adding newly encoded line to lines array
        lines.append(decodedLine)

    # Writing encoded message to output file
    for line in lines:
        outFile.write(line)

    # Closing input and output files
    inFile.close()
    outFile.close()

# Event handlers
def run(*args):
    try:
        shift = int(shiftVal.get())
        # Checking to ensure shift value is positive
        if shift < 1:
            messagebox.showerror("Error", "Enter a shift value of 1 or more")
        
        if int(option.get()) == 0:
            encode(shift)
        elif int(option.get()) == 1:
            decode(shift)
        else:
            messagebox.showerror("Error", "Select an action")
        shiftVal.set("")
    except ValueError:
        # Displaying error message for non-numeric input
        messagebox.showerror("Error", "Enter a numeric value for the shift. (e.g., 4, 10, etc.)")
        pass

# Root/mainframe configuration
root = Tk()
root.title("Caesar Shift Cipher")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variables
option = IntVar()
shiftVal = StringVar()

# Widgets
ttk.Label(mainframe, text="Select an option:").grid(column=0, row=0)
radEncode = ttk.Radiobutton(mainframe, text="Encode", variable=option, value=0)
radEncode.grid(column=0, row=1)
radDecode = ttk.Radiobutton(mainframe, text="Decode", variable=option, value=1)
radDecode.grid(column=0, row=2)
ttk.Label(mainframe, text="Enter a shift value:").grid(column=0, row=3)
txtShiftVal = ttk.Entry(mainframe, textvariable=shiftVal)
txtShiftVal.grid(column=0, row=4)
btnGo = ttk.Button(mainframe, text="Go!", command=run)
btnGo.grid(column=0, row=5)

# Final config and run
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
