import winsound
import time
import sys
import os
def morse(char):
    code = { 'a':'.-', 'b':'-...', 
                    'c':'-.-.', 'd':'-..', 'e':'.', 
                    'f':'..-.', 'g':'--.', 'h':'....', 
                    'i':'..', 'j':'.---', 'k':'-.-', 
                    'l':'.-..', 'm':'--', 'n':'-.', 
                    'o':'---', 'p':'.--.', 'q':'--.-', 
                    'r':'.-.', 's':'...', 't':'-', 
                    'u':'..-', 'v':'...-', 'w':'.--', 
                    'x':'-..-', 'y':'-.--', 'z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ':'.....'} 
    trans = ''  

    if char.startswith('.') or char.startswith('−'):
        codeen = dict([(a, b) for b, a in code.items()])
        char = char.split(' ')
        for x in char:
            trans += codeen.get(x)    

    else:
        char = char.lower()
        for x in char:
            trans += code.get(x) + ' '
    return trans.strip()

os.system('cls')
message = input('What would you like to see typed in morse code?\n>>>')
message = morse(message)
print(message)
hear = input('Would you like to hear what that sounds like? (Type n if you don\'t, any other input will play the audio)\n>>>').lower()
if hear == 'n':
    sys.exit()
noise = [message[i:i+1] for i in range(0, len(message), 1)]
line = ''
charcount = 0
while charcount < len(noise): 
    os.system('cls')
    line = line + (noise[charcount])
    print(line)
    if noise[charcount] == '.':
        winsound.Beep(440, 200)
    if noise[charcount] == '-':
        winsound.Beep(440, 600)
    if noise[charcount] == ' ':
        time.sleep(.5)
    charcount += 1
    
