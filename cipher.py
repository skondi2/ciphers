
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
exitProgram = False

while not exitProgram:
    messageString = input("Enter original message : ")
    shift = input('Enter shift : ')

    caesar = False
    polyAlpha = False

    if shift.isdigit():
        shift = int(shift)
        caesar = True
    else:
        polyAlpha = True

    # CAESAR CIPHER
    if caesar:

        cipheredMessage = []

        for letter in messageString:
            for alphabetLetter in alphabet:

                if letter == alphabetLetter:
                    cipherPosition = (alphabet.index(alphabetLetter) + shift) % 26
                    cipheredMessage.append(alphabet[cipherPosition])

                elif letter.upper() == alphabetLetter:
                    cipherPosition = (alphabet.index(alphabetLetter.upper()) + shift) % 26
                    cipheredMessage.append(alphabet[cipherPosition].lower())

        cipheredString = ""
        cipheredString = cipheredString.join(cipheredMessage)
        print(cipheredString)

    # POLY ALPHABETIC CIPHER
    if polyAlpha:

        cipheredMessage = []

        shiftCode = []
        for shifter in shift:
            for alphabetLetter in alphabet:

                if shifter.upper() == alphabetLetter:
                    shiftCode.append((alphabet.index(alphabetLetter)) + 1)

        shiftPerLetter = []
        messageIndex = 0
        while messageIndex != len(messageString):
            shiftPerLetter.append(shiftCode[messageIndex % len(shiftCode)])
            messageIndex += 1

        messageIndex = 0
        while messageIndex != len(messageString):
            cipherPosition = (alphabet.index(messageString[messageIndex].upper()) + shiftPerLetter[messageIndex]) % 26
            if messageString[messageIndex].islower():
                cipheredMessage.append(alphabet[cipherPosition].lower())
            else:
                cipheredMessage.append(alphabet[cipherPosition])
            messageIndex += 1

        cipheredString = ""
        cipheredString = cipheredString.join(cipheredMessage)
        print(cipheredString)

    x = input("Exit program? YES or NO \n")
    if x == "YES" or x == "yes":
        exitProgram = True
    else:
        exitProgram = False










