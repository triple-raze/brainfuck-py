def decompress(inputString): 
    
    charCount = ""      # число в виде строки, т. к. цифры нужно не суммировать
    finalString = ""    # вывод

    for char in inputString:
        if char.isdigit():
            charCount = charCount + char
        
        else:
            if charCount == "":
                letterOutput = char
            else:
                letterOutput = char * int(charCount)

            charCount = ""
            finalString = finalString + letterOutput
    
    return finalString


def compress(inputString):
    
    charCount = 1
    finalString = ""

    for index in range(1, len(inputString)):    # итерации начинаются с 1, т. к. нужно проверять символы парами

        firstChar = inputString[index]
        secondChar = inputString[index - 1]                         
        thirdChar = inputString[index - 2] if index >= 2 else ""    # "" нужен для того, чтоб isdigit работал на thirdchar
    
        if secondChar == firstChar and not secondChar.isdigit() and not thirdChar.isdigit():
            charCount += 1

        else:
            if charCount == 1:
                finalString += f"{secondChar}"
            else:
                finalString += f"{charCount}{secondChar}"
            charCount = 1

    if charCount == 1:
        finalString += f"{firstChar}"
    else:
        finalString += f"{charCount}{firstChar}"
    
    return finalString


def convertString(inputString, lightMode=True):
    print(inputString)
    output = ""
    
    for char in inputString:
        output += f"{ord(char)}+.>"
            
    return output

