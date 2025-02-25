# 100 Day Of Code : The Complete Python Pro Bootcamp
# Day 82 - Project Morse Code
MORSE_CODE = { 'A':'.-', 'B':'-...',
               'C':'-.-.', 'D':'-..', 'E':'.',
               'F':'..-.', 'G':'--.', 'H':'....',
               'I':'..', 'J':'.---', 'K':'-.-',
               'L':'.-..', 'M':'--', 'N':'-.',
               'O':'---', 'P':'.--.', 'Q':'--.-',
               'R':'.-.', 'S':'...', 'T':'-',
               'U':'..-', 'V':'...-', 'W':'.--',
               'X':'-..-', 'Y':'-.--', 'Z':'--..',
               '1':'.----', '2':'..---', '3':'...--',
               '4':'....-', '5':'.....', '6':'-....',
               '7':'--...', '8':'---..', '9':'----.',
               '0':'-----', ', ':'--..--', '.':'.-.-.-',
               '?':'..--..', '/':'-..-.', '-':'-....-',
               '(':'-.--.', ')':'-.--.-'}

def encode_massage(massage):
    cipher = ''
    for letter in massage:
        if letter != ' ':
            cipher += MORSE_CODE[letter] + ' '
        else:
            cipher += ' '
    return cipher

def decode_massage(massage):
    massage += ' '
    decipher = ''
    citext = ''
    for letter in massage:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i+=1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(citext)]
                citext = ''
    return decipher

def main():
    end_program = False
    print("MORSE CODE.")
    while end_program == False:
        mode_massage = input("Want to decode or encode your message? input d - for decode or e to encode to morse. :")
        if mode_massage == 'd' :
            massage = input("Your massage: ")
            result = decode_massage(massage)
            print(f'Decode massage: {result}')
        elif mode_massage == 'e' :
            massage = input("Your massage: ")
            result = encode_massage(massage.upper())
            print(f'Encode massage: {result}')
        else :
            print("option not recognized")

        print("\n" * 3)
        repeat_option = input("Repeat program? y/n :")
        if repeat_option == 'n' :
            end_program = True
        if repeat_option == 'y' :
            print("\n" * 100)

if __name__ == '__main__':
    main()